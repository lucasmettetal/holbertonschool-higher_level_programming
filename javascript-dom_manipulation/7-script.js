// Task 7: Star Wars movies
// Write a JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// All movie titles must be list in the HTML ul element with id list_movies

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const listMovies = document.getElementById('list_movies');
        data.results.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            listMovies.appendChild(li);
        });
    })
    .catch(error => console.error('Error:', error));
