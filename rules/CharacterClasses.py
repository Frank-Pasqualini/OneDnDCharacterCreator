# TODO IN NEED OF CLEANUP AND COMPLETION
class CharacterClass:
    def __init__(self, name: str):
        self.name = name
        self.subclass = None
        self.level = 1
        self.features = []

    def __str__(self):
        output = f"{self.name} {self.level}"

        if self.subclass is not None:
            output = str(self.subclass) + " " + output

        return output


class Expert(CharacterClass):
    def __init__(self, name: str):
        super().__init__(name)
