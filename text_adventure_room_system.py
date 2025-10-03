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
        for item in current_room.items:
            if item.name == item_name and item.can_take:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                return f'You picked up {item_name}'
        return "Can't pick that up"

    def drop(self, drop_item):
        for item in current_room.inventory:
            if inventory:
                self.drop_item = Player.inventory.pop(item)
                current_room.items.append(drop_item[item])
                return current_room.items
        return 'Empty inventory no item to drop!'

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
hero.addInventory('sword')
villian.addInventory('shield')

print(villian.inventory)

player = Player('Hero', kitchen)
print(player.current_room.name)
player.move('north')
print(player.current_room.name)

""" Implement the basic Room class """
"""Add a Player class that tracks current location"""
"""Add methods for moving between rooms"""
"""Bonus: How would you handle locked doors?"""
