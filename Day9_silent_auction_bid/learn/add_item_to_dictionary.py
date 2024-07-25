travel_log = [
	{
		'country': 'France',
		'visits': 12,
		"cities": ['Paris', 'Lille', 'Dijon'],
	},
	{
		'country': 'Germany',
		'visits': 5,
		"cities": ['Berlin', 'Hamburg', 'Struttgart'],
	}
]

def add_new_country(country_visited, times_visited, cities_visited ):
	obj = {
		'country': country_visited,
		'visits': times_visited,
		'cities': cities_visited,
	}
	travel_log.append(obj)

	
add_new_country('Russia', 2, ['Moscow, Saint Petursburg'])

print(travel_log)
