class Animal:
    def zvuk(self):
        self.golos=None
        print(self.golos)


class Sobaka(Animal):
    def __init__(self):
        self.golos="Gav"


sharik=Sobaka()
sharik.zvuk()