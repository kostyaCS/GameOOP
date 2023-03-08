"""
This module represent a game, with classes as Room, Enemy, Friend, Item and Character.
"""
class Room:
    """
    This class represent one instance of room.
    """
    def __init__(self, room_type: str) -> None:
        """
        The constructor for a class.
        """
        self.room_type = room_type
        self.description = None
        self.another_rooms_as_parts_of_the_world = {}
        self.character = None
        self.item = None

    def set_description(self, description: str) -> None:
        """
        This method sets description to the room.
        """
        assert isinstance(description, str), f'Invalid description for {self.room_type}'
        self.description = description

    def link_room(self, other_room, part_of_the_world: str) -> None:
        """
        This method links different rooms as parts of the world to current room.
        """
        self.another_rooms_as_parts_of_the_world[part_of_the_world] = other_room

    def set_character(self, enemy):
        """
        This method links a room with an enemy.
        """
        self.character = enemy

    def set_item(self, item):
        """
        This method links a room with an item that will be in this room.
        """
        self.item = item

    def get_details(self):
        """
        This method sets description for current room.
        """
        print(self.room_type)
        print("-" * 20)
        for part, room in self.another_rooms_as_parts_of_the_world.items():
            print(f"{room.room_type} is {part}")

    def get_character(self):
        """
        This method returns enemy, that is in the room.
        """
        return self.character

    def move(self, command: str):
        """
        This method returns direction to the another room.
        """
        return self.another_rooms_as_parts_of_the_world[command]

    def get_item(self):
        """
        This method return's item's name
        """
        return self.item


class Enemy:
    """
    This class represent one instance of enemy that lives in the room.
    """
    number_of_defeated = 0

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.quote = None
        self.weakness = None

    def set_conversation(self, quote):
        """
        This method sets a quote of current enemy.
        """
        assert isinstance(quote, str), f"Invalid quote for {self.name}"
        self.quote = quote

    def set_weakness(self, kill_item):
        """
        This method links an item that can kill an enemy with enemy.
        """
        self.weakness = kill_item

    def talk(self):
        """
        This method return's enemy's quote. 
        """
        print(f"[{self.name} says]: {self.quote}")

    def describe(self):
        """
        This method describe's enemy.
        """
        print(f"{self.name} is here!")
        print(f"{self.description}")

    def fight(self, tool):
        """
        This method represent fight with enemy.
        """
        if tool == self.weakness:
            self.number_of_defeated += 1
            return True
        return False

    def get_defeated(self):
        """
        This method returns number of defeated enemies.
        """
        return self.number_of_defeated



class Item:
    """
    This method represent one instance of item that will be in the room.
    """
    def __init__(self, name) -> None:
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        This method sets description to the current item.
        """
        assert isinstance(description, str), f"Inavlid description for {self.name}"
        self.description = description


    def describe(self):
        """
        This method describes an item.
        """
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        """
        This method returns item's name.
        """
        return self.name
