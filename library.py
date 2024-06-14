# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately (hint: do a membership check to see if the new book is already in the library).

# Existing Library Data:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book():
    while True:
        new_book = (input("What book would you like to add to the library?: "), input("Who is the author?: "))
        if new_book in library:
            print("I'm sorry! That book is already in our library. Please try again.")
            continue
        else: 
            library.append(new_book)
            print(library)
        break
add_book()
