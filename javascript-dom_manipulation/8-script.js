// Task 8: Say Hello!
// Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.com/?lang=fr
// and displays the value of hello from that fetch in the HTML element with id hello

fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
        document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => console.error('Error:', error));
