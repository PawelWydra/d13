class Names:
    def __init__(self):
        self.reversed_names = []

    def add(self, name):
        return self.reversed_names.append(name[::-1].title())


names = Names()
names.add("Uisaj")
names.add("Aisak")
names.add("Aisa")
names.add("Kemot")
names.add("Lahcim")

print(names.reversed_names)
