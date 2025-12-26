import nltk
import google.generativeai as genai

nltk.download('punkt')
nltk.download('punkt_tab')

genai.configure(api_key="AIzaSyCNzzTK09CoQCQ0mn0etTwFkkbnWnzChiA")
model = genai.GenerativeModel("gemini-2.0-flash-exp")
