#!/usr/bin/node
// script that computes and prints a factorial
function factorial (fac) {
  const nmr = Number(fac);
  if (isNaN(nmr) === true | nmr === 1) {
    return 1;
  }
  return nmr * factorial(nmr - 1);
}
console.log(factorial(process.argv[2]));
