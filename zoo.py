class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species: str, name: str) -> None:
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species: str) -> str:
        if species == "mammal":
            species_title = "Mammals"
            names = ", ".join(self.mammals)
        elif species == "fish":
            species_title = "Fishes"
            names = ", ".join(self.fishes)
        elif species == "bird":
            species_title = "Birds"
            names = ", ".join(self.birds)
        else:
            species_title = species.capitalize() + "s"
            names = ""

        return f"{species_title} in {self.name}: {names}\nTotal animals: {Zoo.__animals}"


zoo_name = input().strip()
zoo = Zoo(zoo_name)

n = int(input().strip())
for _ in range(n):

    species, name = input().split()
    zoo.add_animal(species, name)

query_species = input().strip()
print(zoo.get_info(query_species))
