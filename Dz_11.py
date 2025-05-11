class Human:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I'm {self.name}, {self.age} years old.")

class Programmer(Human):
    def __init__(self, language, **kwargs):
        super().__init__(**kwargs)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}.")

class Youtuber(Human):
    def __init__(self, channel_name, **kwargs):
        super().__init__(**kwargs)
        self.channel_name = channel_name

    def film_video(self):
        print(f"{self.name} is filming a video for {self.channel_name}.")

class TechInfluencer(Programmer, Youtuber):
    def __init__(self, name, age, language, channel_name):
        super().__init__(name=name, age=age, language=language, channel_name=channel_name)

    def show_profile(self):
        self.introduce()
        self.code()
        self.film_video()

influencer = TechInfluencer("Олег", 25, "Python", "CodeLife")
influencer.show_profile()
