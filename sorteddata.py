from sys import argv
from string import *

script, filename = argv

filetext = open(filename).read()	

listLines = filetext.splitlines()

dictrestaurants = {}

for line in listLines:
	temp = line.split(':')
	restaurant = temp[0]
	rating = temp[1]
	dictrestaurants[restaurant] = rating

def sort_alpha(dictrest):
	for key in sorted(dictrest.iterkeys()):
		print "The restaurant %s is rated %s." % (key, dictrest[key])
	sort_list_again()
