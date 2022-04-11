import csv

# This code loads the current book
# shelf data from the csv file
def load_books(filename):
  bookshelf = []
  with open(filename) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
        print(book['title'])
        book['author_lower'] = book['author'].lower()
        book['title_lower'] = book['title'].lower()
        bookshelf.append(book)
  return bookshelf
