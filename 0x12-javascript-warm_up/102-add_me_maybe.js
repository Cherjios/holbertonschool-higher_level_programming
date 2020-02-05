#!/usr/bin/node
// Function that executes x times a function

exports.addMeMaybe = (n, func) => {
  func(n + 1);
};
