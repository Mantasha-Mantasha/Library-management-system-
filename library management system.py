class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.lent_books = {}

    def add_book(self, book_name, quantity=1):
        if book_name in self.books:
            self.books[book_name] += quantity
        else:
            self.books[book_name] = quantity
        print(f"{quantity} copy/copies of '{book_name}' added to the library.")

    def lend_book(self, book_name, user):
        if book_name not in self.books or self.books[book_name] == 0:
            print(f"Sorry, '{book_name}' is not available in the library.")
        elif book_name in self.lent_books and user in self.lent_books[book_name]:
            print(f"'{book_name}' is already lent to {user}.")
        else:
            self.books[book_name] -= 1
            if book_name not in self.lent_books:
                self.lent_books[book_name] = []
            self.lent_books[book_name].append(user)
            print(f"'{book_name}' lent to {user}.")

    def return_book(self, book_name, user):
        if book_name in self.lent_books and user in self.lent_books[book_name]:
            self.lent_books[book_name].remove(user)
            if not self.lent_books[book_name]:
                del self.lent_books[book_name]
            self.books[book_name] += 1
            print(f"'{book_name}' returned by {user}.")
        else:
            print(f"'{book_name}' was not lent to {user}.")

    def display_books(self):
        print(f"Books available in {self.name}:")
        for book, quantity in self.books.items():
            print(f"{book} - {quantity} copy/copies")
        if not self.books:
            print("No books available.")

    def display_lent_books(self):
        print(f"Books currently lent out:")
        for book, users in self.lent_books.items():
            print(f"{book} -> {', '.join(users)}")
        if not self.lent_books:
            print("No books are currently lent out.")


# Example usage
if __name__ == "__main__":
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
