inventory = {
    'clues':[],
    'items':[]
}

def start_game():
    print("Welcome to the Abandoned Arcade!")
    print("You're standing in front of an old arcade machine. The screen is flickering strangely, sparking your curiousity.")

    choice1 = input("Do you investigate the machine or walk through the door? (Type 'machine' or 'door'): ").lower()

    if choice1 == 'machine':
        investigate_machine()
    elif choice1 == 'door':
        enter_hallway()
    else:
        print("A strange static fills the air. That wasn't a choice... Try again.")
        start_game()
def investigate_machine():
    print("You hesistantly touch the machine, and the screen glitches violently.")
    print("A distorted voice crackles through the machine's speakers, 'WHY ARE YOU HERE?'")

    choice2 = input("Do you (1) respond to the voice or (2) step away from the machine? ")

    if choice2 == '1':
        print("The voice chuckles. The screen flashes with a list of names, some indistinguishable from being scratched out.")
        print("One name near the bottom looks familiar... but you don't remember why.")
        print("As you reach out to touch the screen, a small compartment slides open below the machine.")
        print("Inside, you find a crumpled note with shaky handwriting: 'The game sees all. Don't trust the voices.'")
        print("You pocket the note. It might be important later.")
        inventory['clues'].append('Crumpled Note')
        print("(Clue added to inventory: Crumpled Note)")

    elif choice2 == '2':
        print("You step away from the machine, but the voice continues to echo louder, as if... watching you.")
    
    else: 
        print("The screen distorts, the game rejecting your hesitation...")
        investigate_machine()

def enter_hallway():
    print("You push open the door and step into a dimly lit hallway. The air is thick with dust.")
    print("Faint neon lights flicker overhead, casting long, eerie shadows.")

    choice2 = input("Do you (1) examine the strange writing casted on the walls casted by the neon lights or (2) follow the flickering light further into the hallway?")

    if choice2 == '1':
        print("You step closer to the wall. The words shift as you read them, spelling out:")
        print("THE GAME IS WATCHING YOU. THERE IS NO WAY BACK.")
        print("Suddenly, you hear a soft whisper behind you...When you turn, there's nothing but darkness.")
        inventory['clues'].append('Strange Wall Writing')
        print("(Clue added to inventory: Strange Wall Writing)")
    elif choice2 == '2':
        print("You move toward the flickering light. A shadow moves just out of sight.")
        print("It's a girl-pale, glitching slightly, as if she doesn't belong here.")
        print("'You shouldn't be here,' she whispers. The game... it traps us. Find the tokens. They're the only way out.")
        inventory['items'].append('Ghostly Token')
        print("(Item added to inventory: Ghostly Token)")
    else:
        print("The hallway seems to stretch endlessly when you hesitate...")
        enter_hallway()

def check_inventory():
    print("---INVENTORY---")
    print("Clues:", inventory['clues'])
    print("Items:", inventory['items'])

start_game()