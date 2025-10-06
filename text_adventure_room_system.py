class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # {'north': room_object, 'south': room_object}
        self.items = []

    def add_exit(self, direction, room):
        """Connect this room to another"""
        self.exits[direction] = room
        # Bonus: automatically add reverse connection?

    def describe(self):
        """Return full description including exits"""
        items_list = [item.name for item in self.items]
        item_names = ' '.join(items_list)
        next_room = self.exits.keys()
        enter_room = ' '.join(list(next_room))

        return ', '.join([self.name, self.description, item_names, enter_room])

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            return f'You move {direction}'
        return "You can't go that way!"
    
    def addInventory(self, item):
        self.inventory.append(item)

    def pick_up(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name and item.can_take:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                return f'You picked up {item_name}'
        return "Can't pick that up"

    def drop(self, dropped_item):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                self.current_room.items.append(item)
                return 'You have droped an item'
        return "You don't have that item!"

class Item:
    def __init__(self, name, can_take=True):
        self.name = name
        self.can_take = can_take

# Usage would look like:
kitchen = Room("Kitchen", "A messy kitchen with dishes everywhere")
hallway = Room("Hallway", "A narrow corridor")
kitchen.add_exit("north", hallway)
hallway.add_exit('south', kitchen)

hero = Player('Hero', kitchen)
villian = Player('Villian', hallway)
sword = Item('sword')
hero.addInventory(sword)
shield = Item('shield')
villian.addInventory(shield)

print(villian.inventory)

player = Player('Hero', kitchen)
print(player.current_room.name)
player.move('north')
print(player.current_room.name)
print(type(hero.inventory[0]))
