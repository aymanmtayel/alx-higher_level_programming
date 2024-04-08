#!/usr/bin/node

let i = 0;
let j = 0;

while (process.argv[i + 2] !== undefined) { i++; }
if (i === 0) { console.log('No argument'); }
if (i > 0) { for (j = 2; j < i + 2; j++) { console.log(process.argv[j]); } }
