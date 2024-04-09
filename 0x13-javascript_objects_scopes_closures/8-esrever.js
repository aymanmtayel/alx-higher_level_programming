#!/usr/bin/node

exports.esrever = function (list) {
  if (list.length === 0) { return []; }

  let i;
  const temp = [];
  for (i = 0; i < list.length; i++) {
    temp[i] = list[list.length - 1 - i];
  }
  return temp;
};
