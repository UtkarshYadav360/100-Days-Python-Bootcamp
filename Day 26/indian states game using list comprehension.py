import turtle
import pandas


# making the screen
screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(height=700, width=800)
# adding image to the background turtle window
image = "indian_states_image.gif"
screen.addshape(image)
turtle.shape(image)


# reading the csv file
data = pandas.read_csv("states_name.csv")
all_states = data.states.to_list()


# states guessed by the user will be stored here
guessed_states = []

# number of states guessed by the user
guessed_states_count = 0

# loop runs till the user guesses all the states
while len(guessed_states) < 29:
    # asking for the state input
    state_input = screen.textinput(
        title=f"{guessed_states_count}/29 States", prompt="What's another state name?"
    ).title()

    # checking if the user is not entering the same state again and again
    if state_input in all_states and state_input not in guessed_states:
        guessed_states_count += 1

    # stops the game and adds all the states that are not entered by the user to a file called "states_to_learn.csv"
    if state_input == "Exit":
        missing_states = [
            state for state in all_states if state_input not in guessed_states
        ]
        # making a csv file for the missing states
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    # checking if the state entered by the user is in the 29_states
    if state_input in all_states:
        guessed_states.append(state_input)
        # getting the data of the state entered by the user
        state_data = data[data.states == state_input]
        # making turtle to write the state name in the correct place on the map
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        t.write(state_input)
