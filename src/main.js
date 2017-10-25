const express = require('express')
const app = express()
const parse = require('csv-parse')
const fs = require('fs')

function parseValues() {
  var parser = parse({delimiter: ":"}, function(err, data) {
    console.log(err);
    console.log(data);
  });
  fs.createReadStream("../data/men-outdoor.csv");
}


app.get('/', function (req, res) {
  parseValues()
  res.send('Hello World!')
})

app.listen(3000, function () {
  console.log('Example app')
})
