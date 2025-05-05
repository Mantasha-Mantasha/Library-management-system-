# Library Management System

This is a simple Python implementation of a Library Management System. It allows users to manage a library's collection of books, lend books to users, and track which books are currently lent out. The system also includes features for returning books and displaying the library's inventory.

## Features

1. **Add Books**: Add books to the library with a specified quantity.
2. **Lend Books**: Lend books to users and track which users have borrowed which books.
3. **Return Books**: Return books to the library and update the inventory.
4. **Display Books**: Display the current inventory of books in the library.
5. **Display Lent Books**: Display a list of books that are currently lent out and the users who have borrowed them.

## Code Overview

The program is built around the `Library` class, which contains the following methods:

- **`__init__(self, name)`**: Initializes the library with a name, an empty dictionary for available books (`books`), and an empty dictionary for lent books (`lent_books`).

- **`add_book(self, book_name, quantity=1)`**: Adds a specified quantity of a book to the library's inventory.

- **`lend_book(self, book_name, user)`**: Lends a book to a user, updating the inventory and tracking lent books.

- **`return_book(self, book_name, user)`**: Handles the return of a book from a user, updating the inventory and tracking.

- **`display_books(self)`**: Displays the library's current inventory of books.

- **`display_lent_books(self)`**: Displays a list of books currently lent out and their respective borrowers.

## Example Usage

The following is an example of how to use the `Library` class:

```python
# Creating a library instance
library = Library("City Library")

# Adding books
library.add_book("Harry Potter", 3)
library.add_book("The Hobbit", 2)

# Displaying books
library.display_books()

# Lending books
library.lend_book("Harry Potter", "Alice")
library.lend_book("The Hobbit", "Bob")

# Displaying lent books
library.display_lent_books()

# Returning books
library.return_book("Harry Potter", "Alice")

# Displaying books and lent books after returning
library.display_books()
library.display_lent_books()
```

## Output

The program provides output to the console for every operation, such as adding books, lending books, returning books, and displaying the library's inventory and lent books. Below is an example of the output:

```
3 copy/copies of 'Harry Potter' added to the library.
2 copy/copies of 'The Hobbit' added to the library.
Books available in City Library:
Harry Potter - 3 copy/copies
The Hobbit - 2 copy/copies
'Harry Potter' lent to Alice.
'The Hobbit' lent to Bob.
Books currently lent out:
Harry Potter -> Alice
The Hobbit -> Bob
'Harry Potter' returned by Alice.
Books available in City Library:
Harry Potter - 3 copy/copies
The Hobbit - 1 copy/copies
Books currently lent out:
The Hobbit -> Bob
```

## How to Run

1. Clone the repository to your local machine.
2. Ensure you have Python 3 installed.
3. Run the script using the following command:

   ```bash
   python library_management.py
   ```

Modify the script as needed to suit your specific use case.

## License

This code is provided under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## Author

This Library Management System was implemented by **Mantasha-Mantasha**.
