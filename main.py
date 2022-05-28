class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = int(age)

    def add_track(self, track):
        self.track = track

    def get_score(self, score):
        self.score = float(score)


Bob = Student(name="Bob", age=26, track=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(12.698)


print(f"My name is {Bob.name}.")
print(f"I am under the {Bob.track} Track.")
print(f"I am {Bob.age} years old.")
print(f"My current score is {Bob.score}")