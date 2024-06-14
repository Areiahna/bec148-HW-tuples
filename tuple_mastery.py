# Objective: The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:

"Itinerary 1: Alice - From New York to London"
"Itinerary 2: Bob - From Tokyo to San Francisco"
flights = (("Alice","New York","London"),("Bob","Tokyo","San Francisco"))
# ({"01":{"Passenger": "Alice", "From" : "New York", "To":"London"}},{"02":{"Passenger": "Bob", "From" : "Tokyo", "To":"San Francisco"}})
# print(flights)

def main(atuple):
    for itin, passenger in enumerate(atuple):
        print (f'''
            Itinerary {itin + 1}: {passenger[0]} - From {passenger[1]} to {passenger[2]}
        ''')

main(flights)

