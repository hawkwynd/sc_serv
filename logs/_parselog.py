#!/usr/bin/python
import urllib2
import sys
import json
import requests

print "Hello Scott!"

lineList = [line.rstrip('\n') for line in open('log_ips.log')]
mylist = list(dict.fromkeys(lineList))

# print mylist
# 'a' = append 'w' = overwrite
with open('listeners.log', 'w') as the_file:
    
    for i in mylist:

        hostname = i
        locUrl = "http://ipinfo.io/"+hostname+"/json"

        # print hostname

        try:
            res = urllib2.urlopen(locUrl).read()  
            # print res
            pak = json.loads(res)
            
            if 'region' not in pak or pak['region'] == '':
                pak['region']='Unknown Region'

            if 'city' not in pak or pak['city'] == '':
                pak['city']='Unknown City'

            if 'country' not in pak or pak['country'] == '':
                pak['country']='Uknown Country'

            if 'org' not in pak:
                pak['org'] = 'Unkown Org'   

            print pak['ip'] + "\t" + pak['city'] , pak['region'] +"," + pak['country'] + "\t" + pak['org']
            
            lineTowrite = pak['ip'] + "," + pak['city'] + "," + pak['region'] + "," + pak['country'] + "," + pak['org']

            the_file.write( lineTowrite + '\n')

        except:
        
            print ""

print "listeners.log file created.\n\n"