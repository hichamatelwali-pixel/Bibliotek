class Item:
    """Base class for items in the library system."""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_info(self):
        """Display basic information. To be overridden by subclasses."""
        print(f"ID: {self.id}, Name: {self.name}")


class Book(Item):
    """Represents a book in the library."""
    def __init__(self, book_id, title, author, copies):
        super().__init__(book_id, title)
        self.author = author
        self.copies = copies

    def display_info(self):
        """Display book information."""
        print(f"ID: {self.id}, Title: {self.name}, Author: {self.author}, Copies: {self.copies}")


class DVD(Item):
    """Represents a DVD in the library."""
    def __init__(self, dvd_id, title, director, duration):
        super().__init__(dvd_id, title)
        self.director = director
        self.duration = duration

    def display_info(self):
        """Display DVD information."""
        print(f"ID: {self.id}, Title: {self.name}, Director: {self.director}, Duration: {self.duration} min")


class Member(Item):
    """Represents a member of the library."""
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.borrowed_books = []

    def display_info(self):
        """Display member information."""
        borrowed_titles = [book.name for book in self.borrowed_books]
        print(f"ID: {self.id}, Name: {self.name}, Borrowed Books: {borrowed_titles}")

    def borrow_book(self, book):
        """Borrow a book if copies are available."""
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.name}'")
        else:
            print(f"No copies available for '{book.name}'")

    def return_book(self, book):
        """Return a borrowed book."""
        if book in self.borrowed_books:
            book.copies += 1
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.name}'")
        else:
            print(f"'{book.name}' was not borrowed by {self.name}")


class Library:
    """Manages books, DVDs, and members."""
    def __init__(self):
        self.books = {}  # book_id: Book
        self.dvds = {}   # dvd_id: DVD
        self.members = {}  # member_id: Member

    def add_book(self, book):
        """Add a book to the library."""
        self.books[book.id] = book

    def remove_book(self, book_id):
        """Remove a book by ID."""
        if book_id in self.books:
            del self.books[book_id]
        else:
            print(f"Book with ID {book_id} not found")

    def update_book(self, book_id, title=None, author=None, copies=None):
        """Update book details."""
        if book_id in self.books:
            book = self.books[book_id]
            if title is not None:
                book.title = title
            if author is not None:
                book.author = author
            if copies is not None:
                book.copies = copies
        else:
            print(f"Book with ID {book_id} not found")

    def add_dvd(self, dvd):
        """Add a DVD to the library."""
        self.dvds[dvd.id] = dvd

    def remove_dvd(self, dvd_id):
        """Remove a DVD by ID."""
        if dvd_id in self.dvds:
            del self.dvds[dvd_id]
        else:
            print(f"DVD with ID {dvd_id} not found")

    def update_dvd(self, dvd_id, title=None, director=None, duration=None):
        """Update DVD details."""
        if dvd_id in self.dvds:
            dvd = self.dvds[dvd_id]
            if title is not None:
                dvd.title = title
            if director is not None:
                dvd.director = director
            if duration is not None:
                dvd.duration = duration
        else:
            print(f"DVD with ID {dvd_id} not found")

    def add_member(self, member):
        """Add a member to the library."""
        self.members[member.id] = member

    def remove_member(self, member_id):
        """Remove a member by ID."""
        if member_id in self.members:
            del self.members[member_id]
        else:
            print(f"Member with ID {member_id} not found")

    def update_member(self, member_id, name=None):
        """Update member details."""
        if member_id in self.members:
            member = self.members[member_id]
            if name is not None:
                member.name = name
        else:
            print(f"Member with ID {member_id} not found")

    def issue_book(self, member_id, book_id):
        """Issue a book to a member."""
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.borrow_book(book)
        else:
            print("Member or book not found")

    def return_book(self, member_id, book_id):
        """Return a book from a member."""
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)
        else:
            print("Member or book not found")

    def display_books(self):
        """Display all books."""
        if not self.books:
            print("No books in the library")
        else:
            for book in self.books.values():
                book.display_info()

    def display_members(self):
        """Display all members."""
        if not self.members:
            print("No members in the library")
        else:
            for member in self.members.values():
                member.display_info()

    def display_dvds(self):
        """Display all DVDs."""
        if not self.dvds:
            print("No DVDs in the library")
        else:
            for dvd in self.dvds.values():
                dvd.display_info()

    def display_all(self, items):
        """Display information for all items (books or members)."""
        for item in items:
            item.display_info()

    def search_books(self, query):
        """Search books by title or author."""
        results = []
        query_lower = query.lower()
        for book in self.books.values():
            if query_lower in book.name.lower() or query_lower in book.author.lower():
                results.append(book)
        return results


# Example usage
if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book(1, "1984", "George Orwell", 3)
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 2)
    library.add_book(book1)
    library.add_book(book2)

    # Add DVDs
    dvd1 = DVD(1, "Inception", "Christopher Nolan", 148)
    dvd2 = DVD(2, "The Matrix", "Wachowski Sisters", 136)
    library.add_dvd(dvd1)
    library.add_dvd(dvd2)

    # Add members
    member1 = Member(1, "Ali")
    member2 = Member(2, "Hicham")
    library.add_member(member1)
    library.add_member(member2)

    # Display
    print("Books:")
    library.display_books()
    print("\nDVDs:")
    library.display_dvds()
    print("\nMembers:")
    library.display_members()

    # Issue book
    print("\nIssuing book 1 to member 1:")
    library.issue_book(1, 1)

    # Display again
    print("\nAfter issuing:")
    library.display_books()
    library.display_members()

    # Return book
    print("\nReturning book 1 from member 1:")
    library.return_book(1, 1)

    # Display again
    print("\nAfter returning:")
    library.display_books()
    library.display_members()

    # Demonstrate polymorphism with display_all
    print("\nDisplay of all books (polymorphism):")
    library.display_all(library.books.values())

    print("\nDisplay of all DVDs (polymorphism):")
    library.display_all(library.dvds.values())

    print("\nDisplay of all members (polymorphism):")
    library.display_all(library.members.values())
