class Musician:
    def __init__(self, name):
        name = self.name

    def __str__(self):
        return f"My name is {self.name} and I am a musician"

    def __repr__(self):
        return f'Musician("{self.name}")'


class Guitarist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f'Guitarist("{self.name}")'


class Drummer(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f'Drummer("{self.name}")'


class Bassist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f'Bassist("{self.name}")'
