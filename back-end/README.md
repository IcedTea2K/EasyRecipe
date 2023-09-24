# EasyRecipe Backend

## Installation
Build the provided Dockerfile by running `./build.sh`.

## Running
The Azure Form Recognizer endpoint URL and API key need to be provided in a `.env` file located in the main directory:


```
AZURE_FORM_RECOGNIZER_ENDPOINT=https://<custom_url>.cognitiveservices.azure.com/
AZURE_FORM_RECOGNIZER_KEY=<api_key>
```

Run the Docker image by passing in the `.env` file:
```bash
docker run --env-file .env -it receipt-parser
```