const characterElem = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

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
    return data;
  })
  .catch(error => console.error('There was a problem with the fetch operation:', error));

response.then(data => {
  characterElem.appendChild(document.createTextNode(data.name));
});
