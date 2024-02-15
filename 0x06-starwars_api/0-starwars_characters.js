#!/usr/bin/node

const request = require('request');
const args = require('process').argv[2]

const url = `https://swapi-api.alx-tools.com/api/films/${args}`;

request(url, function (error, response, body) {
 if (!error) 
  {
  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  
  (async () => {
     for (const value of characters) {
      try {
const name = await fetchName(value);
console.log(name);
}
catch (error) {
   console.error(error);
}
}
})();
 }});


async function fetchName(url_) {
	return new Promise(function (resolve, reject) {
	request(url_, function (error, response, body) {
	if (response) {
	  const person = JSON.parse(body)
	  resolve(person.name)
	  }
	});
});
}
