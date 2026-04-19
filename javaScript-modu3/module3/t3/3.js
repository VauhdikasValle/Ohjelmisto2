'use strict';
const names = ['John', 'Paul', 'Jones'];

const targetElement = document.querySelector('#target');

for (const name of names) {
    const listNames = document.createElement('li');
    listNames.textContent = name;
    targetElement.appendChild(listNames);

}