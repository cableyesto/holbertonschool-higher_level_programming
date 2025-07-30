#!/usr/bin/node
const fs = require('fs');
let args = process.argv.slice(2);

try {
  const data = fs.readFileSync(args[0], 'utf8');
  console.log(data);
} catch (err) {
  console.error('Error reading file:', err);
}
