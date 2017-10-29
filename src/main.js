const express = require('express')
const app = express()
const fs = require('fs')

// API Key: AIzaSyDLdRthKBLV8onmtltCvu9-aB96Y-iFsSc


app.get('/', function (req, res) {
  res.send('Hello World!');
})

app.get('/hi', function (req, res) {
  res.send('Hi People Whats Up'); 
})

app.listen(3000);
