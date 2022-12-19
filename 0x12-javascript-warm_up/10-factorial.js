#!/usr/bin/node
const a = parseInt(process.argv[2]);
function factorial (x) {
  if (isNaN(x) || x === 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(factorial(a));
