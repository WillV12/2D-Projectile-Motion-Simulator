import turtle


def space():
    from turtle import Shape, Screen, Turtle, Vec2D as Vec
    G = 8  # Gravitational constant
    NUM_LOOPS = int(input("How many steps should the simulation take?:\n"))  # Number of loops in the simulation.
    Ro_X = 0
    Ro_Y = -85
    Vo_X = int(input("What is the ships initial x velocity?:\n"))
    Vo_Y = int(input("What is the initial y velocity?:\n"))
    class GravSys:
        """Runs a gravity simulation on n-bodies."""

        def __init__(self):
            self.bodies = []
            self.t = 0
            self.dt = 0.001

        def sim_loop(self):
            """Loop bodies in a list through time steps."""
            for _ in range(NUM_LOOPS):  # Stops simulation after capsule splashdown.
                self.t += self.dt
                for body in self.bodies:
                    body.step()


    class Body(Turtle):
        """Celestial object that orbits and projects gravity field."""

        def __init__(self, mass, start_loc, vel, grav_sys, shape):
            super().__init__(shape=shape)
            self.gravsys = grav_sys
            self.penup()
            self.mass = mass
            self.setpos(start_loc)
            self.vel = vel
            grav_sys.bodies.append(self)
            turtle.hideturtle()
            self.pendown()

        def acc(self):
            """Calculate combined force on body and return vector components."""
            a = Vec(0, 0)
            for body in self.gravsys.bodies:
                if body != self:
                    r = body.pos() - self.pos()
                    a += (G * body.mass / abs(r) ** 3) * r  # Units: dist/time^2.
            return a

        def step(self):
            """Calculate position, orientation, and velocity of a body."""
            dt = self.gravsys.dt
            a = self.acc()
            self.vel = self.vel + dt * a
            self.setpos(self.pos() + dt * self.vel)
            if self.gravsys.bodies.index(self) == 2:  # Index 2 = CSM.
                rotate_factor = 0.0006
                self.setheading((self.heading() - rotate_factor * self.xcor()))
                if self.xcor() < -20:
                    self.shape('arrow')
                    self.shapesize(0.5)
                    self.setheading(105)

    def main():
        # Setup screen
        screen = Screen()
        screen.setup(width=1.0, height=1.0)  # For full-screen.
        screen.bgcolor('black')
        screen.title("Apollo 8 Free Return Simulation")

        grav_sys = GravSys()

        image_earth = 'earth_100x100.gif'
        screen.register_shape(image_earth)
        earth = Body(1000000, (0, -25), Vec(0, -2.5), grav_sys, image_earth)
        earth.pencolor('white')
        earth.getscreen().tracer(0, 0)

        image_moon = 'moon_27x27.gif'
        screen.register_shape(image_moon)
        moon = Body(32000, (344, 42), Vec(-27, 147), grav_sys, image_moon)
        moon.pencolor('gray')

        csm = Shape('compound')
        cm = ((0, 30), (0, -30), (30, 0))
        csm.addcomponent(cm, 'white', 'white')
        sm = ((-60, 30), (0, 30), (0, -30), (-60, -30))
        csm.addcomponent(sm, 'white', 'black')
        nozzle = ((-55, 0), (-90, 20), (-90, -20))
        csm.addcomponent(nozzle, 'white', 'white')
        screen.register_shape('csm', csm)


        ship = Body(1, (Ro_X, Ro_Y), Vec(Vo_X, Vo_Y), grav_sys, 'csm')
        ship.shapesize(0.2)
        ship.color('white')
        ship.getscreen().tracer(1, 0)
        ship.setheading(90)
        ship.pencolor('red')
        grav_sys.sim_loop()


    main()
