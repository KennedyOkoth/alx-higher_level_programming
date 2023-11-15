#!/usr/bin/node

const SquareT = require('./5-square');

class Square extends SquareT {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let rows = '';
      for (let y = 0; y < this.width; y++) {
        rows += c;
      }
      console.log(rows);
    }
  }
}

module.exports = Square;
