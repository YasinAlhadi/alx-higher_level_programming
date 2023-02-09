#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        if (tasks[i].userId in completedTasks) {
          completedTasks[tasks[i].userId]++;
        } else {
          completedTasks[tasks[i].userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
