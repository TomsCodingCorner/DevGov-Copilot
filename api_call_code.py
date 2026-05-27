import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

PROJECT_ENDPOINT = os.getenv("AZURE_EXISTING_AIPROJECT_ENDPOINT")
AGENT_NAME = "DevGov"

if not PROJECT_ENDPOINT:
    raise ValueError("Missing AZURE_EXISTING_AIPROJECT_ENDPOINT in .env")

project_client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

openai_client = project_client.get_openai_client()

conversation = openai_client.conversations.create()

response = openai_client.responses.create(
    conversation=conversation.id,
    input="Tell me what you can help with.",
    extra_body={
        "agent_reference": {
            "name": AGENT_NAME,
            "type": "agent_reference",
        }
    },
)

print(response.output_text)