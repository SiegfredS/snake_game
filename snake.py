from turtle import Turtle


class Snake:
    def __init__(self,
                 params=("white", 5),
                 speed=10,
                 move_distance=10):
        self.color = params[0]
        self.length = params[1]
        self.segments = []
        self.speed = speed
        self.move_distance = move_distance
        # We start at (x,y) = (0,0) however for every length of snake we move leftwards by -20
        self.starting_position =[(-20*x, 0) for x in range(0, self.length)]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(self.length):
            self.create_new_segment(starting_pos_index=i)

    def create_new_segment(self,
                           starting_pos_index):
        """
        creates the snake using individual square turtles. Appends it to the segment of the snake such that
        segment[0] is the head and segment[-1] is the tail.
        :return:
        """
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(self.color)
        new_segment.speed(self.speed)
        new_segment.goto(self.starting_position[starting_pos_index])
        self.segments.append(new_segment)

    def move(self):
        # Starting with the tail to head move to next coordinate
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
        #Head moves forward
        self.head.forward(self.move_distance)

    def snake_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        else:
            pass

    def snake_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        else:
            pass

    def snake_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        else:
            pass

    def snake_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        else:
            pass

    def has_collided(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        else:
            return False

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(self.color)
        new_segment.speed(self.speed)
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
