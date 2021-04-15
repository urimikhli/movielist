import React, { useEffect, useState } from "react";
import {
  useParams,
  Link
} from "react-router-dom";

const MovieList = () => {
  let { search } = useParams();
  let searchParams = ''
  if (search) searchParams = "?search=" + search
  const protocol = 'http://'
  const apiurl = '127.0.0.1:5000/movie/list'

  const [movieList, setMovieList] = useState({})

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
    </div>;
  } else {

    const localList = JSON.parse(JSON.stringify(movieList));

    return <div>
      <h1>Search results</h1>
      {
        localList.map((movieData, index) => (
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