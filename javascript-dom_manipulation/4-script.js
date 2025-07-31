const myListElem = document.querySelector('.my_list');
const addItemElem = document.querySelector('#add_item');
addItemElem.addEventListener('click', (e) => {
  const li = document.createElement('li');
  li.appendChild(document.createTextNode('Item'));
  myListElem.appendChild(li);
});
