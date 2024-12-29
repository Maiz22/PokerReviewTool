# PokerReviewTool
Pokerstars Review Tool reading a users Pokerstars hand history (.txt file), parses it to create actions and displays the history inside a gui by recreating a poker table.
A basic gui to read a hand history and start the reviewing process is created using tkinter in a MVC architecture.

<img src="https://private-user-images.githubusercontent.com/114342435/399185362-17865502-1c4d-4b79-84a1-14b22b193edf.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzU1MDQyNTMsIm5iZiI6MTczNTUwMzk1MywicGF0aCI6Ii8xMTQzNDI0MzUvMzk5MTg1MzYyLTE3ODY1NTAyLTFjNGQtNGI3OS04NGExLTE0YjIyYjE5M2VkZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMjI5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTIyOVQyMDI1NTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNTA5ZjkyNzQ3ZGJiYmVmZDY0NTczZDNmZjY2ZGIxMTdlNjM0MDAwOGNlNWQ2NTE1ZjI0NmEyMzUwMWQ4ZGUzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.6Y-dY2mjHL_iX2Tt_qHKVzgIQyAKYGzGI4PY1TZ4INo" alt="Screenshot 2024-12-29 212100" style="width: 500px;">

By clicking on "Review..." a pygame surface representing a poker table is started. Here the user can see his played hand step by step by using the arrow keys. 
![Screenshot 2024-12-29 210143](https://github.com/user-attachments/assets/59acc5c8-4999-4211-a724-46c1bffe58a2)
(Player names have been anonymized since actual hand histories have been read here)

Core of the parsing process are specific actions (inside action.py) and an action registry. The blueprint of each action is given by the abstract BaseAction. An Action constist of a pattern, a constructor and an "execute" method. The pattern is used to parse the right action to the corresponding line of the handhistory. The constructor uses groups of the matched regex as parameter to create class attributes. The execute method takes the pygame main surface as argument to create a pygame action. Createing a new Action is fairly easy, since the blueprint of the baseaction can be followed. 

Status:
A first version has been created making it possible to review basic Pokerstars hands. Further patterns are necessary to match all actions given in the hand history txt file. The execution method has only been created for the most important actions. 
