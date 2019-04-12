class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(object):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.Weapon = True
        self.damage = damage


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


class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
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
        self.fuel = 100


class Chevrolet(Vehicle):
    def __init__(self):
        super(Chevrolet, self).__init__("Chevrolet")


class Armor(Item):
    def __init__(self, name, armor_amt):
        self(Armor).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

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


# Items
sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
wiebe_armor = Armor("Armor of the gods", 10000000000000000000)

# Characters
orc = Character("orc", 100, sword, Armor("Generic",2))
wiebe = Character("Wiebe", 100000000, canoe, wiebe_armor)

orc.attack(wiebe)
wiebe_armor(orc)
wiebe_armor(orc)