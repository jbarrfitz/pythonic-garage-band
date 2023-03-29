from abc import ABC, abstractmethod


class Musician(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_instrument(self):
        pass


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.instrument = "guitar"

    def get_instrument(self):
        return self.instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.instrument = "bass"

    def get_instrument(self):
        return self.instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.instrument = "drums"

    def get_instrument(self):
        return self.instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


class Band:
    pass
