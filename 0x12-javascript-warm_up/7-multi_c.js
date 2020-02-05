#!/usr/bin/node
// script that prints x times "C is fun"
const num = parseInt(process.argv[2]);
let i;
if (isNaN(num)) {
  console.log('Missing number of occurances');
} else {
  for (i = 0; i <= num; i++) {
    console.log('C is fun');
  }
}
