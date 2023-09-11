class Author:
    #  pass
    def __init__(self, name):
        self.Name = name
        self.Articles = []

    def name(self):
        return self.Name

    def articles(self):
        return self.Articles

    def magazines(self):
        alone_magazines = set()
        for article in self.Articles:
            alone_magazines.add(article.magazine())
        return list(alone_magazines)


class Magazine:
    def __init__(self, name):
        self.Name = name

    def name(self):
        return self.Name


class Article:
    def __init__(self, author, magazine, title):
        self.Author = author
        self.Magazine = magazine
        self.Title = title
        author.articles().append(self)

    def title(self):
        return self.Title

    def magazine(self):
        return self.Magazine


author = Author("Captain Morgan")
magazine1 = Magazine("First Magazine")
magazine2 = Magazine("Second Magazine")
article1 = Article(author, magazine1, "First Article")
article2 = Article(author, magazine2, "Second Article")
article3 = Article(author, magazine1, "Third Article")

print(author.name())

for article in author.articles():
    print(article.title())

for magazine in author.magazines():
    print(magazine.name())