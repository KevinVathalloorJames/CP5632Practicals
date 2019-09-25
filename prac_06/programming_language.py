class ProgrammingLanguage:
    def __init__(self, program_name, typing, reflection, year):
        self.program_name = program_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.program_name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"


def run_test():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [visual_basic, ruby, python]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.program_name)


if __name__ == "__main__":
    run_test()



