from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from fastapi import FastAPI, File, UploadFile
import os

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
		retObj["merchant_name"] = receipt.fields.get("MerchantName")
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
	return getReceiptItems(file.file)