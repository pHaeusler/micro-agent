from agent import agi

directory = "./app"

purpose = """A terminal based game
- the user must guess a number between 0-100
- the game will reply if the number is higher or lower
"""

agi.run(purpose, directory)
