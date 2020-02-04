#!/usr/bin/node
// script that prints Arguments:
const Arguments = process.argv.length;
const myVar1 = 'No argument';
const myVar2 = 'Argument found';
const myVar3 = 'Arguments found';
if (Arguments === 2) console.log(myVar1);
if (Arguments === 3) console.log(myVar2);
if (Arguments > 3) console.log(myVar3);
