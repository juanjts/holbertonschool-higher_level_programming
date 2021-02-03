#!/usr/bin/node
const nmr = process.argv.slice(2);
if (process.argv.length <= 3) {
  console.log('0');
} else {
  nmr.sort((a, b) => a - b);
  console.log(nmr[nmr.length - 2]);
}
