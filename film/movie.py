import requests

class theMovieDb: 
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
        

    def getPopolars(self):
        response = requests.get(self.api_url)
        return response.Json()

while True : 
    secim = imput("1-Popular Movie\n2-Exit")
    if(secim == 1):
        break
    else:
      movies = movieApi.getPopulers()
      for movie in movies["result"]:
          print(movie)



