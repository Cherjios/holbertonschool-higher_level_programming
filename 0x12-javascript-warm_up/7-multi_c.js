#!/usr/bin/node
// script that prints x times "C is fun"
const x = parseInt(process.argv[2]);
let i;
if (isNaN(x)) {
  console.log('Missing number of occurances');
} else {
  for (i = 1; i <= x; i++) {
    console.log('C is fun');
  }
}
