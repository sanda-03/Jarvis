from google import genai
client = genai.Client()
key="AIzaSyA5e7iOo71Kj-rEX__-RG4ZVHjxl8weMRw"
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)