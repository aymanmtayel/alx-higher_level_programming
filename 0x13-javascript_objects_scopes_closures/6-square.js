#!/usr/bin/node

const old = require('./5-square');

module.exports = class Square extends old {
  charPrint (c) {
    let i;
    if (c === undefined) {
      this.print();
    } else {
      for (i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
    }
  }
};
