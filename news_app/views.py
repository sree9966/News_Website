import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render

# Loading environment variables from .env
load_dotenv()

def fetch_news(request):
    api_key = os.getenv("GNEWS_API_KEY")
    api_url =f"https://gnews.io/api/v4/top-headlines?token={api_key}&lang=en&country=in"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
        print("Fetched articles:", articles)  # Debug: Check terminal output
    except requests.RequestException as e:
        print("Error fetching news:", e)
        articles = []
    return render(request, "news_app/news_list.html", {"articles": articles})
