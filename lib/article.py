class Article:
    articles = []

    def __init__(self, author, magazine, title):
        self.Author = author
        self.Magazine = magazine
        self.Title = title
        Article.articles.append(self)

    def title(self):
        return self.Title

    def author(self):
        return self.Author

    def magazine(self):
        return self.Magazine

    def all():
        return Article.articles


class Author:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    def name(self):
        return self._name

    def category(self):
        return self._category


author1 = Author("Morgan Jason,")
author2 = Author("Jason Morgan,")

magazine1 = Magazine("First Magazine", "Category One")
magazine2 = Magazine("Second Magazine", "Category Two")

article1 = Article(author1, magazine1, "Article 1:")
article2 = Article(author2, magazine2, "Article 2:")
article3 = Article(author1, magazine1, "Article 3:")

print(article1.title())
print(article1.author().name())
print(article1.magazine().name())

articles = Article.all()
for article in articles:
    print(article.title(), article.author().name(), article.magazine().name())