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
      const bodyJSON = JSON.parse(body);
      const results = bodyJSON.results;

      const filteredResults = results.filter(movie => {
        const subStr = '18';
        const subArr = movie.characters.filter(str => str.includes(subStr));
        return subArr.length > 0;
      });
      console.log(filteredResults.length);
    }
  });
} catch (err) {
  console.error('Error in request:', err);
}
