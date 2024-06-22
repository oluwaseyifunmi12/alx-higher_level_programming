#!/usr/bin/node

const args = process.argv.slice(2);
const [realArg] = args;

if (realArg) {
  console.log(realArg);
} else {
  console.log('No argument');
}
