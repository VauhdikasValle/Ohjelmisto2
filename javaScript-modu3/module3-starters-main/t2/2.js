const targetElement = document.querySelector('#target');

const item1 = document.createElement('li');
item1.textContent = 'First item';
targetElement.appendChild(item1);

const item2 = document.createElement('li');
item2.textContent = 'Second item';
item2.classList.add('my-item');
targetElement.appendChild(item2);

const item3 = document.createElement('li');
item3.textContent = 'Third item';
targetElement.appendChild(item3);
