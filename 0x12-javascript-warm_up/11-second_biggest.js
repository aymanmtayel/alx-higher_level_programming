#!/usr/bin/node

const list = process.argv.slice(2, process.argv.length).map(Number)

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const sorted = list.sort((a, b)=> a - b);
  console.log(sorted[sorted.length - 2]);
}
