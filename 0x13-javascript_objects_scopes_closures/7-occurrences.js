#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i; let j = 0;
  for (i = 0; i < list.length; i++) { if (list[i] === searchElement) { j += 1; } }
  return j;
};
