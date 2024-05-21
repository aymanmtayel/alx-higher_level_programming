#!/usr/bin/node

const request = require('request');

const api = process.argv[2];

request(api, (err, resp, body) => {
  if (!err) {
    const dictu = {};
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      const id = data[i].userId;
      const completed = data[i].completed;
      if (completed && !dictu[id]) {
        dictu[id] = 0;
      }
      if (completed) ++dictu[id];
    }
    console.log(dictu);
  } else {
    console.log(err);
  }
});
