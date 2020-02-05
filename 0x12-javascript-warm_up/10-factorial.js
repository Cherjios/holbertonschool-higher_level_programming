#!/usr/bin/node
// script that computes and prints the factorial
const n = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n) || n === 1 | n === 0) return (1);
  else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(n));
