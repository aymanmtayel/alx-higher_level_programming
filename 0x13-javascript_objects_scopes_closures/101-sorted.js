#!/usr/bin/node

const dictold = require('./101-data.js').dict;

console.log(dictold);
const dict1 = {};

for (const key in dictold) {
  const occur = dictold[key];
  if (!dict1[occur]) { dict1[occur] = []; }
  dict1[occur].push(key);
}
console.log(dict1);
