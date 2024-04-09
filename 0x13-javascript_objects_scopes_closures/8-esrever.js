#!/usr/bin/node

exports.esrever = function (list) {
  let i; const temp = [0];
  for (i = 0; i < list.length; i++) {
    temp[i] = list[list.length - 1 - i];
  }
  return temp;
};
