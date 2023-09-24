import requests
import os
import urllib.parse

key = os.environ.get("GOOGLE_SEARCH_KEY")
engineID = os.environ.get("GOOGLE_SEARCH_ENGINE_ID")
serpKey = os.environ.get("SERP_SEARCH_KEY")

def searchFood(query):
	# rq = "https://www.googleapis.com/customsearch/v1?key="+ key + "&cx=" + engineID + "&num=1"
															
	# rsp = requests.get(rq + "&q=" + urllib.parse.quote(query) + "&field=spelling,items(title)")
	# initialRsp = rsp.json()
	# if "spelling" in initialRsp:
	# 	rsp = requests.get(rq + "&q=" + initialRsp["spelling"]["correctedQuery"] + "&field=items(title)")

	url = "https://serpapi.com/search?engine=google&api_key=" + serpKey + \
					"&location=Vancouver&num=2&q=" + urllib.parse.quote(query)

	rsp = requests.get(url)

	return rsp.json()