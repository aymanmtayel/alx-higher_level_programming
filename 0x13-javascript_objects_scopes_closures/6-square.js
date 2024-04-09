#!/usr/bin/node

const old = require('./5-square');

module.exports = class Square extends old {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let i;
    if (c === undefined) {
      this.print();
    } else {
      for (i = 0; i < this.size; i++) { console.log(c.repeat(this.size)); }
    }
  }
};
