import requests
import os
from dotenv import load_dotenv

# Tải biến môi trường từ file .env
load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

repos = requests.get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100",
    auth=(USERNAME, TOKEN)
).json()

lang_totals = {}

for repo in repos:
    lang_url = repo['languages_url']
    langs = requests.get(lang_url, auth=(USERNAME, TOKEN)).json()
    for lang, bytes in langs.items():
        lang_totals[lang] = lang_totals.get(lang, 0) + bytes

total = sum(lang_totals.values())
for lang, bytes in lang_totals.items():
    percent = bytes / total * 100
    print(f"{lang}: {percent:.2f}%")
