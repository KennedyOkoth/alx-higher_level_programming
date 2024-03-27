#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w === parseInt(w) && h === parseInt(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    const r = "X".repeat(this.width);
    for (let j = 0; j < this.height; ++j) {
      console.log(r);
    }
  }
}

module.exports = Rectangle;
