#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const urlWithInput = 'https://swapi-api.hbtn.io/api/films/' + args[0];

const options = {
  method: 'GET',
  url: urlWithInput
};

try {
  request(options, function (error, response, body) {
    if (!error) {
      let bodyJSON = JSON.parse(body);
      console.log(bodyJSON.title);
    }
  });
} catch (err) {
  console.error('Error in request:', err);
}
