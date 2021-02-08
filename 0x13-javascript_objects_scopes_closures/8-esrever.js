#!/usr/bin/node
exports.esrever = function (list) {
  let x = 0;
  const reverse = [];
  for (let i = list.length; i > 0; i--) {
    reverse[x] = list[i - 1];
    x++;
  }
  return reverse;
};
