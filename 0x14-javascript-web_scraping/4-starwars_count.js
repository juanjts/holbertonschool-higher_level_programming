#!/usr/bin/node

const request = require('request');
const args = process.argv;
let count = 0;

request(args[2], function(error, response, body) {
    if (error) {
        console.log(error);
    }else{
        const films = JSON.parse(body).results;
        for (let i in films){
            for (let x in films[i].characters){
                if (films[i].characters[x].includes('/18/')) {
                    count = count + 1;
                }
            }
        }
    }
    return console.log(count);
});
