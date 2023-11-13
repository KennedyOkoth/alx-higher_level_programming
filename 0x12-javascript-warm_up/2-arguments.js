#!/usr/bin/node

const { argv } = require('node:process');

let value = 0;

argv.forEach((arg, index) => {
  if (index > 0) {
    value++;
  }
});

if (value === 2) {
  console.log('Argument found');
} else if (value > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
