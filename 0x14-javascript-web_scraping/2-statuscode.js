#!/usr/bin/node

const myUrl = process.argv[2];
const request = require('request');
request(myUrl, function (error, response) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code: ' + response.statusCode);
});
