




"""
# setting keys_list to list of unsorted restaurants
keys_list = dictrestaurants.keys()
# setting values_list to list of unsorted ratings WITH SAME INDEX as unsorted restaurants
values_list = dictrestaurants.values()

# setting i to how many values there are
i = len(keys_list)
# creates an empty list the size of the list - will be used for adding restaurant names in order sorted by ratings
sorted_restaurant_keys = [''] * i
# creates sorted values list
sorted_rating_values = sorted(values_list)

# iterates through the unsorted list of restaurants
for restaurant in keys_list:
	# finds rating of restaurant by accessing the index of that restaurant in the UNSORTED RESTAURANTS list for future use with the UNSORTED RATINGS list
	rest_rating = values_list[keys_list.index(restaurant)]
	# interates through the sorted values
	for rating in sorted_rating_values:
		# if the sorted rating iteration is the same as the rating of the unsorted restaurant list
		if rest_rating == rating:
			# then go to the spot in the to-be-filled sorted restaurants list using the index of the unsorted rating list, and check if it's filled with a restaurant name or empty
			sorted_restaurant_space = sorted_restaurant_keys[sorted_rating_values.index(rating)]
			# if it's empty
			if sorted_restaurant_space == '':
				# fill that spot in the sorted restaurants list with the restaurant name
				sorted_restaurant_space = restaurant
				# make sure not to set any future places with that rating with the restaruant (avoid duplicates) by breaking
				break
			# if there is already a name there, continue so it searches for the next spot with a matched rating
			else:
				continue
		else:
			continue

sorted_dict = {}
for rating in sorted_rating_values:
	restname = sorted_rating_values.index(rating)
	sorted_dict[restname] = rating
print sorted_dict
"""