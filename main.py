import turtle
from turtle import Screen,Turtle
import pandas

screen = Screen()
screen.title("US game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
score = 0
is_game_on = True
data = pandas.read_csv("50_states.csv")
guess = []
not_guessed = []
while len(guess) < 50:
    answer = screen.textinput(title=f"{score}/50 state correct", prompt="What is another state name?").title()

    if answer in data["state"].tolist():
        guess.append(answer)
        info = data[data["state"] == answer]
        # print(info)
        turtle.goto(int(info.x.iloc[0]), int(info.y.iloc[0]))
        turtle.write(f"{answer}", align="center", font=("Arial", 8, "normal"))
    if answer == "Exit":

        for state in data.state.tolist():
            if state not in guess:
                not_guessed.append(state)
            data1 = pandas.DataFrame(not_guessed)
            data1.to_csv("missing_state.csv")
        #print(not_guessed)
        break







