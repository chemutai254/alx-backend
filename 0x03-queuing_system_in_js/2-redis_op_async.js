import { createClient } from 'redis';
import { promisfy } from 'utils';

function redisConnect() {
  const client = createClient();

  client.on('connect', function() {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

};

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
};

async function displaySchoolValue(schoolName) {
    client.get(schoolName, function(error, result) {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
