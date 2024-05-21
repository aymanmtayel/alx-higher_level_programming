#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, resp, data) => {
  if (data) {
    fs.writeFile(process.argv[3], data, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(err);
  }
});
