#!/usr/bin/node

const firstArg = Number(process.argv[2]);
const secArg = Number(process.argv[3]);

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

add(firstArg, secArg);
