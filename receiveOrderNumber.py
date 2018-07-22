#!/usr/bin/python
import cgi
import cgitb
import urllib2
import urllib
cgitb.enable()

print "Content-Type: text/html"
print ""


form = cgi.FieldStorage()
if "orderNumber" not in form:
    print "<H1>Error</H1>"
    print "Please fill in the Order Number."
   
print "Order Number:", form["orderNumber"].value

string = form["orderNumber"].value + "\n"

f = open('outputON', 'w')
f.write(string)
f.close()

# <form action="demo_form.asp">
# First name: <input type="text" name="FirstName"><br>
# Last name: <input type="text" name="LastName"><br>
# <input type="submit" value="Submit">
# </form>


#json.dumps
