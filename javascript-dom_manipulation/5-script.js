const headerElem = document.querySelector('header');
const updateHeaderElem = document.querySelector('#update_header');
updateHeaderElem.addEventListener('click', (e) => {
  headerElem.textContent = 'New Header!!!';
});
