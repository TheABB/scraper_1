# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
import scraperwiki
import lxml.html
#change url to scrape different page
html = scraperwiki.scrape("http://www.parliament.uk/mps-lords-and-offices/mps/?search_term=wales")
#print html
#remember html above is only a descriptive label, and 'html' has no instrinsic meaning in the line above
# next line imports the lxml.html library 
# use the .fromstrong function to turn html into a lxml 'object', a variable called 'root'
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
# next line looks for anything in an <a href= ...> tag and puts in a list called 'tds'
tds = root.cssselect("a") #key tag!!
# note that 'cell' is just an arbitrary label
indexno = 0
for td in tds:
  indexno = indexno + 1
  record = {"td":td.text, "index" : indexno}
  scraperwiki.sqlite.save(["index"], record)
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
