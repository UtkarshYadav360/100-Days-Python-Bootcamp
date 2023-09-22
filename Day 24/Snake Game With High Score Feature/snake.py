from turtle import Turtle

# constants of the snake
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# creating the snake class
class Snake:
    def __init__(self):
        self.segments = []  # segments of the snake will be stored here
        self.create_snake()  # method to create the snake
        self.snake_head = self.segments[0]  # snake head

    def create_snake(self):
        """Add the segments to form a snake."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Takes position and adds the segment to the snake."""
        new_segment = Turtle(shape="square")
        new_segment.color("blueviolet")
        new_segment.penup()
        # setting the position of each segment of the snake
        new_segment.goto(position)
        self.segments.append(new_segment)  # appending all the segments to a list

    def extend_snake(self):
        """Extend the snake by one segment when snake hits the food."""
        self.add_segment(
            self.segments[-1].position()
        )  # add the segment to the last position of the snake

    def reset(self):
        """Resets the snake position when the snake hits the wall or collides with it's own body."""
        # moving previous snake segments to a very far position on the screen, So they cannot be seen
        for segs in self.segments:
            segs.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def move(self):
        """Moves the snake."""
        # loop iterates to the number of segments in the snake body in reverse order
        for segment_number in range(len(self.segments) - 1, 0, -1):
            # making new x-coordinates and y-coordinates for the snake segments
            new_x_pos = self.segments[segment_number - 1].xcor()
            new_y_pos = self.segments[segment_number - 1].ycor()
            # changing the current coordinates of the snake segments
            self.segments[segment_number].goto(new_x_pos, new_y_pos)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves snake upwards."""
        # checks if the snake head is not in downward direction using the "heading()"
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """Moves snake downwards."""
        # checks if the snake head is not in upward direction using the "heading()"
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        """Moves snake left."""
        # checks if the snake head is not in right direction using the "heading()"
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """Moves snake right."""
        # checks if the snake head is not in left direction using the "heading()"
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
