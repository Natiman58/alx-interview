const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi.co/api/films/';

// Make a GET request to the Star Wars API to retrieve information about the movie
request(baseUrl + movieId, (error, response, body) => {
  if (error) {
    console.error(`Error fetching movie: ${error}`);
    return;
  }

  // Parse the response body as a JSON object
  const movie = JSON.parse(body);

  // Extract the list of character URLs from the movie object
  const characters = movie.characters;

  // Loop through each character URL and make a request to retrieve information about each character
  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error fetching character ${index}: ${error}`);
        return;
      }

      // Parse the response body as a JSON object
      const character = JSON.parse(body);

      // Display the name of the character
      console.log(character.name);
    });
  });
});
