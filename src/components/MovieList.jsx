import React, { useEffect, useState } from "react";
import {
  useLocation,
  Link
} from "react-router-dom";
import queryString from 'query-string';


const MovieList = (props) => {
  const location = useLocation();
  const params = queryString.parse(location.search)
  let { search } = params
  let searchParams = '';
  if (search) searchParams = "?search=" + search;
  const protocol = 'http://';
  const apiurl = '127.0.0.1:5000/movie/list';

  const [movieList, setMovieList] = useState({});

  useEffect(() => {
    fetch(`${protocol}${apiurl}${searchParams}`)
      .then(res => res.json())
      .then(data => {
        setMovieList(data);
      })
      .catch(err => console.error(err));
  }, [search]);

  if (Object.keys(movieList).length === 0) {
    return <div>

      <h1>Search on Title: coming soon</h1>
      {/* Here is where the search text form would be*/}
    </div>;
  } else {

    return <div>
      <h1>Search results</h1>
      {
        movieList.map((movieData, index) => (
          <div key={index}>
            <div> <Link to={{
              pathname: "/movie/" + movieData.id
            }}
            >{movieData.movieTitle}</Link> {movieData.movieYear}</div>
          </div>
        ))
      }


  </div>
  }
}

export default MovieList;