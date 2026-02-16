import requests
from django.shortcuts import render
from django.contrib import messages

API_URL = "https://jsonplaceholder.typicode.com/posts"
REQUEST_TIMEOUT = 5  # seconds


def home(request):
    posts = []
    show_full_screen = False

    # Triggered when user clicks "START NOW"
    if request.GET.get('fetch_data'):
        try:
            response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()  # Raises HTTPError for bad responses

            data = response.json()

            # Safety check: ensure response is a list
            if isinstance(data, list):
                posts = data[:10]  # Limit to first 10 posts (clean UI)
                show_full_screen = True
            else:
                messages.error(request, "Unexpected API response format.")

        except requests.exceptions.Timeout:
            messages.error(request, "The request timed out. Please try again.")
        except requests.exceptions.ConnectionError:
            messages.error(request, "Connection error. Check your internet.")
        except requests.exceptions.HTTPError as e:
            messages.error(request, f"HTTP error: {e}")
        except ValueError:
            messages.error(request, "Invalid JSON response.")
        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")

    context = {
        'json_posts': posts,
        'show_full_screen': show_full_screen
    }

    return render(request, 'home.html', context)