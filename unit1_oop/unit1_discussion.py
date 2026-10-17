"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Character:
    starting_health = 100  # Class variable representing the default health for all characters

    def __init__(self, name: str, inventory: list):
        self.name = name
        self.inventory = inventory
        self.health = self.starting_health
    
    def describe(self):
        return f"{self.name}: {self.health}/{self.starting_health} HP, Inventory: {self.inventory}"

    def take_damage(self, amount: int):
        self.health = max(0, self.health - amount)  # Ensure health doesn't go below 0

    def heal(self, amount: int):
        self.health = min(self.starting_health, self.health + amount)  # Ensure health doesn't exceed starting health

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class NPC(Character):
    starting_health = 50 
    npc_count = 0  # Class variable to keep track of the number of NPCs created

    def __init__(self, name: str, inventory: list, npc_role: str, dialogue: str):
        super().__init__(name, inventory)  # Call the parent class constructor
        self.npc_role = npc_role
        self.dialogue = dialogue
        NPC.npc_count += 1  # Increment the NPC count whenever a new NPC is created

    def describe(self):
        return f"{super().describe()} Role: {self.npc_role}"

    def interact(self):
        return f"{self.name} says: '{self.dialogue}'"

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Three NPC objects
    baker = NPC("Tomasz Chlebowski", ["Bread", "Rolling Pin"], 
                "Baker", "Heya! I am a kind, old baker!")
    guard = NPC("Jan Wachman", ["Sword", "Shield"], 
                "Guard", "You shall not pass!")
    villager = NPC("Anna Kowalska", ["Basket", "Herbs"], 
                   "Villager", "Good day! Care for some herbs?")

    # Accessing class variable through the class and objects
    print(f"Class variable accessed through class: {NPC.npc_count}")
    print(f"Class variable accessed through object: {baker.npc_count}")

    # Adding npc_type attribute to only one object
    baker.npc_type = "Hostile NPC"

    # Displaying each object's namespace
    print(f"\nBaker's namespace: {baker.__dict__}")
    print(f"Guard's namespace: {guard.__dict__}")
    print(f"Villager's namespace: {villager.__dict__}")

    # Displaying the class namespace
    print(f"\nNPC class namespace: {NPC.__dict__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create a character with nested mutable inventory data
    player = Character(
        "Player",
        [{"name": "Health Potion", "effects": ["restore health"]}]
    )

    # Create a shallow copy and a deep copy
    shallow_copy = copy(player)
    deep_copy = deepcopy(player)

    # Modify the nested data in the original character
    player.inventory[0]["effects"].append("increase strength")

    # Display the results
    print("\nOriginal character:", player.__dict__)
    print("Shallow copy:", shallow_copy.__dict__)
    print("Deep copy:", deep_copy.__dict__)

    # A shallow copy creates a new outer object but shares nested objects.
    # Therefore, changing the original inventory's nested list also
    # changes what the shallow copy sees.

    # A deep copy recursively copies nested objects.
    # Therefore, the deep copy retains its original inventory effects.


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n" + "=" * 45)
    print("       WELCOME TO THE ADVENTURE!")
    print("=" * 45)

    # Create an object of the parent class, Character.
    # Input validation prevents the player from having an empty name.
    while True:
        try:
            name = input("\nChoose a name for your character: ").strip()

            if not name:
                raise ValueError("Character name cannot be empty.")

            break

        except ValueError as error:
            print(f"Invalid input: {error}")

    player = Character(
        name,
        ["Map", "Compass", "Pencil of Unbreaking"]
    )

    print("\n" + "-" * 45)
    print("             CHARACTER CREATED")
    print("-" * 45)
    print(player.describe())

    # Create objects of the child class, NPC.
    # NPC inherits Character's attributes and methods.
    baker = NPC("Tomasz Chlebowski", ["Bread", "Rolling Pin"], 
        "Baker", "Heya! I am a kind, old baker! Absolutely nothing happens to your health!. . .")
    villager = NPC("Anna Kowalska", ["Basket", "Herbs"], 
        "Villager", "Good day! Care for some healing herbs? I've been foraging in the forest for mushrooms!")
    guard = NPC("Jan Wachman", ["Sword", "Shield"], 
        "Guard", "You shall not pass!")

    # Demonstrate inheritance and method overriding.
    # describe() is inherited from Character and overridden by NPC
    # to include each NPC's role. interact() is an NPC-specific method.
    print("\n" + "-" * 45)
    print("                MEET THE NPCs")
    print("-" * 45)
    print(baker.describe())
    print(guard.describe())
    print(villager.describe())

    # Main game loop lets the player interact with the objects.
    while True:
        print("\n" + "=" * 45)
        print("                 ADVENTURE MENU")
        print("=" * 45)
        print("  1. View your character")
        print("  2. Talk to the baker")
        print("  3. Talk to the villager")
        print("  4. Talk to the guard")
        print("  5. Exit the game")
        print("-" * 45)

        choice = input("Choose an action (1-5): ").strip()

        if choice == "1":
            print("\n--- YOUR CHARACTER ---")
            print(player.describe())

        elif choice == "2":
            print("\n--- THE BAKER ---")
            print(baker.interact())
            player.take_damage(99)
            print(f"\n You take 99 damage! HP: {player.health}/{player.starting_health}")

        elif choice == "3":
            print("\n--- THE VILLAGER ---")
            print(villager.interact())
            player.heal(50)
            print(f"\n You gain 50 health! HP: {player.health}/{player.starting_health}")

        elif choice == "4":
            print("\n--- THE GUARD ---")
            print(guard.interact())
            player.take_damage(10)
            print(f"\n You take 10 damage! HP: {player.health}/{player.starting_health}")

        elif choice == "5":
            print("\nThanks for playing. Goodbye!")
            break

        else:
            # Handle invalid menu choices without crashing the program.
            print("\nInvalid choice. Please enter a number from 1 to 5.")

    # Call the required namespace demonstration function.
    # This displays class and instance namespaces using __dict__.
    demonstrate_namespaces()

    # Call the required copying demonstration function.
    # This compares the effects of shallow and deep copying.
    demonstrate_copying()


if __name__ == "__main__":
    main()