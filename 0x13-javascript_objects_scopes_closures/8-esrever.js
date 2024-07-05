#!/usr/bin/node

exports.esrever = function (list) {
  let start = list[0];
  let end = list[list.length - 1];

  while (start < end) {
    const temp = list[0];
    list[0] = list[list.length - 1];
    list[list.length - 1] = temp;

    start++;
    end--;
  }
  return list;
};
