#!/usr/bin/node

const file = require('fs');
const file1 = file.readFileSync(process.argv[2]);
const file2 = file.readFileSync(process.argv[3]);
file.writeFileSync(process.argv[4], file1 + file2);
