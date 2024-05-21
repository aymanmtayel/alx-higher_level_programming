#!/usr/bin/node

const request = require('request');

const api = process.argv[2];
let count = 0;

request(api, (err, resp, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const all = data.results;
    for (let i = 0; i < all.length; i++) {
      const allcharacter = all[i].characters;

      for (let j = 0; j < allcharacter.length; j++) {
        const allid = allcharacter[j].split('/')[5];
        if (allid === '18') {
          count += 1;
        }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
