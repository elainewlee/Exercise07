# import scores.txt
# readlines the file
	# creates a list of strings containing each "line" ==> restaurant:rating
	# for each line, separate at colon
	# left = key/restaurant, right = value/rating

# create a dictionary with the above

# alphabetize ?

from sys import argv
from string import *

script, filename = argv

filetext = open(filename).read()	

#listLines = splitlines(filetext)
listLines = filetext.splitlines()

# sorted_list = sorted(listLines)
# print sorted_list
# print listLines

dictrestaurants = {}

for line in listLines:
	temp = line.split(':')
	restaurant = temp[0]
	rating = temp[1]
	dictrestaurants[restaurant] = rating

#response = raw_input("Do you want to sort alphabetically? Type yes or no. > ")

#print listLines



def sort_by_rating(dictrest, switched_list_pair):
	list_pair = dictrest.items() # returns list of tuples in form [(key, value),(key,value),etc]
	# iterates through lists of 2: pair[0] = key, pair[1] = value
	# essentially switches key and value place in each list of tuples and then sticks that tuple onto the new list of pairs
	#print list_pair
	
	for pair in list_pair:
		# make temp variable that sets the tempkey to the pair's value
		tempkey = pair[1]
		# make temp variable that sets the tempvalue to the pair's key
		tempvalue = pair[0]
		# adds the temp values into the new list of tuples
		# APPARENTLY PARENTHESES ARE IMPORTANT HERE!!!!
		switched_list_pair += [(tempkey, tempvalue)]
	switched_list_pair.sort()
	return switched_list_pair

def sort_lowest_highest(dictrestlow, switched_list_low):
	switched_low = sort_by_rating(dictrestlow, switched_list_low)
	for pair in switched_low:
		print "The rating is %s for restaurant %s." % (pair[0], pair[1])
	sort_list_again()

def sort_highest_lowest(dictresthigh, switched_list_high):
	switched_high = sort_by_rating(dictresthigh, switched_list_high)
	reverse_list = switched_high[::-1]
	for pair in reverse_list:
		print "The rating is %s for restaurant %s." % (pair[0], pair[1])
	sort_list_again()

def sort_alpha(dictrest):
	for key in sorted(dictrest.iterkeys()):
		print "The restaurant %s is rated %s." % (key, dictrest[key])
	sort_list_again()

def sort_list_question():
	print "1. By rating (lowest first)"
	print "2. By rating (highest first)"
	print "3. By restaurant name"
	answer = raw_input("> ")
	if answer == '1':
		switched_list = []
		sort_lowest_highest(dictrestaurants, switched_list)
	elif answer == '2':
		switched_list = []
		sort_highest_lowest(dictrestaurants, switched_list)
	elif answer == '3':
		sort_alpha(dictrestaurants)
	elif answer == '42':
		print "Congratulations you've discovered the meaning of life."
	else:
		print "Completely unacceptable. Kindly try that again."
		print "HINT: type '1', '2', or '3'"
		sort_list_question()

def sort_list_again():
	print "Would you like to sort the list again? Yes or No?"
	answer = raw_input("> ")
	if answer.lower() == 'yes':
		sort_list_question()
	elif answer.lower() == 'no':
		print "Goodbye!"
	else:
		print "Sorry, didn't quite catch that. "
		sort_list_again()
		

print "Welcome to Zagat. How would you like to sort your restaurant listings?"
sort_list_question()

# Switching keys/values using lambda

#def sort_lowest_highest(dictrest):
#	for key, value in sorted(dictrest.iteritems(), key = lambda (k,v): (v,k)):
#		print "The rating is %s for restaurant %s." % (value, key)