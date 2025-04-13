from langchain_community.agent_toolkits.json.toolkit import JsonToolkit
from langchain_community.agent_toolkits.json.base import create_json_agent
from langchain_openai import AzureChatOpenAI
from langchain_community.tools.json.tool import JsonSpec
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()
'''chosen_llm = ChatOllama(base_url='http://localhost:11434', model="llama3")'''
chosen_llm = AzureChatOpenAI(model ="o3-mini", api_version="2025-01-01-preview", azure_endpoint="https://56948-m9bdjgpg-eastus2.cognitiveservices.azure.com/openai/deployments/o3-mini/chat/completions?api-version=2025-01-01-preview", api_key=os.environ.get("AZURE_OPENAI_API_KEY"))

# Retrieve and load up-to-date greenery data per neighborhood
dataset = requests.get('https://data.rivm.nl/geo/ank/ows?service=WFS&request=GetFeature&typeName=rivm_2022_groenpercentage_kaart_per_buurt&propertyName=bu_naam,_mean&outputFormat=json').json()

# Extract properties (not used anymore)
'''properties = []
neighborhoodGreenery = {}

for feature in dataset["features"]:
    properties.append(feature["properties"])

for property in properties:
    neighborhoodGreenery[property["bu_naam"]] = property["_mean"]

with open('groenPercentagePerBuurt.json', 'w') as file:
    json.dump(neighborhoodGreenery, file)
#print(properties)'''

# Create toolkit
json_spec = JsonSpec(dict_=dataset, max_value_length=4000)
json_toolkit = JsonToolkit(spec=json_spec)

# Create agent
json_agent_executor = create_json_agent(
    llm=chosen_llm,
    toolkit=json_toolkit,
    verbose=True,
    max_iterations=10
)

# Execute Agent
input_text = "Can you find out what the neighborhood Binnenstad-Noord has as _mean?"
response = json_agent_executor.invoke(input_text)
