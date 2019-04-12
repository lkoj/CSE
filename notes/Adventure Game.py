class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description


# There are the instances of the room (Instantiation)

Master_Room = Room("This is the room you start in", None, None)
Kitchen = Room("This is the kitchen here is where I eat", None, Master_Room)
Exit_Door = Room("The exit door is here I can go outside", None)
Living_Room = Room("I'm in the living room", None, Exit_Door)
Garage = Room("Look at all these cars", None, Living_Room)
Basement = Room("Look at all these stuff in the", None, Garage)
Attic = Room("Look there are some many things in here!!!", None, Garage)

Master_Room.east = Kitchen
Kitchen.north = Exit_Door
Exit_Door.west = Living_Room
Living_Room.south = Exit_Door
Garage.east = Living_Room

directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_direction = ['n', 's', 'e', 'w', 'u', 'd']
playing = True


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(object):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.Weapon = True
        self.damage = 70
        self.battery_life = 100


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword")
        self.damage = 50


class Gun(Weapon):
    def __init__(self):
        super(Gun, self).__init__("Gun")
        self.damage = 70


class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__("Axe")
        self.damage = 40


class Knifes(Weapon):
    def __init__(self):
        super(Knifes, self).__init__("Knifes")
        self.damage = 25


class Shotgun(Weapon):
    def __init__(self):
        super(Shotgun, self).__init__("Shotgun")
        self.damage = 100


class Flashlight(Weapon):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight")
        self.Battery_life = 100


class Tourch(Weapon):
    def __init__(self):
        super(Tourch, self).__init__("Tourch")
        self.fuel = 100


class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.fuel = 100


class Jeep(Vehicle):
    def __init__(self):
        super(Jeep, self).__init__("Jeep")
        self.fuel = 100


class Ford(Vehicle):
    def __init__(self):
        super(Ford, self).__init__("Ford")
        self.fuel = 100


class Buffalo(Vehicle):
    def __init__(self):
        super(Buffalo, self).__init__("Buffalo")
        self.fuel = 100


class Humuee(Vehicle):
    def __init__(self):
        super(Humuee, self).__init__("Humuee")


class Chevrolet(Vehicle):
    def __init__(self):
        super(Chevrolet, self).__init__("Chevrolet")


class Armor(Item):
    def __init__(self, name, armor_amt):
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor


class Player(Character):
    def __init__(self, name, health, weapon, armour):
        super(player, self).__init__(name, health, weapon, armour)
        self.inventory = []


while playing:
    player = Player(Master_Room)
    print(player.current_location.name)

    command = input(">_")
    if command in short_direction:
        pos = short_direction.index(command)
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        pass
    elif "take" in command:
        Item_name = command[5:]
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except AttributeError:
            print("THere is no path this way")
        except KeyError:
            print("I can't go that way.")
    else:player = Player(Master_Room)
    print("Command not recognized.")
Found_item = None
for item in player.current_location.item:
    if item.name == Item_name:
        Found_item = item
    if Found_item is not Item_name:
        player.inventory.append(Found_item)
        player.current_location.item.remove(Found_item)


def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because of some FABULOUS armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))


def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Characters
Joseph = Character("Joseph", 150, Gun, Armor("Metal", 50))
enemy = Character("enemy", 100, Sword, Armor("Wooden", 30))

enemy.attack(Joseph)
Armor(enemy)
Joseph(enemy)
