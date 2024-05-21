#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, data) {
  if (!err) {
    console.log('code:', data.statusCode);
  } else {
    console.log(err);
  }
});
