#!/usr/bin/node
class Square extends Rectangle {
  constructor (w, h, size) {
    super (w, h);
    this.size = size;
  }
}
module.exports = Square;
