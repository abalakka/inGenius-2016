import urllib2

orderNumber = raw_input("Enter Order Number\n")

url = 'http://localhost/receiveOrderNumber.py?orderNumber=' + orderNumber
response = urllib2.urlopen(url).read()


