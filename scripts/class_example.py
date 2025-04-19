class animal():
    def __init__(self, name='animal', age=0):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} and {self.age} years old."
    def speak(self):
        print("I'm", self)

class dog(animal):
    def __init__(self, name='dog', age=0):
        super().__init__(name, age)
    def speak(self):
        print("WOFF!! I'm", self)

class karen(dog, animal):
    def __init__(self, name='karen', age=48):
        super().__init__(name, age)
    def speak(self):
        animal.speak(self)
    def shout2ppl(self):
        super().speak()

if __name__ == "__main__":
    a = animal()
    a.speak()
    d = dog()
    d.speak()
    m = karen()
    m.speak()
    m.shout2ppl()