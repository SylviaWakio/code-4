class Magazine:
    magazines = []

    def __init__(self, name, category):
        self.Name = name
        self.Category = category
        Magazine.magazines.append(self)

    def name(self):
        return self.Name

    def category(self):
        return self.Category

    def all():
        return Magazine.magazines


magazine1 = Magazine("First Magazine", "First Category")
magazine2 = Magazine("Second Magazine", "Second Category")
magazine3 = Magazine("Third Magazine", "First Category")

print(magazine1.name())
print(magazine2.category())

magazines = Magazine.all()
for magazine in magazines:
    print(magazine.name(), magazine.category())