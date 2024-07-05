#!/usr/bin/node

const args = process.argv[2];
const myNum = parseInt(args);

if (isNaN(myNum) || myNum === undefined) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
