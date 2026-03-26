// Task 5: Change the text
// Write a JavaScript script that updates the text of the header element to "New header!!!"
// when the user clicks on the element with id update_header

document.getElementById('update_header').addEventListener('click', function () {
    document.querySelector('header').textContent = 'New header!!!';
});
