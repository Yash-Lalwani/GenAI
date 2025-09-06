# Zero Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBjA34ENgeGNplvIqCP-qcH2fuMkqxdO7o",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero Shot Prompting: Directly giving the inst to the model
SYSTEM_PROMPT = "Your role is to only and only answer programming related questions in java language, if user asked a question which is not related to programming or in any other coding language just say sorry and do not ans that."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, Can you write a java code to print hello world" }
    ]
)

print(response.choices[0].message.content)
# 1. Zero-shot Prompting: The model is given a direct question or task without prior examples.