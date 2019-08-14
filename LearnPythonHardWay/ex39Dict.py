# map state to abreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print(states)
# States and cities
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL':  'Jacksonville'
}


# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#cities['CA'] = 'Ipswich'

# print some States
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print list of cities and their states
print(' '*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} is the city {city}")

#both together
print(' ~'*10)
print(list(states.items()))
for state, abbrev in list(states.items()):
    print(f"{state} has city(s) {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there

state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

print('#'*20, 'try again ...')
state ='Texas'

try:
    abbrev =  states.get(state)
    print(f"{state} has city(s) {cities[abbrev]}")
except:
    print(f"The city for the state {state} is: Not Found")
