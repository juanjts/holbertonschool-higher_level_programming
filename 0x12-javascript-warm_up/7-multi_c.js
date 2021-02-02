#!/usr/bin/node
if (process.argv.length === 2) {
    console.log('Missing number of occurrences');
  } else {
    for (let myVar = 0; myVar < process.argv[2]; myVar++) {
      console.log('C is fun');
    }
  }
