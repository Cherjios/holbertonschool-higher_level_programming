#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
  return list.reduce((count, elem) => {
    if (elem === searchElement){
      count++;
    }
    return count;
  }, 0);
};
