#!/usr/bin/node

const old = require('./100-data.js').list;
console.log(old);
console.log(old.map((number, i) => number * i));
