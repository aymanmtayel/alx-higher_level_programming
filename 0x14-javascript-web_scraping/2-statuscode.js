#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, data) {
    console.log('code', data.statusCode);
});
