#!/usr/bin/node

const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(api, (err, resp, data) => {
  if (!err) {
    const procc = JSON.parse(data).characters;
    for (let i = 0; i < procc.length; ++i) {
      request(procc[i], (err2, resp2, data2) => {
        const names = JSON.parse(data2).name;
        console.log(names);
      });
    }
  }
});
