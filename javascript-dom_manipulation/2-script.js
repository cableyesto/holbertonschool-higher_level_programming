const headerElem = document.querySelector('header');
const redHeaderElem = document.querySelector('#red_header');
redHeaderElem.addEventListener('click', (e) => {
  headerElem.classList.add('red');
});
