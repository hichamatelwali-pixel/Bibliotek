# Library Management System

This is a simple library management system made in Python, with object programming such as classes, objects, inheritance, and polymorphism.

## Features

- **Book Management**: Add, remove, update, and display books.
- **DVD Management**: Add, remove, update, and display DVDs.
- **Member Management**: Add, remove, update, and display members.
- **Book Issuing and Returning**: Issue books to members if available, and return them.
- **Search Functionality**: Search books by title or author.
- **Polymorphism**: Demonstrated through the `display_info` method in `Book`, `DVD`, and `Member` classes, all inheriting from `Item`.

## Classes

### Item (Base Class)
- Attributes: `id`, `name`
- Methods: `display_info` (polymorphic)

### Book (Inherits from Item)
- Additional Attributes: `author`, `copies`
- Methods: `__init__`, `display_info`

### DVD (Inherits from Item)
- Additional Attributes: `director`, `duration`
- Methods: `__init__`, `display_info`

### Member (Inherits from Item)
- Additional Attributes: `borrowed_books` (list of Book objects)
- Methods: `__init__`, `display_info`, `borrow_book`, `return_book`

### Library
- Attributes: `books` (dict), `dvds` (dict), `members` (dict)
- Methods: `add_book`, `remove_book`, `update_book`, `add_dvd`, `remove_dvd`, `update_dvd`, `add_member`, `remove_member`, `update_member`, `issue_book`, `return_book`, `display_books`, `display_dvds`, `display_members`, `display_all`, `search_books`

## Installation and Setup

1. Have Python is installed.
2. Download the project files.
3. Run the main script: `python library_management_system.py`
4. Run tests: `python "Library test.py"`


## Testing

Unit tests are provided in `Library test.py` using Python's `unittest` module. Run the tests to verify functionality.

## Requirements

- Python

## Author

Hicham

## License

No license
