import nltk
import google.generativeai as genai

nltk.download('punkt')
nltk.download('punkt_tab')

genai.configure(api_key="AIzaSyChU6b2V2ueWATMAw9utMVELietoVVTJZw")
model = genai.GenerativeModel("gemini-2.0-flash-exp")
