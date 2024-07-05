#!/usr/bin/node

const arg = Number(process.argv[2]);

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return (1);
  } else if (n < 0) {
    return (-1);
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(arg));
