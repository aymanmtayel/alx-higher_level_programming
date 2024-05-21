#!/usr/bin/node

const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(api, (err, resp, body) => {
  const data = JSON.parse(body);
  if (!err) {
    console.log(data.title);
  } else {
    console.log(err);
  }
});
