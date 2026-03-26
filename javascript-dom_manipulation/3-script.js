// Task 3: Toggle classes
// Write a JavaScript script that toggles the class of the header element
// when the user clicks on the tag with id toggle_header
// The header element must always have one class: red or green (never both, never empty)
// If the current class is red, when the user click on toggle_header, it becomes green
// If the current class is green, when the user click on toggle_header, it becomes red

document.getElementById('toggle_header').addEventListener('click', function () {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});
