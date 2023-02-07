#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

const baseUrl = `https://swapi.dev/api/films/${filmId}/`;

request(baseUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
