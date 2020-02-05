#!/usr/bin/node
// script that prints the addition of 2 integers
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
function add () {
  return (num1 + num2);
}
if (isNaN(num1)) {
  console.log('NaN');
} else {
  console.log(add());
}
