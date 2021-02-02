#!/usr/bin/node
function fact (a, b) {
  if (a == 1) {
    return b;
  }
  b *= a;
  return fact(--a, b);
}

const myVar = process.argv.slice(2);
const nmr = parseInt(myVar[0], 10);
if (isNaN(nmr)) {
  console.log(1);
} else {
  console.log(fact(nmr, 1));
}
