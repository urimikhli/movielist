# Movies

## Local Setup
### JS App
1. Run `npm install`
2. Run `npm run start`
3. Visit `localhost:3000`. A sample movie detail page can be viewed at `localhost:3000/movie/tt0110357`

### Python API
1. Navigate to the `transformApp` directory: `cd transformApp`
2. Install the necessary python packages: `pip3 install -r requirements.txt`
3. Start up the API: `python3 api.py`

## Routes
There are 2 main routes to the JS app:
1. Root `/`: This should display a list of movies available
2. Movie detail `/movie/${id}`: This displays details of the movie that matches `id`. This component currently pulls sample data from the python API.

## Folders

1. `src` - Contains the react app and all its components
3. `transformApp` - Contains the python API

## Schema

The snippet below is the schema the React App expects the data to be in.

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "Movie",
  "description": "Schema for individual movies",
  "type": "object",
  "properties": {
    "contentType": {
      "enum": [ "movie" ]
    },
    "id": {
      "description": "IMDB ID of the movie",
      "type": "string"
    },
    "movieTitle": {
      "description": "Title of the movie",
      "type": "string"
    },
    "movieYear": {
      "description": "The year the movie was made",
      "type": "string"
    },
    "movieLength": {
      "description": "Length in minutes of the movie",
      "type": "string"
    },
    "moviePlot": {
      "description": "Short description/plot of the movie",
      "type": "string"
    },
    "moviePoster": {
      "description": "Poster image of the movie",
      "type": "string"
    },
  },
  "required": [ "contentType", "id", "movieTitle", "movieYear", "movieLength" ]
}
```