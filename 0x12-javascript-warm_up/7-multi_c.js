#!/usr/bin/node

const occur = parseInt(process.argv[2]);
let i;
if (isNaN(occur)) {
  console.log('Missing number of occurrences');
} else { for (i = 0; i < occur; i++) { console.log('C is fun'); } }
