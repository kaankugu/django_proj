from django.http import JsonResponse
import requests

def get_popular_movies(request):
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

    headers = {
        "accept": "application/json",
     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2NTU0OTUxNzUwOGNkZmI2ODc5YTgzODE0YTBmYjk3ZSIsInN1YiI6IjY0YTUyODdmOGM0NGI5MDEwYzljZWUxNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.p-00ldRZZqasbBcq2PxmWFeoTnj9qPF-keOsRaXSTHo"
    }

    response = requests.get(url, headers=headers)
    
    data = response.json()

    return JsonResponse(data)
