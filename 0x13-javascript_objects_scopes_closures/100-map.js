#!/usr/bin/node
const list = require('./100-data').list;
let nlist = [];
nlist = list.map(function (n, i) {
  return n * i;
});
console.log(list);
console.log(nlist);
