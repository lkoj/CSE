class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
            """This method tales a direction, and finds the variable of the
            room.

            :param direction: A String (all lowercase), with a cardinal direction
            :return: A room object if it exists, None of it does not
            """
            return getattr(self.current_location, direction)



# There are the instances of the room (Instantiation)

Master_Room = Room("This is the room you start in", None, None)
Kitchen = Room("This is the kitchen here is where I eat", None, Master_Room)
Exit_Door = Room("The exit door is here I can go outside",None)
Living_Room = Room("I'm in the living room", None, Exit_Door)

Master_Room.east = Kitchen
Kitchen.north = Exit_Door
Exit_Door.west = Living_Room
Living_Room.south = Exit_Door

player = Player(Master_Room)

directions = ['north', 'south', 'east', 'west', 'up', 'down' ]
playing = True

# Controller
while playing:
    print(player.current_location.name)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except AttributeError:
            print("There is no path this way")
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")

print(player.current_location.name)

while playing:
