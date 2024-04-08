#!/usr/bin/node

const sorted = process.argv.sort();

if (process.argv.length <= 3) {
  console.log(0);
} else { console.log(sorted.reverse()[1]); }
