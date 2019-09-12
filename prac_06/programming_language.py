class ProgrammingLanguage:
    def __init__(self,program_name,typing,reflection,year):
        self.program_name = program_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{},fuel ={}, odometer={}".format(self.name, self.fuel, self.odometer)

    def is_dynamic(self):
        return self.typing == "Dynamic"


