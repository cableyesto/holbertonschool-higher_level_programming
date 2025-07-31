
document.addEventListener('DOMContentLoaded', () => {
  const helloElem = document.querySelector('#hello');
  const url = 'https://hellosalut.stefanbohacek.com/?cc=fr';

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
      return data.hello;
    })
    .catch(error => console.error('There was a problem with the fetch operation:', error));

  response.then(helloMessage => {
    helloElem.appendChild(document.createTextNode(helloMessage));
  });
});
