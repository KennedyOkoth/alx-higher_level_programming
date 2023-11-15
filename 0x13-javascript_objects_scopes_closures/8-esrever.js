#!/usr/bin/node

exports.esrever = function (list) {
  let leng = list.length - 1;
  let y = 0;

  while ((leng - y) > 0) {
    const temp = list[leng];
    list[leng] = list[y];
    list[y] = temp;
    y++;
    leng--;
  }
  return list;
};
