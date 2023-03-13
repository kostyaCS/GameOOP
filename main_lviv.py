"""
This module represent the game in Lviv.
"""
import game_lviv


main_character = game_lviv.MainCharacter('Your name here!')

kozelnytska = game_lviv.Street("Kozelnytska Street")
kozelnytska.set_description("Your alma mater! You came here young, but you will leave with new strength and knowledge")

levandivka = game_lviv.Street("Levandivka Street")
levandivka.set_description("Such a dangerous place! During the day, it plays with its colors,\
 and at night local burlaks, who are called gopniks, come here")

virmenska = game_lviv.Street("Virmenska Street")
virmenska.set_description("The smell of delicious coffee, bright shops and interesting people! What could be better?")

pid_dubom = game_lviv.Street("Pid Dubom Street")
pid_dubom.set_description("Semi-working district. Lots of offices, busy people and traffic.")

rinok = game_lviv.Street("Rinok Square")
rinok.set_description("The central square of the city. Music, dancing, mysteries - it's all here!")

tarasa_shevchenka = game_lviv.Street('Tarasa Shevchenka Street')
tarasa_shevchenka.set_description("Won't say anything about this place. It's wonderful!")

outages = game_lviv.Street("Outage of Lviv")
outages.set_description("Where else could the secret forge be located? Of course on the outage!")

kozelnytska.link_street(rinok, "south")
rinok.link_street(levandivka, 'west')
levandivka.link_street(rinok, 'east')
levandivka.link_street(virmenska, 'south')
virmenska.link_street(levandivka, 'north')
virmenska.link_street(tarasa_shevchenka, "east")
tarasa_shevchenka.link_street(virmenska, "west")
tarasa_shevchenka.link_street(pid_dubom, 'east')
pid_dubom.link_street(outages, "south")
pid_dubom.link_street(tarasa_shevchenka, 'west')
outages.link_street(pid_dubom, 'north')


magic_lab = game_lviv.MagicLaboratory()


policeman = game_lviv.Policeman("Policeman Dmytro", "Guardian of the city order")
pid_dubom.set_character(policeman)

homeless = game_lviv.Homeless("Homeless Mark", "The man who had everything but lost everything")
virmenska.set_character(homeless)

gopnik = game_lviv.GopnikFromLevandivka('Andrew-gopnik', 'The usual prototype of the gangster culture of the city')
levandivka.set_character(gopnik)

russian = game_lviv.Russian('russian guy Evgeniy', 'A typical Russian - a person who should not exist')
rinok.set_character(russian)

angry_molfar = game_lviv.AngryMolfar('Molfar Yagailo', 'He is a Carpathian legend. The whole country is afraid of him!')
tarasa_shevchenka.set_character(angry_molfar)

bronze = game_lviv.Item('bronze')
bronze.set_description("This methal was found in Virmenska street, so there are a lot of it here.")
virmenska.set_item(bronze)

pistol = game_lviv.Item('pistol')
pistol.set_description("Desert Eagle, which is very often used in street fights. But be careful with it!")
pid_dubom.set_item(pistol)

book = game_lviv.Item('book')
book.set_description("A very interesting fantastic story '39 keys'.")
rinok.set_item(book)


current_street = kozelnytska

asked = False
documents_checked = False
asked_for_docs = False


while main_character.able_to_play:
    print("\n")
    current_street.get_details()
    if not asked_for_docs:
        if current_street == kozelnytska and not main_character.have_docs:
            print("Such an worrious days are coming! Do you wanna take documents with yourself?")
            choice = input('>>> ')
            if choice.lower() == 'yes':
                main_character.have_docs = True
            else:
                print("I don't understand you!")
                continue
        asked_for_docs = True
        continue
    print('\n')
    if current_street == outages and not asked:
        if 'gold' not in main_character.backpack:
            magic_lab.make_gold(main_character)
            asked = True
            continue
    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        print('\n')

    if inhabitant == policeman and not documents_checked:
        policeman.check_documents(main_character)
        
        if not main_character.able_to_play:
            break
        documents_checked = True
        current_street.character = None
        continue

    item = current_street.get_item()
    if item is not None:
        item.describe()
        print('\n')


    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        asked = False
        try:
            current_street = current_street.move(command)
        except KeyError:
            print('There is no street at this direction')
            continue
    elif command == "talk":
        asked = False
        if inhabitant is not None:
            inhabitant.talk()
            if inhabitant == homeless:
                homeless.ask_for_money(main_character)
                if main_character.money <= 0:
                    print("You lose all your money! What a pity!")
                    main_character.able_to_play = False
    elif command == "fight":
        asked = False
        if inhabitant is not None:
            print("What will you fight with?")
            fight_with = input()
            if fight_with in main_character.backpack:
                if inhabitant.fight(fight_with):
                    current_street.character = None
                    if inhabitant == angry_molfar:
                        print('Yes! You made it! You killed the boss! This is a victory!')
                        break
                else:
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the Game!")
                    main_character.able_to_play = False
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        asked = False
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            main_character.backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
