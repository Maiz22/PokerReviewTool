# PokerReviewTool
The PokerStars Review Tool reads a user's PokerStars hand history (stored as a .txt file), parses it to extract actions, and displays the history within a graphical interface by recreating a virtual poker table. A basic GUI, developed using tkinter with an MVC architecture, serves as the starting point for reviewing hands.

![screenshot_resized](https://github.com/user-attachments/assets/8eeb629d-0b51-4d6b-95b2-42de784be89f)

### Hand Review Interface
Upon clicking "Review..." in the tkinter GUI, a pygame window opens, simulating a poker table. Here, users can review their played hands step by step using the arrow keys for navigation.

![Screenshot 2024-12-29 210143](https://github.com/user-attachments/assets/59acc5c8-4999-4211-a724-46c1bffe58a2)
(Player names have been anonymized since actual hand histories have been read here)

### Parsing and Actions
The core of the tool’s parsing functionality lies in its modular action-handling system, defined within action.py. Actions are registered in an action registry and are based on the abstract BaseAction class, which serves as their blueprint.
Each action consists of three key components:
- Pattern: A regex pattern used to identify and match the corresponding line in the hand history file.
- Constructor: Creates class attributes by extracting values from the regex match groups.
- Execute Method: Takes the pygame main surface as input to visually render the action on the poker table.
Adding new actions is straightforward by following the blueprint defined in BaseAction. 

Status:
A first version has been created making it possible to review basic Pokerstars hands. Further patterns are necessary to match all actions given in the hand history txt file. The execution method has only been created for the most important actions. 
