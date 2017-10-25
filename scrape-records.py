#!/usr/bin/python

from lxml import html
import requests
import json 

IAAF_URI = 'https://www.iaaf.org/records/by-category/world-records'
TABLE_IDS = ['menoutdoor','womenoutdoor','menindoor','womenindoor']
OUTPUT_FILES = ['data/men-outdoor.json','data/women-outdoor.json','data/men-indoor.json','data/women-indoor.json']
MAX = 4

def getRecordTableElement(table_id):
  page = requests.get(IAAF_URI)
  tree = html.fromstring(page.content)
  table_div  = tree.get_element_by_id(table_id)
  return table_div.getchildren()[0]

def getText(elem):
  if not elem.getchildren():
    return elem.text.encode('utf-8').strip()
  return elem.text_content().encode('utf-8').strip() 

def getTableHeading(table_rows):
  headers = []
  for row in table_rows:
    children = row.getchildren()
    for c in children:
      headers.append(getText(c))
  return headers
  
def getJSONObjects(keys,table_rows,file_obj):
  json_array = []
  for row in table_rows:
    children = row.getchildren()
    i = 0
    obj = {}
    for c in children:
      obj[keys[i]] = getText(c)
      i += 1
    json_array.append(obj)
  return json_array

def writeJSONRecords(file_name, table_id):
  file_obj = open(file_name,"w")
  t = getRecordTableElement(table_id)
  thead = t.getchildren()[0]
  keys = getTableHeading(thead.getchildren())
  tbody = t.getchildren()[1]
  json_array = getJSONObjects(keys,tbody.getchildren(),file_obj)
  file_obj.write(json.dumps(json_array, sort_keys=True, indent=2))

# Main #
i = 0
while i < MAX:
  writeJSONRecords(OUTPUT_FILES[i],TABLE_IDS[i])
  i += 1
