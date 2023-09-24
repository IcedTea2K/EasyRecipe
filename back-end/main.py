from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from fastapi import FastAPI, File, UploadFile
import os
from search import searchFood

endpoint = os.environ.get("AZURE_FORM_RECOGNIZER_ENDPOINT")
key = os.environ.get("AZURE_FORM_RECOGNIZER_KEY")

document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

app = FastAPI()

def getReceiptItems(img):
	poller = document_analysis_client.begin_analyze_document(
		"prebuilt-receipt", document=img, locale="en-US"
	)
	receipts = poller.result()

	retObj = {"items": []}
	# print(receipts.documents)
	receipt = receipts.documents[0]
	if receipt.fields.get("MerchantName"):
		retObj["merchant_name"] = receipt.fields.get("MerchantName").value
	if receipt.fields.get("Items"):
		for idx, item in enumerate(receipt.fields.get("Items").value):
			item_description = item.value.get("Description")
			if item_description:
				retObj["items"].append(item_description.value)
	return retObj


@app.get("/")
async def root():
	return {"message": "Hello World"}

# @app.get("/parser")
# async def parser():
# 	with open('./imgs/img1.jpg', 'rb') as f:
# 		return getReceiptItems(f)

@app.post("/parser")
async def parseReceipt(file: UploadFile | None = None):
	if not file:
		return {"error": "No file sent"}

	# rawItems = getReceiptItems(file.file)
	rawItems = {
					"items": ["L&P SCE","NN OATS","T&T SWT CHILISCE","NN EGGS WH LRG","PHILA SOFT PLAIN","HOM MILK 3. 25%MF","RECYCLING FEE","NNI PEPPERS 2.5","FM ENG CKE 3CT","BANANA","TOMATO ROMA","GINGER ROOT","GROUND BEEF LEAN","CHKN LFC QUARTER","CHKN LEG QUARTER","PORK LN BNLS FZ"],
					"merchant_name": "RCSS"
				}
	retObj = {"raw": rawItems["items"], "items": [], "merchant_name": rawItems["merchant_name"]}

	# searchRes = searchFood(rawItems["merchant_name"] + " " + rawItems["items"][8])
	# print(searchRes["organic_results"][0]["title"])

	for rawItem in rawItems["items"]:
		searchRes = searchFood(rawItems["merchant_name"] + " " + rawItem)
		if not "organic_results" in searchRes:
			retObj["items"].append(rawItem)
		else:
			retObj["items"].append(searchRes["organic_results"][0]["title"])
	return retObj