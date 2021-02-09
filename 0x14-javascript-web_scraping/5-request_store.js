#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv;

request(args[2], function(error, response, body) {
    if (error) {
        console.log(error);
    }else{
       fs.writeFile(args[3], body, 'utf-8', err =>{
           if (err) {
               console.log(err)
           }
       })
    }
});
