const headerElem = document.querySelector('header');
const toggleElem = document.querySelector('#toggle_header');
toggleElem.addEventListener('click', (e) => {
  if (headerElem.classList.contains('red')) {
    headerElem.classList.remove('red');
    headerElem.classList.add('green');
  } else {
    headerElem.classList.remove('green');
    headerElem.classList.add('red');
  }
});
