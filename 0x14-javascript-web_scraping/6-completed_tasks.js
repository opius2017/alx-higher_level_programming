#!/usr/bin/node

const axios = require('axios');

const url = process.argv[2];

axios.get(url)
  .then(response => {
    const completed = {};
    const tasks = response.data;
    for (const task of tasks) {
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  })
  .catch(error => {
    console.error(error.message);
  });
