from abc import ABC, abstractmethod


class Musician(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

    # Thanks to Raven (TA), Lauren Main, and Adam Owada for the collective
    # effort to make this final stretch goal work.
    @abstractmethod
    def some_method_that_must_be_implemented_in_base_class(self):
        pass


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.instrument = "guitar"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "face melting guitar solo"

    def some_method_that_must_be_implemented_in_base_class(self):
        pass

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

    def play_solo(self):
        return "bom bom buh bom"

    def some_method_that_must_be_implemented_in_base_class(self):
        pass

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

    def play_solo(self):
        return "rattle boom crash"

    def some_method_that_must_be_implemented_in_base_class(self):
        pass

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


class Keyboardist(Musician):
    def __init__(self, name, instr):
        super().__init__(name)
        self.name = name
        self.instrument = "keyboard"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "plink plink plink"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


class Band:
    instances = []

    @classmethod
    def to_list(cls):
        return cls.instances

    def __init__(self, name, members, ):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        member_strings = [str(member) for member in self.members]
        return " ".join(member_strings)

    def play_solos(self):
        solos = [member.play_solo() for member in self.members]
        return solos
