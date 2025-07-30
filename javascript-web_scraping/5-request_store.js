#!/usr/bin/node
// Url used, https://lorem-api.com/api/lorem?paragraphs=5
const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);
const urlAPI = args[0];
const filename = args[1];

const options = {
  method: 'GET',
  url: urlAPI
};

try {
  request(options, function (error, response, body) {
    if (!error) {
      fs.writeFileSync(filename, body, 'utf8');
    }
  });
} catch (err) {
  console.error('Error in request:', err);
}
