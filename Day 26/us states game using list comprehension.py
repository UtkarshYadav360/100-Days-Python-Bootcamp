import turtle
import pandas

# PROJECT 25 :
# US STATES GAME


# making the screen
screen = turtle.Screen()
screen.title("US States Game")
# adding image to the turtle window background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# states guessed by the user will be stores here
guessed_states = []

# number of states guessed by the user
guessed_states_count = 0


# reading the csv file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


# loop runs till the user guesses all the state names
while len(guessed_states) < 50:
    # asking for the state input
    state_input = screen.textinput(
        title=f"{guessed_states_count}/50 States Guessed",
        prompt="What's another state name?",
    ).title()

    # checking if the user is not entering the same state again and again
    if state_input in all_states and state_input not in guessed_states:
        guessed_states_count += 1

    # stops the game and add all the states that are not guessed by the user to the file called "states_to_learn.csv"
    if state_input == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # making a csv file for the missing states
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    # checking if the state guessed by the user is in the "50_states.csv"
    if state_input in all_states:
        guessed_states.append(state_input)
        # getting the data of the state entered by the user
        state_data = data[data.state == state_input]
        # making turtle to write the state name in the correct place on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # THIS LINE WILL ALSO WORK IN FUTURE
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))

        # THIS LINE WILL WORK FOR NOW, BUT NOT WORK IN FUTURE UPDATE
        # t.goto(int(state_data.x), int(state_data.y))
        t.write(state_input)
