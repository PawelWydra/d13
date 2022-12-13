class Names:
    def __init__(self):
        self.reversed_names = []

    def add(self, name):
        to_lower_case = name.lower()
        reverse_and_title = to_lower_case[::-1].title()
        self.reversed_names.append(reverse_and_title)


names = Names()
names.add("Uisaj")
names.add("Aisak")
names.add("Aisa")
names.add("Kemot")
names.add("Lahcim")

print(names.reversed_names)