#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(args[2], function (error, response) {
    if(error) {
        console.error('code:', error);
        return;
    }else{
        console.log('code:', response.statusCode);
    }
});
