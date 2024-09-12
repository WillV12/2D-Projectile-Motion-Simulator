"""Used to run the 2-d projectile simulation program"""


def projectile():
    # Importing these modules to plot and calculate data
    import turtle
    import math
    import matplotlib.pyplot as plt

    """This used to test if a given value is negative"""
    def neg_test(num):
        c = 5 + num
        if c > 5:
            return False
        elif c < 5:
            return True
    # Initializing variables and getting input for initial conditions
    plx = []
    ply = []
    dt = 0
    # Initial conditions input
    ivx = input("What is the initial x velocity?:\n")
    ivy = input("What is the initial y velocity?:\n")
    h = input("What is the initial height?:\n")
    angle = input("What is the angle you are throwing at?:\n")
    if ivx.isnumeric() is False or ivy.isnumeric() is False or h.isnumeric() is False or angle.isnumeric() is False:
        raise Exception("One of the inputs is incorrect")
    else:
        ivx = int(ivx)
        ivy = int(ivy)
        h = int(h)
        angle = int(angle)

    px = []
    py = []
    # Calculates initial vectors and initializes gravity/acceleration
    a = 9.81
    vx = ivx * math.cos(math.radians(angle))
    vy = ivy * math.sin(math.radians(angle))
    time = []
    vxl = []
    vyl = []
    # Calculates velocities, new conditions, and appends data 10000 times
    for i in range(0, 10000):
        time.append(dt)
        ix = ivx + vx * dt
        iy = ivy + vy * dt
        vxl.append(ix)
        vyl.append(iy)
        vy = vy - 0.5 * a * dt
        pos_x = ix * dt
        posy = iy * dt
        # This is used to scale the trajectory down so that it is visible on the screen
        px.append(pos_x/20)
        py.append(posy/20)
        dt += .0001
    # Initializes and sets up the screen for the turtle window
    turtle.title("2-D Projectile Motion")
    turtle.setup(width=1.0, height=1.0)
    turtle.screensize(10000, 10000)
    turtle.hideturtle()
    turtle.tracer(1, 1)
    # Moves turtle to starting position
    turtle.speed(0)
    turtle.penup()
    h = h/20
    turtle.pencolor('Black')
    turtle.goto(-628, -304 + h)
    turtle.pendown()
    w = ''
    for s in range(len(px)):
        # Moves turtle forward based on x component
        turtle.forward(px[s])
        # Test whether the value is negative to determine whether to go left or right and then return facing forward
        if neg_test(py[s]) is False:
            turtle.left(90)
            turtle.forward(py[s])
            turtle.right(90)
        elif neg_test(py[s]) is True:
            x = float(py[s])
            x *= -1
            turtle.right(90)
            turtle.forward(x)
            turtle.left(90)
            # Checks to see if the y cor is at or below the set "ground level" and if so, returns # of steps and breaks
        if turtle.ycor() <= -304 and s > 5:
            w = s
            break
    # Up-scales the x and y components for graphing and showing the data to the user
    # Also will make the negative values in y velocities and components to positive for the same reasons
    for b in range(len(px)):
        j = px[b] * 20
        plx.append(j)
    for n in range(len(py)):
        if neg_test(py[n]) is True:
            o = py[n] * -1
        else:
            o = py[n]
        j = o * 20
        ply.append(j)
    vec_y = []
    for p in range(len(vyl)):
        if neg_test(vyl[p]) is True:
            k = vyl[p] * -1
        else:
            k = vyl[p]
        vec_y.append(k)
    # Prints out data for user
    # [:w] is used to slice the lists to only show used data and not the other redundant calculations
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Simulation steps = {le}\nSteps Used = {te}\nTotal simulation time = {f}".format(le=len(time), te=w, f=time[w]
                                                                                           ))
    print("Time =", time[:w + 1])
    print("x component =", plx[:w + 1])
    print("y component =", ply[:w + 1])
    print("x velocities =", vxl[:w + 1])
    print("y velocities =", vec_y[:w + 1])
    # Initializes & configures graph to have two axes
    # Sets limits for graph for proper scaling
    # Plots data that was used during simulation and labels them accordingly
    plt.subplot(2, 1, 1)
    plt.plot(plx[:w + 1], py[:w + 1], label="x and y Positions in relation to one another")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.subplot(2, 1, 2)
    plt.plot(time[:w + 1], vxl[:w + 1], label="X-velocities")
    plt.plot(time[:w + 1], vec_y[:w + 1], label="Y-Velocities")
    plt.plot(time[:w + 1], px[:w + 1], label="X-Components")
    plt.plot(time[:w + 1], ply[:w + 1], label="Y-Components")
    # Labels axes accordingly
    plt.xlabel("Time")
    plt.ylabel("Velocity/Y component")
    # Initializes legend and title
    plt.legend()
    # Shows graph
    plt.show()
