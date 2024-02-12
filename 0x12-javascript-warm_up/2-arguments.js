#!/usr/bin/node
const { argv } = require('node:process');
let num = argv.length;
if (num === 2) {
	console.log('No argument');
} else if (num === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
