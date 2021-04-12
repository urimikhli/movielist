import React, { useEffect, useState } from "react";
import {
  useParams
} from "react-router-dom";

const MovieDetail = () => {
  const { id } = useParams();
  const [movieData, setMovieData] = useState({});

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/movie/detail/${id}`)
      .then(res => res.json())
      .then(data => {
        setMovieData(data);
      })
      .catch(err => console.error(err));
  }, [id]);
  
  const {
    movieTitle,
    moviePoster,
    movieYear,
    moviePlot,
  } = movieData;

  if (!movieTitle) return <div>Loading...</div>;

  return <div>
      <h1>{`${movieTitle} (${movieYear})`}</h1>
      <img src={moviePoster} alt={movieTitle} />
      <p>{moviePlot}</p>
    </div>
}

export default MovieDetail;