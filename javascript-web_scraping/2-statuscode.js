#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

const options = {
  method: 'GET',
  url: args[0]
};

try {
  request(options, function (error, response, body) {
    if (!error) {
      console.log('code: ', response.statusCode);
    }
  });
} catch (err) {
  console.error('Error in request:', err);
}
