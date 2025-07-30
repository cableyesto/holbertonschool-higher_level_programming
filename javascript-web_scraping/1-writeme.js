#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

try {
  const filename = args[0];
  const text = args[1];
  fs.writeFileSync(filename, text, 'utf8');
} catch (err) {
  console.error('Error writing file:', err);
}
