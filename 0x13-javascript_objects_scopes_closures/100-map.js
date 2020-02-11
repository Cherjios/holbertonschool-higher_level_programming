#!/usr/bin/node
const { list } = require('./100-data.js');

const nlist = list.map((el, index) => el * index);

console.log(list);
console.log(nlist);
