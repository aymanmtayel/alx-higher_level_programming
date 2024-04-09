#!/usr/bin/node

exports.logMe = function (item) {
  if (!this.i) { this.i = 0; }
  console.log(this.i + ': ' + item);
  this.i++;
};
