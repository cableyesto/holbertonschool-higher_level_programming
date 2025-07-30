#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);

const options = {
  method: 'GET',
  url: args[0]
};

try {
  request(options, function (error, response, body) {
    if (!error) {
      const bodyJSON = JSON.parse(body);

      const filteredStudents = bodyJSON.filter(student => {
        return student.completed === true;
      });

      // generate the objet with key that match the students
      let allUserId = [];
      filteredStudents.forEach(student => {
        allUserId.push(student.userId);
      });
      const uniqueAllUserId = allUserId.filter((value, index, array) => array.indexOf(value) === index);
      let objCount = {};
      for (let i = 0; i < uniqueAllUserId.length; i++) {
        // reduce by each student id, to count the completed tasks
        const studentCompletedTasks = filteredStudents.filter(student => student.userId === uniqueAllUserId[i]);
        const countCompletedTasks = studentCompletedTasks.length;

        // generate the object
        objCount[uniqueAllUserId[i]] = countCompletedTasks;
      }
      console.log(objCount);
    }
  });
} catch (err) {
  console.error('Error in request:', err);
}
