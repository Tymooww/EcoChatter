Installing EcoChatter requires a few steps. Make sure to follow them to avoid problems when running the program. Keep in mind that running LLMs locally requires strong hardware.

1. Clone the repository in PyCharm or any other Python IDE.
2. Install Python 3.10.11 and select it as python interpreter.
   Python 3.10.11: https://www.python.org/downloads/release/python-31011/
3. Install manditory pip packages via the terminal: "pip install langchain langchain-ollama langchain-huggingface langchain-google-genai langchain-openai langchain-community dotenv pypdf2 faiss-cpu google-genai".

Running the cloud models:
1. Create a new file called ".env" and add:
   GOOGLE_API_KEY=Your API key
   AZURE_OPENAI_API_KEY=Your API key
2. Generate your API keys at Microsoft Azure and Google AI Studio and add them to the .env file.
   Microsoft Azure: https://ai.azure.com/
   Google AI Studio: https://aistudio.google.com/

Running the local models:
1. Install Ollama at https://ollama.com/
2. Install Llama 3 in the Windows terminal: "ollama run llama3:8b" (4.7 GB of storage required)
3. Install Gemma 3 in the Windows terminal: "ollama run gemma3:4b" (3.3 GB of storage required)
4. Install Qwen 3 in the Windows terminal: "ollama run qwen3:8b" (5.2 GB of storage required)

Running the Gemma tokenizer (via Hugging Face):
1. Log in or create an account at https://huggingface.co/
2. Go to settings and click on access tokens.
3. Select create new token.
4. Tick all three options of repositories and inference.
5. Give the token a name, for example: "gemma-tokenizer".
6. Add "HF_token=Your key" with your key to the .env file.
7. Go to https://huggingface.co/google/gemma-3-4b-it and click "acknowledge license".
8. Enter the details and confirm.

The program has been built in iterations and each major iteration resulted in a new notebook. If you want to run the complete program use the generateBiodiversityReport notebook (or generateBiodiversityReportWithTokenization if you want to see the token usage), if you want to understand the inner workings per component better use the greeneryDataForNeighborhood (V1 is a JSON agent, V2 is a SQL agent) and retrieveGreeneryGoals (RAG system) notebooks. 
