# Pseudo-code:
# First, we define a function to get user input and validate it.
# If the input is wrong, we show an error and ask if they want to try again.
# If the user wants to try again, we repeat; otherwise, we exit.

# Then, we define a function to draw the tree:
# - We check if the depth is 0. If it's 0, we stop.
# - If it's not 0, we:
#     - Draw the main trunk in brown.
#     - For the left branches, color them green.
#     - For the right branches, color them dark green.
#     - We draw the branch, then go right and draw the right branch.
#     - Then, we go back and draw the left branch.
#     - After both branches, we go back to where we started.
#     - Each time, we make the branch shorter by multiplying by the reduction factor.
#     - We repeat this process for as many levels as the user chooses (based on depth).

# After drawing, we set up the turtle to:
# - Move fast and face upwards.
# - Set the background color to white for better visibility.

# Then, we ask the user for the following inputs:
# - The left branch angle,
# - The right branch angle,
# - The starting branch length,
# - The recursion depth,
# - The branch length reduction factor.

# Once we have the inputs, we move the turtle to the starting position and begin drawing the tree.

# Finally, we hide the turtle after drawing and finish.

import turtle

# Function to handle user input with validation
def get_valid_input(prompt, value_type, min_value=None, max_value=None):
    while True:
        try:
            user_input = value_type(input(prompt))
            if (min_value is not None and user_input < min_value) or (max_value is not None and user_input > max_value):
                print(f"Error: Please enter a value between {min_value} and {max_value}.")
                continue
            return user_input
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        
        retry = input("Would you like to try again? (y/n): ").lower()
        if retry == 'n':
            print("Exiting the program.")
            exit()

# Recursive function to draw the tree
def draw_tree(branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0:  # If depth is 0, stop drawing
        return
    else:
        if depth == 6:  # If we are drawing the main trunk, color it brown
            turtle.pencolor("brown")
        else:
            if depth % 2 == 0:  # For left branches, color it green
                turtle.pencolor("green")
            else:  # For right branches, color it dark green
                turtle.pencolor("dark green")

        turtle.forward(branch_length)  # Draw the current branch

        turtle.left(angle_right)  # Turn right for the right branch
        draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

        turtle.right(angle_right + angle_left)  # Return to the starting position for left branch

        draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

        turtle.left(angle_left)  # Return to the original position
        turtle.backward(branch_length)  # Go back to the trunk

# Setup the turtle screen
def setup_turtle():
    turtle.speed(0)  # Make the turtle move fast
    turtle.left(90)  # Start facing upwards
    turtle.bgcolor("white")  # Set background color to white

def main():
    # Get valid inputs with error handling
    angle_left = get_valid_input("Enter the left branch angle (in degrees): ", float, 0, 180)
    angle_right = get_valid_input("Enter the right branch angle (in degrees): ", float, 0, 180)
    start_length = get_valid_input("Enter the starting branch length (in pixels): ", float, 1)
    depth = get_valid_input("Enter the recursion depth: ", int, 1, 10)
    reduction_factor = get_valid_input("Enter the branch length reduction factor (as a decimal, e.g., 0.7 for 70%): ", float, 0.1, 1.0)

    # Setup turtle window and appearance
    setup_turtle()

    # Move the turtle to the starting position
    turtle.penup()
    turtle.setpos(0, -200)  # Move the turtle to a good spot for starting
    turtle.pendown()

    # Start drawing the tree based on the inputs
    draw_tree(start_length, angle_left, angle_right, depth, reduction_factor)

    # Hide the turtle after drawing
    turtle.hideturtle()

    # Finish drawing
    turtle.done()

if __name__ == "__main__":
    main()

