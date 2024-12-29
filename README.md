# PokerReviewTool
Pokerstars Review Tool reading a users Pokerstars hand history (.txt file), parses it to create actions and displays the history inside a gui by recreating a poker table.
A basic gui to read a hand history and start the reviewing process is created using tkinter in a MVC architecture.
![image](https://github.com/user-attachments/assets/069e2968-eb38-420f-a58c-26d561fef6a6)![Screenshot 2024-12-29 205801](https://github.com/user-attachments/assets/b559f8c0-adee-4c7f-a92a-cc3ab4917295
By clicking on "Review..." a pygame surface representing a poker table is started. Here the user can see his played hand step by step by using the arrow keys. 
![Screenshot 2024-12-29 210143](https://github.com/user-attachments/assets/59acc5c8-4999-4211-a724-46c1bffe58a2)
(Player names have been anonymized since actual hand histories have been read here)

Core of the parsing process are specific actions (inside action.py) and an action registry. The blueprint of each action is given by the abstract BaseAction. An Action constist of a pattern, a constructor and an "execute" method. The pattern is used to parse the right action to the corresponding line of the handhistory. The constructor uses groups of the matched regex as parameter to create class attributes. The execute method takes the pygame main surface as argument to create a pygame action. Createing a new Action is fairly easy, since the blueprint of the baseaction can be followed. 

Status:
A first version has been created making it possible to review basic Pokerstars hands. Further patterns are necessary to match all actions given in the hand history txt file. The execution method has only been created for the most important actions. 
