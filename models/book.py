class Book():

    def __init__(self, title, author, genre, available):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def __nonzero__(self):
        return self.available !=0 