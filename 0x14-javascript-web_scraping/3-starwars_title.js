#!/usr/bin/node

const id = process.argv[2];
const myUrl = 'http://swapi.co/api/films/' + id;
const request = require('request');
request.get(myUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body).title;
  console.log(movie);
});
