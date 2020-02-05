#!/usr/bin/node
// Function that executes x times a function

exports.callMeMoby = (n, func)=> {
  for(let i = 0; i < n; i++) {
    func();
  }
};
