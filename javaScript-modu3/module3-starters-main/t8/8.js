const input1 = document.querySelector('#num1');
const input2 = document.querySelector('#num2');

const operation = document.querySelector('#operation');
const calculateButton = document.querySelector('#start');
const resultArea = document.querySelector('#result');

calculateButton.addEventListener('click', function() {
    const val1 = Number(input1.value);
    const val2 = Number(input2.value);

    let result;
 if (operation.value === 'add') {
        result = val1 + val2;
    } else if (operation.value === 'sub') {
        result = val1 - val2;
    } else if (operation.value === 'mul') {
        result = val1 * val2;
    } else if (operation.value === 'div') {
        result = val1 / val2;
    }

    resultArea.textContent = result;
});