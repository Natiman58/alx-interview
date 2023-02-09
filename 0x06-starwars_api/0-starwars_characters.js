#!/usr/bin/node

// A script that prints all characters of a Star Wars movie

const request = require('request');
const args = process.argv[2];
const movieId = `https://swapi-api.alx-tools.com/api/films/${args}`;

request(movieId, function (error, response, body) {
  if (!error) {
    // parse the response body as a JSON object
    const movie = JSON.parse(body);

    // extract the list of chars from the movie object
    const characters = movie.characters;
    printChar(characters, 0);
  }
});

function printChar (url, index) {
  const eachCharurl = url[index];
  request(eachCharurl, function (error, response, body) {
    if (!error) {
      // print the all the names from the response body
      console.log(JSON.parse(body).name);
      // if the next index is less than the last character
      if (index + 1 < url.length) {
        // printthe next name
        printChar(url, index + 1);
      }
    }
  });
}
