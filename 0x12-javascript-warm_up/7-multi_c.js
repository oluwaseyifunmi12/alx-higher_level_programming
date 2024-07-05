#!/usr/bin/node

const args = process.argv[2];
const myNum = parseInt(args);

if (isNaN(myNum) || myNum === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
