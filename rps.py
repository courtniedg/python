import random
import tkinter
root = tkinter.Tk()
root.title("Rock-Paper-Scissors")
def newgame():
    # delete label
    results.destroy()
    # make buttons active again
    rock["state"] = "normal"
    paper["state"] = "normal"
    scissors["state"] = "normal"
    ng.destroy()
def playgame(choice):
    global results, ng
    cp_choice = random.choice(["rock", "paper", "scissors"])
    message = "You chose {} and the computer chose {}. ".format(choice, cp_choice)
    if cp_choice == choice:
        message += "It's a tie!"
    elif choice == "rock":
        if cp_choice == "paper":
            message += "You lose!"
        else:
            message += "You win!"
    elif choice == "paper":
        if cp_choice == "scissors":
            message += "You lose!"
        else:
            message += "You win!"
    elif choice == "scissors":
        if cp_choice == "rock":
            message += "You lose!"
        else:
            message += "You win!"
    #print(message)
    results = tkinter.Label(root,
                            font = ("Helvetica", 18),
                            text = message)
    results.grid(row = 1, column = 0, columnspan = 3)
    rock["state"] = "disabled"
    paper["state"] = "disabled"
    scissors["state"] = "disabled"
    ng = tkinter.Button(root,
                        padx=10,
                        pady=10,
                        font=('Helvetica', '26'),
                        text = "New Game",
                        command = newgame)
    ng.grid(row = 2, column = 1)
    return message
rock = tkinter.Button(root,
                      text = "Rock",
                      fg = "darkred",
                      padx = 40,
                      pady = 10,
                      font = ('Helvetica', '26'),
                      background = "red",
                      command = lambda : playgame("rock"))
rock.grid(row = 0, column = 0)
paper = tkinter.Button(root,
                      text = "Paper",
                      fg = "darkgreen",
                      padx = 40,
                      pady = 10,
                      font = ('Helvetica', '26'),
                      background = "green",
                      command = lambda : playgame("paper"))
paper.grid(row = 0, column = 1)
scissors = tkinter.Button(root,
                      text = "Scissors",
                      fg = "darkblue",
                      padx = 40,
                      pady = 10,
                      font = ('Helvetica', '26'),
                      background = "blue",
                      command = lambda : playgame("scissors"))
scissors.grid(row = 0, column = 2)
