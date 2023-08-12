class Players:
    def __init__(self):
        print("This is the Players class")

class team(Players):
    def __init__(self):
        Players.__init__(self)
        print("This is the team class")

class Vaccination(Players):
    def __init__(self):
        Players.__init__(self)
        print("This is the vaccination class")

class Diet(Players):
    def __init__(self):
        Players.__init__(self)
        print("This is the Diet class")

class Training(team, Vaccination):
    def __init__(self):
        team.__init__(self)
        Vaccination.__init__(self)
        print("This is the Training class")

class FootballManagement(Training, Diet):
    def __init__(self):
        Training.__init__(self)
        Diet.__init__(self)
        print("This is the FootballManagement class")

obj = FootballManagement()