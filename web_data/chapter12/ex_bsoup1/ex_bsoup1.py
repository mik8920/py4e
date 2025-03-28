from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#The program will use urllib to read the HTML from the data files
#parse the data
#extracting numbers
#compute the sum of the numbers in the file
#Sample data - sum=2553, actual data - sum ends with 5

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE





