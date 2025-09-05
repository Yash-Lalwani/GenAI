from google import genai

client = genai.Client(
    api_key="AIzaSyBs0ftLkZQSjIY1LOd2NVvbqY0s3PobYaY"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)

print(response.text)