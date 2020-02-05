#!/usr/bin/node
// script that prints Arguments:
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
