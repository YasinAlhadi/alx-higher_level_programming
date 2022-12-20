#!/usr/bin/node
const SquareC = require('./5-square.js');
class Square extends SquareC {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let ro, co;
    for (ro = 0; ro < this.height; ro++) {
      let str = '';
      for (co = 0; co < this.width; co++) {
        str += c;
      }
      console.log(str);
    }
  }
}
module.exports = Square;
