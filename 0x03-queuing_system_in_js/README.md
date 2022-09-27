# 0x03. Queuing System in JS
---

## Learning Objectives
- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue
---

## Install Redis on Linux
- Install lbs release first using command: sudo apt install lsb-release
- Add repository to apt index with the commands:
	curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

	echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

	sudo apt-get update
	sudo apt-get install redis
---

## Compile Redis to the latest version
- $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
- $ tar xzf redis-6.0.10.tar.gz
- $ cd redis-6.0.10
- $ make
---

## Start Redis in the background with src/redis-server
- Outputs: $ src/redis-server &
---

## Make sure that the server is working with a ping src/redis-cli ping
- Outputs: PONG
---

## Using the Redis client again, set the value School for the key Holberton
- Outputs:
- 127.0.0.1:[Port]> set Holberton School
- OK
- 127.0.0.1:[Port]> get Holberton
- "School"
---

## Kill the server with the process id of the redis-server (hint: use ps and grep)
- ps aux | grep redis-server : $ kill [PID_OF_Redis_Server]$ kill [PID_OF_Redis_Server]
- or
- ps -ef | grep -i 'redis-server' : kill -9 PID owned by redis
---


