import random


class KindaBool:
    names = {1: "False", 2: "KindaFalse", 3: "Neutral", 4: "KindaTrue", 5: "True"}

    def __init__(self, value: int):
        if value not in range(1, 6):
            raise ValueError("value must be in range 1-5")
        self.value = value

    def __bool__(self):
        return random.randint(1, 4) < self.value

    def __repr__(self):
        return f"KindaBool({self.value})"

    def __str__(self):
        return self.names[self.value]

    def __int__(self):
        return self.value
