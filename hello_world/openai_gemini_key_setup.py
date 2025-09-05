from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# just add these two lines two use the open ai code but with the gemini key
client = OpenAI(
    api_key="AIzaSyBs0ftLkZQSjIY1LOd2NVvbqY0s3PobYaY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# and change the model to gemini
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": "You are an expert in Maths and only and only ans maths realted questions. That if the query is not related to maths. Just say sorry and do not ans that." },
        { "role": "user", "content": "Hey, can you help me solve the a + b whole square"}
    ]
)

print(response.choices[0].message.content)