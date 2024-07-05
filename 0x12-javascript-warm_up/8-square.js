#!/usr/bin/node

const args = process.argv[2];
const myNum = parseInt(args);

if (isNaN(myNum) || myNum === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('X'.repeat(myNum));
  }
}
