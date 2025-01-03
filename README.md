# PokerReviewTool
Pokerstars Review Tool reading a users Pokerstars hand history (.txt file), parses it to create actions and displays the history inside a gui by recreating a poker table.
A basic gui to read a hand history and start the reviewing process is created using tkinter in a MVC architecture.

![screenshot_resized](https://github.com/user-attachments/assets/8eeb629d-0b51-4d6b-95b2-42de784be89f)

By clicking on "Review..." a pygame surface representing a poker table is started. Here the user can see his played hand step by step by using the arrow keys. 

![Screenshot 2024-12-29 210143](https://github.com/user-attachments/assets/59acc5c8-4999-4211-a724-46c1bffe58a2)
(Player names have been anonymized since actual hand histories have been read here)

Core of the parsing process are specific actions (inside action.py) and an action registry. The blueprint of each action is given by the abstract BaseAction. An Action constist of a pattern, a constructor and an "execute" method. The pattern is used to parse the right action to the corresponding line of the handhistory. The constructor uses groups of the matched regex as parameter to create class attributes. The execute method takes the pygame main surface as argument to create a pygame action. Creating a new Action is fairly easy, since the blueprint of the BaseAction can be followed. 

Status:
A first version has been created making it possible to review basic Pokerstars hands. Further patterns are necessary to match all actions given in the hand history txt file. The execution method has only been created for the most important actions. 
