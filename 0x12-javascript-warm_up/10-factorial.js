#!/usr/bin/node

function fact (a) {
  if (isNaN(a) || a === 0) { return 1; }
  return (a * fact(a - 1));
}

const a = parseInt(process.argv[2]);
console.log(fact(a));
