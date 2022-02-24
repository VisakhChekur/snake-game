from turtle import Turtle, Screen
screen = Screen()
STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Deals with the attributes of the snake and its movement."""

    def __init__(self):
        """Initializes the attributes of the snake."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the body of the snake."""
        for position in STARTING_POSITIONS:
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1500, 1500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Function to move and control the snake."""

        def face_up():
            """Makes the snake face up when 'up' arrow key is pressed."""
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def face_down():
            """Makes the snake face down when 'down' arrow is pressed."""
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def face_right():
            """Makes the snake face right when the 'right' arrow is pressed."""
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

        def face_left():
            """Makes the snake face left when the 'left' arrow is pressed."""
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        # Keeps the snake moving in the direction it is already
        # moving
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

        # will change the direction of the snake based on the arrow key
        # pressed
        screen.listen()
        screen.onkey(key='Up', fun=face_up)
        screen.onkey(key='Down', fun=face_down)
        screen.onkey(key='Left', fun=face_left)
        screen.onkey(key='Right', fun=face_right)

    def add_segment(self):
        """Adds a new segment but its position is at home (0,0). This new
        segment is hidden so the user doesn't see it while it moves to the
        correct position at the end of the snake."""
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.segments.append(segment)

    def move_through_wall(self):
        """Makes the snake 'move' through the walls."""
        x_coordinate = self.head.xcor()
        y_coordinate = self.head.ycor()
        heading = self.head.heading()
        if heading == 0 or heading == 180:
            new_x_coordinate = -1 * x_coordinate
            self.head.goto(new_x_coordinate, y_coordinate)
        elif heading == 90 or heading == 270:
            new_y_coordinate = -1 * y_coordinate
            self.head.goto(x_coordinate, new_y_coordinate)
