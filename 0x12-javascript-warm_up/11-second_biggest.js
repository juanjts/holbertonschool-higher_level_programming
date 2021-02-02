#!/usr/bin/node
let myVar = process.argv.slice(2)
let x = 0, nmr = 0, nmr2 = myVar[0], nmr3 = nmr2;
if (isNaN(nmr2)){
  console.log(0)
} else if (isNaN(myVar[1])){
  console.log(0)
} else {
  while (x < myVar.length){
    nmr = myVar[x]
    if (nmr > nmr2){
      nmr3 = nmr2
      nmr2 = nmr
    }
    x++
  }
  console.log(nmr3)
}
