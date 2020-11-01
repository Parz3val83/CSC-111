class Book:

    def __init__(self, title='', isbn='', authors='', publisher='', edition='', published_year=0):
        self.title = title
        self.isbn = isbn
        self.authors = authors
        self.publisher = publisher
        self.edition = edition
        self.published_year = published_year

    def setTitle(self, title):
        self.title = title

    def setIsbn(self, isbn):
        self.isbn = isbn

    def setAuthors(self, authors):
        self.authors = authors

    def setPublisher(self, publisher):
        self.publisher = publisher

    def setEdition(self, edition):
        self.edition = edition

    def setPublished_year(self, published_year):
        self.published_year = published_year



    def getTitle(self):
        return self.title

    def getIsbn(self):
        return self.isbn

    def getAuthors(self):
        return self.authors

    def getPublisher(self):
        return self.publisher

    def getEdition(self):
        return self.edition

    def getPublished_year(self):
        return self.published_year
    

    def print(self):
        print('\n\nTitle:', self.title, '\nIsbn', self.isbn, '\nAuthors:', self.authors, '\nPublisher:', self.publisher, '\nEdition:', self.edition, '\nPublished year:', self.published_year)

    
        


class NewBook(Book):

    def __init__(self, title='', isbn='', authors='', publisher='', edition='', published_year=0, price=0.0):
        Book.__init__(self, title, isbn, authors, publisher, edition, published_year)
        self.price = price

    def setPrice(self, price):
        self.price = price


    
    def getPrice(self):
        return self.price



    def calculate_price(self):
        return self.price

    def print(self):
        print('\n\nTitle:', self.title, '\nIsbn', self.isbn, '\nAuthors:', self.authors, '\nPublisher:', self.publisher, '\nEdition:', self.edition, '\nPublished year:', self.published_year, '\nPrice:', self.price)



class UsedBook(Book):

    def __init__(self, title='', isbn='', authors='', publisher='', edition='', published_year=0, price_new=0, age=0): # What does the double mean
        Book.__init__(self, title, isbn, authors, publisher, edition, published_year)
        self.price_new = price_new
        self.age = age

    
    def setPrice_new(self, price_new):
        self.price_new = price_new

    def setAger(self, age):
        self.age = age



    def getPrice_new(self):
        return self.price_new

    def getAge(self):
        return self.age



    def calculate_price(self):
        return self.price_new * (1 - (0.01 * self.age))

    def print(self):
        print('\n\nTitle:', self.title, '\nIsbn', self.isbn, '\nAuthors:', self.authors, '\nPublisher:', self.publisher, '\nEdition:', self.edition, '\nPublished year:', self.published_year, '\nPrice new:', self.price_new, '\nAge:', self.age)
