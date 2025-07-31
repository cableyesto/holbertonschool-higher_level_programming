const listMoviesElem = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

/* global fetch */
const response = fetch(url)
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      const message = `An error has occured: ${response.status}`;
      throw new Error(message);
    }
  })
  .then(data => {
    return data.results;
  })
  .catch(error => console.error('There was a problem with the fetch operation:', error));

response.then(movieArray => {
  const movieTitleArray = [];
  movieArray.forEach(movie => {
    movieTitleArray.push(movie.title);
  });
  console.log(movieTitleArray);

  movieTitleArray.forEach(title => {
    const li = document.createElement('li');
    li.appendChild(document.createTextNode(title));
    listMoviesElem.appendChild(li);
  });
});
