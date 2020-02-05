#!/usr/bin/node
// script that searchs the second biggest integer
if (process.argv.length < 4) {
  console.log(0);
} else {
  const arrNums = process.argv.slice(2).sort((a, b) => a - b);
  console.log(arrNums[arrNums.length - 2]);
}
