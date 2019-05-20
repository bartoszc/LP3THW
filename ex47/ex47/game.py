class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.witcher_trigger = False

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def death(self):
        quips = ["You died.  You kinda suck at this.",
                "Your Mom would be proud...if she were smarter.",
                "Such a luser.",
                "I have a small puppy that's better at this.",
                "You're worse than your Dad's jokes."]
        return(quips[randint(0, len(self.quips)-1)])
        exit(1)
