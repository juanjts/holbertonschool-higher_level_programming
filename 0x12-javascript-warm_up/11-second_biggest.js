#!/usr/bin/node
const myVar = process.argv.slice(2);
let x = 0; let nmr = 0; let nmr2 = myVar[0]; let nmr3 = nmr2;
if (isNaN(nmr2)) {
  console.log(0);
} else if (isNaN(myVar[1])) {
  console.log(0);
} else {
  while (x < myVar.length) {
    nmr = myVar[x];
    if (nmr > nmr2) {
      nmr3 = nmr2;
      nmr2 = nmr;
    }
    x++;
  }
  console.log(nmr3);
}
