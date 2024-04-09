#!/usr/bin/node

const list = process.argv.slice(2).map(Number);

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const sorted = list.sort();
  console.log(sorted.reverse()[1]);
}
