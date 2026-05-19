from langchain.chat_models import init_chat_model

GOOGLE_API_KEY = "AIzaSyDwvbJMhV4sxEc5DOOW4_6X2eojgMI8JPw"

model = init_chat_model(
    model='gemini-3.5-flash',
    model_provider='google-genai',
    api_key=GOOGLE_API_KEY)

with open('wood.txt') as file:
    wood = file.read()

response = model.invoke(f"Which of these woods is best for furniture? {wood}")

print(response.content[0]['text'])
