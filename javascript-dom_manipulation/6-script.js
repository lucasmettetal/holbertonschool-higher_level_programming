// Task 6: Star wars character
// Write a JavaScript script that fetches the character name from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
// The name must be displayed in the HTML tag with id character

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('character').textContent = data.name;
    })
    .catch(error => console.error('Error:', error));
