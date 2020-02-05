#!/usr/bin/node
// script that prints My numnber:
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
