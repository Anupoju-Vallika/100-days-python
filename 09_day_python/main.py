import turtle
import pandas

# Setup screen
screen = turtle.Screen()
screen.title("India States Game")

# Load India map
image = "Blank-India-Map.gif"
screen.addshape(r"C:\Users\Vallika\OneDrive\Desktop\21 days code\21-days-100_pythonproject\09_day_python\Blank-India-Map.gif")
turtle.shape(image)

# Load states data
data = pandas.read_csv("india_states_coordinates.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 29:   # 29 states (or update if including UTs)
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/29 States Correct",
        prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
