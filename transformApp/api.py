import logging
import requests
import json
import flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
apikey = 'da0a1687'
omdbapi_host = 'www.omdbapi.com/'
protocol = 'http://'

sampleMovieDetail = {
  "id": "tt0110357",
  "movieTitle": "The Lion King",
  "movieYear": "1994",
  "movieLength": "88 min",
  "moviePlot": "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.",
  "moviePoster": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SX300.jpg",
  "contentType": "movie"
}

sampleMovieList = [
    {
        "id": "tt0110357",
        "movieTitle": "The Lion King",
        "movieYear": "1994",
        "movieLength": "88 min",
        "moviePlot": "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.",
        "moviePoster": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SX300.jpg",
        "contentType": "movie"
    },
    {
        "id": "tt3896198",
        "movieTitle": "Guardians of the Galaxy Vol. 2",
        "movieYear": "2017",
        "movieLength": "136 min",
        "moviePlot": "The Guardians struggle to keep together as a team while dealing with their personal family issues, notably Star-Lord's encounter with his father the ambitious celestial being Ego.",
        "moviePoster": "https://m.media-amazon.com/images/M/MV5BNjM0NTc0NzItM2FlYS00YzEwLWE0YmUtNTA2ZWIzODc2OTgxXkEyXkFqcGdeQXVyNTgwNzIyNzg@._V1_SX300.jpg",
        "contentType": "movie",
    }
]


@app.route('/movie/list', methods=['GET'])
@cross_origin()
def movie_list():
    params = request.args #.get('username')
    print(params)
    for movie in sampleMovieList:
      jsonify(movie)
    
    print(sampleMovieList)
    return jsonify(sampleMovieList)

@app.route('/movie/detail/<string:movie_id>', methods=['GET'])
@cross_origin()
def movie_detail(movie_id):
    #sample usage: http://www.omdbapi.com/?i=tt3896198&apikey=da0a1687
    request = '{}{}?i={}&apikey={}'.format(protocol,omdbapi_host,movie_id,apikey)
    response = requests.get(request)

    if response.status_code == 200:
      print("running mapper")
      movieDetail = movie_mapper(response.json())
    else:
      print("running Sample")
      movieDetail = sampleMovieDetail

    return jsonify(movieDetail)

def movie_mapper(responseData):
  return {
    "id": responseData['imdbID'],
    "movieTitle": responseData['Title'],
    "movieYear": responseData['Year'],
    "movieLength": responseData['Runtime'],
    "moviePlot": responseData['Plot'],
    "moviePoster": responseData['Poster'],
    "contentType": responseData['Type']
  }

app.run()
