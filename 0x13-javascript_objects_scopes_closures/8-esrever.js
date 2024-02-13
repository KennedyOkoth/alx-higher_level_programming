#!/usr/bin/node;

exports.esrever = function (list) {
  let reversedList = list.slice();

  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    let temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }

  return reversedList;
};
