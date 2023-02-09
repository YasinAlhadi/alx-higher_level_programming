#!/usr/bin/node

const fs = require('fs').promises;
const file = process.argv[2];

async function readFile (file) {
  try {
    const data = await fs.readFile(file, 'utf8');
    console.log(data);
  } catch (err) {
    console.log(err);
  }
}
readFile(file);
