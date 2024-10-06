class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        return "Name: ", self.name, ". Age: ", self.age, ". Is happy: ", self.isHappy, "."

cat1 = Cat()
cat1.set_data("Barsik", 3, True)

cat2 = Cat()
cat2.set_data("Жопен", 2, False)

print(cat1.get_data())
print(cat2.get_data())
