
import requests
from django.shortcuts import render

def home(request):
    json_posts = []
    show_full_screen = False
    
    # This triggers when you tap "START NOW"
    if 'fetch_data' in request.GET:
        # The specific JSON link you requested
        url = "https://jsonplaceholder.typicode.com/posts"
        try:
            response = requests.get(url)
            # Fetching the list of posts from the API
            json_posts = response.json() 
            show_full_screen = True
        except Exception as e:
            print(f"Connection Error: {e}")

    return render(request, 'home.html', {
        'json_posts': json_posts, 
        'show_full_screen': show_full_screen
    })