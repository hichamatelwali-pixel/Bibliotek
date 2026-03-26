import unittest
import sys
import os

# Add the opgave 1 directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'opgave 1'))

from library_management_system import Book, Member, Library


class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.library = Library()
        self.book1 = Book(1, "1984", "George Orwell", 3)
        self.book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 2)
        self.member1 = Member(1, "Ali")
        self.member2 = Member(2, "Hicham")

    def test_add_book(self):
        """Test adding a book."""
        self.library.add_book(self.book1)
        self.assertIn(1, self.library.books)
        self.assertEqual(self.library.books[1].name, "1984")

    def test_remove_book(self):
        """Test removing a book."""
        self.library.add_book(self.book1)
        self.library.remove_book(1)
        self.assertNotIn(1, self.library.books)

    def test_remove_nonexistent_book(self):
        """Test removing a book that doesn't exist."""
        self.library.remove_book(999)  # Should not raise error

    def test_update_book(self):
        """Test updating a book."""
        self.library.add_book(self.book1)
        self.library.update_book(1, title="Nineteen Eighty-Four", copies=5)
        book = self.library.books[1]
        self.assertEqual(book.title, "Nineteen Eighty-Four")
        self.assertEqual(book.copies, 5)

    def test_update_nonexistent_book(self):
        """Test updating a book that doesn't exist."""
        self.library.update_book(999, title="Test")  # Should not raise error

    def test_add_member(self):
        """Test adding a member."""
        self.library.add_member(self.member1)
        self.assertIn(1, self.library.members)
        self.assertEqual(self.library.members[1].name, "Ali")

    def test_remove_member(self):
        """Test removing a member."""
        self.library.add_member(self.member1)
        self.library.remove_member(1)
        self.assertNotIn(1, self.library.members)

    def test_update_member(self):
        """Test updating a member."""
        self.library.add_member(self.member1)
        self.library.update_member(1, name="Ali Sadik")
        self.assertEqual(self.library.members[1].name, "Ali Sadik")

    def test_issue_book(self):
        """Test issuing a book."""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)
        self.library.issue_book(1, 1)
        self.assertEqual(self.book1.copies, 2)
        self.assertIn(self.book1, self.member1.borrowed_books)

    def test_issue_book_no_copies(self):
        """Test issuing a book with no copies."""
        book = Book(3, "Out of Stock", "Author", 0)
        self.library.add_book(book)
        self.library.add_member(self.member1)
        self.library.issue_book(1, 3)
        self.assertEqual(book.copies, 0)
        self.assertNotIn(book, self.member1.borrowed_books)

    def test_return_book(self):
        """Test returning a book."""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)
        self.library.issue_book(1, 1)
        self.library.return_book(1, 1)
        self.assertEqual(self.book1.copies, 3)
        self.assertNotIn(self.book1, self.member1.borrowed_books)

    def test_return_book_not_borrowed(self):
        """Test returning a book not borrowed."""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)
        self.library.return_book(1, 1)
        self.assertEqual(self.book1.copies, 3)
        self.assertNotIn(self.book1, self.member1.borrowed_books)

    def test_search_books(self):
        """Test searching books."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        results = self.library.search_books("1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "1984")

        results = self.library.search_books("orwell")
        self.assertEqual(len(results), 1)

        results = self.library.search_books("nonexistent")
        self.assertEqual(len(results), 0)

    def test_polymorphism_display_info(self):
        """Test polymorphic display_info."""
        # Just check that methods exist and can be called without error
        self.book1.display_info()
        self.member1.display_info()


if __name__ == '__main__':
    unittest.main()
