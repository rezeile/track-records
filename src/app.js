const express = require('express')
const fs = require('fs')
const queryString = require('query-string')


// API Key: AIzaSyDLdRthKBLV8onmtltCvu9-aB96Y-iFsSc
const apiKey = "AIzaSyDLdRthKBLV8onmtltCvu9-aB96Y-iFsSc"
const app = express()

const baseUri = 'https://www.googleapis.com/youtube/v3/search?';

function getSearchResults(part,max,query,key) {
  var params = {
    "part": part,
    "maxResults": max,
    "q": query,
    "key": key,
  }
  return baseUri + queryString.stringify(params)
}

/* Default Route */
app.get('/', function (req, res) {
  var link = getSearchResults("snippet",10,"Usain Bolt",apiKey)
  var source = '<a src=\"' + link + '\">' + 'link' + '</a>'
  res.send(link)
})

app.get('/hi', function (req, res) {
  res.send('Hi People Whats Up');
})

app.listen(3000);
