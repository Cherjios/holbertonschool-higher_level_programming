#!/usr/bin/node
// script that prints x times a square
const x = parseInt(process.argv[2]);
let i, j, res;
res = '';
if (isNaN(x)) {
  console.log('Missing number of occurances');
} else {
  for (i = 1; i <= x; i++) {
    for (j = 1; j <= x; j++) {
      res += 'X';
    }
    console.log(res);
    res = '';
  }
}
