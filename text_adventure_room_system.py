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
    def __init__(self, name, starting_room, max_weight=10, required_key='key'):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.max_weight = max_weight
        self.required_key = required_key

    def current_weight(self):
        total = 0
        for item in self.inventory:
            total += item.weight
        return total

    def move(self, direction, provided_key):
        self.provided_key = provided_key
        if direction in self.current_room.exits and self.provided_key == self.required_key:
            self.current_room = self.current_room.exits[direction]
            print(f'You move {direction}')
        else:
            print("You can't go that way!")
    
    def addInventory(self, item):
        self.inventory.append(item)

    def pick_up(self, item_name):
        for item in self.current_room.items:
            if item.weight > self.max_weight:
                return "Too heavy to carry!"
            else:
                if item.name == item_name and item.can_take:
                    self.inventory.append(item)
                    self.current_room.items.remove(item)
                    return f'You picked up {item_name}'
            return "Can't pick that up"

    def drop(self, drop_item):
        for item in self.inventory: # checks if item can be reamoved from the inventory
            if item.name == drop_item:
                self.inventory.remove(item)
                self.current_room.items.append(item) #adds items to the self.items list from the inventory
                return 'You have dropped an item'
        return "You don't have that item!"

class Item:
    def __init__(self, name, weight=1, can_take=True, description=''):
        self.name = name
        self.weight = weight
        self.can_take = can_take

    def examine(self):
        return self.description or f"It's a {self.name}"

class Container:
    def __init__(self):
        self.chest = []

    def addItemsToChest(self):
        self.chest.extend(self.current_room.items)


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

player = Player('Hero', kitchen, 'key')
print(player.current_room.name)
player.move('north', 'big')
print(player.current_room.name)
print(type(hero.inventory[0]))
print(hero.inventory[0].weight)
