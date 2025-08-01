import requests
from django.shortcuts import render

def fetch_news(request):
    # Replace YOUR_GNEWS_API_KEY with your actual GNews API key.
    api_url = "https://gnews.io/api/v4/top-headlines?token=bbc6c52ee3af530a5ec8d3f9660dabe7&lang=en&max=10"
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
