#!/usr/bin/node

const myVar1 = process.argv[2];
const myVar2 = process.argv[3];
const myVar3 = 'undefined';

if (myVar1 === undefined) {
  console.log(myVar3 + ' is ' + myVar3);
} else if (myVar2 === undefined) {
  console.log(myVar1 + ' is ' + myVar3);
} else {
  console.log(myVar1 + ' is ' + myVar2);
}
