#!/usr/bin/python

from lxml import html
import requests

IAAF_URI = 'https://www.iaaf.org/records/by-category/world-records'
TABLE_IDS = ['menoutdoor','womenoutdoor','menindoor','womenindoor']
OUTPUT_FILES = ['data/men-outdoor.csv','data/women-outdoor.csv','data/men-indoor.csv','data/women-indoor.csv']
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

def addTableRowContents(table_rows,file_obj):
  for row in table_rows:
    children = row.getchildren()
    for c in children[:-1]:
       file_obj.write(getText(c) + ", ")
    file_obj.write(getText(children[-1]) + "\n")

def writeRecordCSV(file_name, table_id):
  file_obj = open(file_name,"w")
  t = getRecordTableElement(table_id)
  thead = t.getchildren()[0]
  addTableRowContents(thead.getchildren(),file_obj)
  tbody = t.getchildren()[1]
  addTableRowContents(tbody.getchildren(),file_obj)

# Main #
i = 0
while i < MAX:
  writeRecordCSV(OUTPUT_FILES[i],TABLE_IDS[i])
  i += 1
