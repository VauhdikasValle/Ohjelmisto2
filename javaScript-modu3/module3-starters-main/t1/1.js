const targetElement = document.querySelector('#target');

targetElement.innerHTML = `
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
`;

targetElement.classList.add('my-list');