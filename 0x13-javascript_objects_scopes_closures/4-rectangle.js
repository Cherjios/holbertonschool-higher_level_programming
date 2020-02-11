#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  // Method print()
  print () {
    let res = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        res += 'X';
      }
      console.log(res);
      res = '';
    }
  }

  // Method rotate()
  rotate () {
    const temp = this.widht;
    this.width = this.height;
    this.height = temp;
  }

  // Method double()
  double () {
    this.width *= 2;
    this.heiht *= 2;
  }
}

module.exports = Rectangle;
