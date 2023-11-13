#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
}

for (let i = 1; i <= parseInt(process.argv[2]); i++) {
  let row = '';
  for (let y = 1; y <= parseInt(process.argv[2]); y++) {
    row += 'X';
  }
  console.log(row);
}
