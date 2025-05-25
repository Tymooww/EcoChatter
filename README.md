Installing EcoChatter requires a few steps. Make sure to follow them to avoid problems when running the program. Keep in mind that running Llama 4 Scout requires some decent hardware to run, Llama3 should run fine on most hardware.

1. Clone the repository in PyCharm or any other Python IDE.
2. Install Python 3.10.11 and select it as python interpreter.
   Python 3.10.11: https://www.python.org/downloads/release/python-31011/
3. Install manditory pip packages via the terminal: "pip install langchain langchain-ollama langchain-huggingface langchain-google-genai langchain-openai langchain-community dotenv pypdf2 faiss-cpu".

Running the cloud models:
1. Create a new file called ".env" and add:
   GOOGLE_API_KEY=Your API key
   AZURE_OPENAI_API_KEY=Your API key
2. Generate your API keys at Microsoft Azure and Google AI Studio and add them to the .env file.
   Microsoft Azure: https://ai.azure.com/
   Google AI Studio: https://aistudio.google.com/

Running the local models:
1. Install Ollama at https://ollama.com/
2. Install Llama 3 in the Windows terminal: ollama run llama3 (5GB storage required)
3. Install Llama 4 Scout in the Windows terminal: ollama run llama4:scout (67GB storage required)

The program has been built in iterations and each major iteration resulted in a new notebook. If you want to run the complete program use the generateBiodiversityReport notebook, if you want to understand the inner workings per component better use the greeneryDataForNeighborhood (V1 is a JSON agent, V2 is a SQL agent) and retrieveGreeneryGoals (RAG system) notebooks. 
