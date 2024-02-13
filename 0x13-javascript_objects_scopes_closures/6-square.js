#!/usr/bin/node;
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    c = c || 'X';
    const r = c.repeat(super.size);
    for (let j = 0; j < super.size; ++j) {
      console.log(r)
    }
  }
}
module.exports = Square;
