"""
This module includes different classes for game, adopted to Lviv's locations.
"""
class Character:
    """
    This class represent one instance of character.
    """
    def __init__(self, name: str, description: str) -> None:
        """
        The constructor for a class.
        """
        self.__name = name
        self.description = description
        self.quote = None

    def talk(self):
        """
        This method represent character's phrase.
        """
        print(f"{self.__name}: {self.quote}")

    def describe(self):
        """
        This method describe's enemy.
        """
        print(f"{self.__name} is here!")
        print(f"{self.description}")


class MainCharacter:
    """
    This class represent an instance of the main character.
    """
    def __init__(self, name) -> None:
        """
        The constructor for a class.
        """
        self.name = name
        self.money = 100
        self.able_to_play = True
        self.have_docs = False
        self.backpack = []

    def take_docs(self):
        """
        This method allows main character to take his docs.
        """
        choice = input('>>> ')
        if choice.lower() == 'yes':
            self.have_docs = True


class Street:
    """
    This class represent a street.
    """
    def __init__(self, street_name: str) -> None:
        """
        The constructor for a class.
        """
        self.street_name = street_name
        self.another_streets = {}
        self.character = None
        self.item = None
        self.description = None

    def set_description(self, description):
        """
        This method sets a description for a street.
        """
        self.description = description

    def link_street(self, other_street, part_of_the_world: str) -> None:
        """
        This method links different streets as parts of the world to current street.
        """
        self.another_streets[part_of_the_world] = other_street

    def set_character(self, enemy):
        """
        This method links a street with an enemy.
        """
        self.character = enemy

    def set_item(self, item):
        """
        This method links a street with an item that will be at this street.
        """
        self.item = item

    def get_details(self):
        """
        This method sets description for current street.
        """
        print(self.street_name)
        print(self.description)
        print("-" * 20)
        for part, street in self.another_streets.items():
            print(f"{street.street_name} is {part}")

    def move(self, command: str):
        """
        This method returns direction to the another street.
        """
        return self.another_streets[command]

    def get_character(self):
        """
        This method returns enemy, that is in the street.
        """
        return self.character

    def get_item(self):
        """
        This method return's item's name
        """
        return self.item


class Item:
    """
    This class represent the item.
    """
    def __init__(self, name) -> None:
        """
        The constructor for a class.
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        This method sets description to the current item.
        """
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


class Enemy(Character):
    """
    This class represent one instance of enemy.
    """
    def __init__(self, name: str, description: str) -> None:
        """
        The constructor for a class.
        """
        super().__init__(name, description)
        self.weakness = None

    def fight(self, tool_to_fight):
        """
        This method represent fight with an enemty.
        """
        if tool_to_fight == self.weakness:
            print('YES! You got it! Won the fight!')
            return True
        return False


class Policeman(Character):
    """
    This class represent an instance of policeman.
    Policeman only checks your docs.
    If you have docs - you can go, otherwise - you lose.
    """
    def __init__(self, name: str, description: str) -> None:
        """
        The constructor for a class.
        """
        super().__init__(name, description)
        self.quote = 'Good afternoon sir! Can you show me your docs?'

    def check_documents(self, main_character):
        """
        This method represen't policeman's document's check.
        """
        print('Policeman is coming to you...')
        print('Good afternoon sir! Can you show me your docs?(yes/no)')
        choice = input('>>> ')
        if choice.lower() == 'yes':
            if main_character.have_docs:
                print('Thank you! Have a nice day!')
            else:
                print("Sorry, but as I see you don't have docs with yourself. Come with me!")
                main_character.able_to_play = False
        else:
            print('Sorry, but you have to follow me to recognize your personality!')
            main_character.able_to_play = False


class Homeless(Character):
    """
    This class represent an instance of homeless character.
    He can only talk and you can give him some money.
    """
    def __init__(self, name: str, description: str) -> None:
        """
        The constructor for a class.
        """
        super().__init__(name, description)
        self.quote = 'Such a hard days are coming! COVID, war... What will be next?'

    def ask_for_money(self, main_character):
        """
        This method represent when homeless asks for money
        """
        print('Hey, maybe you have some small change?(yes, no)')
        choice = input('>>> ')
        if choice.lower() == 'yes':
            main_character.money -= 20
            print("Oooh, thank you, dear! God bless you!")
        elif choice.lower() == 'no':
            print("Go away! You're all so scrooge!")
        else:
            print('What did you say? Ahh, go away!')


class GopnikFromLevandivka(Enemy):
    """
    This class represent gopnik from Lviv's Levandivka.
    """
    def __init__(self, name: str, description: str) -> None:
        """
        The constructor for a class.
        """
        super().__init__(name, description)
        self.quote = "Shigirau! Haw u doin'?) Have a cigarette?"
        self.weakness = 'book'

    def fight(self, tool_to_fight):
        """
        This method represent fight with an enemty.
        """
        if tool_to_fight == self.weakness:
            print('YES! You got it! You made a gopnik smarter!')
            return True
        return False


class Russian(Enemy):
    """
    This class represent russian.
    """
    def __init__(self, name: str, description: str) -> None:
        """
        The constructor for a class.
        """
        super().__init__(name, description)
        self.quote = "Dobriy den'! Kak vashi dela? U vas krasyvii gorod!"
        self.weakness = 'pistol'


class AngryMolfar(Enemy):
    """
    This class represent angry molfar(the boss).
    """
    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.quote = 'I will destoy you! Try to fight with me!'
        self.weakness = 'gold'


class MagicLaboratory:
    """
    This class represent magic laboratory, with help of each
    main character can make gold from bronze.
    """
    def make_gold(self, main_character):
        """
        This method represent the proccess of making gold from bronze.
        """
        print('This is a magic laboratory and here you can make a gold from bronze!')
        print('Do you want to convert bronze into the gold?(yes/no)\n')
        choice = input('>>> ')
        if choice.lower() == 'yes':
            if 'bronze' in main_character.backpack:
                main_character.backpack.remove('bronze')
                main_character.backpack.append('gold')
                print("You've done it! Now you're able to be the best!")
            else:
                print("You don't have bronze in your backpack! Go and search it!")
        else:
            return
