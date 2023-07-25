#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const result = {};
request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    for (let i = 0; i < body.length; i++) {
      const todo = body[i];
      if (todo.completed === true) {
        if (!result[todo.userId]) {
          result[todo.userId] = 1;
        } else {
          result[todo.userId] += 1;
        }
      }
    }
    console.log(result);
  }
});
