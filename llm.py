import requests
from prompt import RandomJapanesePrompt, prompt, BusinessJapanesePrompt
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def generate_response(japanese_sentence):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {
        'Content-Type': 'application/json'
    }
    
    question = 'Given sentence: "' + japanese_sentence + '", ' + prompt

    data = {
        "contents": [{
            "parts": [{"text": question}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['candidates'][0]['content']['parts'][0]['text']

def generate_random_japanese_sentence():

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "contents": [{
            "parts": [{"text": RandomJapanesePrompt}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['candidates'][0]['content']['parts'][0]['text']

def generate_business_japanese_translation(english_sentence):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "contents": [{
            "parts": [{"text": f'{BusinessJapanesePrompt}\n\nEnglish Sentence: "{english_sentence}"'}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['candidates'][0]['content']['parts'][0]['text']
