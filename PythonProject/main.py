from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

model = init_chat_model(
    model='gemini-3.5-flash',
    model_provider='google-genai',
    api_key=GOOGLE_API_KEY)

with open('wood.txt') as file:
    wood = file.read()

response = model.invoke(f"Which of these woods is best for furniture? {wood}")

print(response.content[0]['text'])
