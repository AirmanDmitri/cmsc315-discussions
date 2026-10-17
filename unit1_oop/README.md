# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation

### 1. Parent Class: Character

I implemented the `Character` class as the parent class for the characters in my RPG. The class variable `starting_health` set the default maximum health to 100. The constructor, `__init__()`, initialized each character's `name`, `inventory`, and `health`. The `describe()` method returned a summary of the character, while `take_damage()` and `heal()` modified health without allowing it to fall below zero or exceed the character's starting health.

### 2. Child Class: NPC

I implemented the `NPC` class as a child of `Character`, allowing NPCs to reuse its attributes and methods. The class defined its own `starting_health` value of 50 and introduced the class variable `npc_count` to track the number of NPC objects created. Each NPC also received a `npc_role` and `dialogue`. The overridden `describe()` method used `super().describe()` to reuse the parent's description before adding the NPC's role. The `interact()` method returned the NPC's dialogue.

### 3. Class and Instance Namespaces

I created the `demonstrate_namespaces()` function to explore class and instance namespaces. It created three NPC objects and accessed `npc_count` through both `NPC.npc_count` and `baker.npc_count`. I then added `npc_type` to the baker alone, demonstrating how an individual object could have an attribute that the other NPCs did not have. Printing each object's `__dict__` displayed its instance attributes, while `NPC.__dict__` displayed the class namespace, including its class variables and methods.

The NPC count displayed six because `main()` created three NPCs before `demonstrate_namespaces()` created another three. Since `npc_count` tracked all NPC objects created during the program's execution, the total increased to six.

### 4. Shallow and Deep Copying

I created the `demonstrate_copying()` function to compare shallow and deep copying using nested inventory data. The character's inventory contained a dictionary representing a health potion, which included a nested list of effects. I created a shallow copy using `copy()` and a deep copy using `deepcopy()`. After adding `"increase strength"` to the original inventory's effects list, the shallow copy reflected the change because it shared the nested data. The deep copy retained its original effects because its nested objects had been copied independently.

### 5. Main Function and RPG Extension

I implemented `main()` to create a player as a `Character` and three NPCs using the `NPC` class. The program displayed their descriptions and presented an interactive menu that allowed the player to view their character or speak to the baker, villager, and guard. These interactions changed the player's health through the `take_damage()` and `heal()` methods. I also included input validation that rejected empty character names and handled invalid menu choices without terminating the game.

Finally, `main()` called both demonstration functions to display the namespace and copying examples after the player exited the game.