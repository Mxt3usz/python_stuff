"""Fireworks.

This module implements a fireworks that is drawn onto a tkinter canvas.

Original Lecture:
    http://www.informatik.uni-freiburg.de/~ki/teaching/ws1617/info1/lecture.html

Authors:
    Tim Schulte
    Thorsten Engesser

Rewritten by:
    Hannes Saffrich

Version:
    WS 2020/21

"""

import tkinter as tk

from time        import time
from random      import choice, uniform
from math        import sin, cos
from dataclasses import dataclass

## Basic Geometric Shapes ######################################################

@dataclass
class TkShape:
    """Common base class for geometric shapes like circles, squares and
    triangles, which can be drawn on the `tk.Canvas` of a window.
    """

    def add_to_canvas(self, cv: tk.Canvas):
        """Add this shape to a canvas. Specific shapes, which inherit from
        TkShape, are expected to override this method.  If we add a shape to a
        canvas, the Tk library gives us an id, which can be used to remove the
        shape again. We store this id in the `cid` attribute, such that the
        `remove_from_canvas` method can remove it again.
        """
        pass

    def remove_from_canvas(self, cv: tk.Canvas):
        """Delete this shape from the canvas. Works the same for any shape."""
        if self.cid != None:
            cv.delete(self.cid)
            self.cid = None

@dataclass
class Circle(TkShape):
    """Class for a circle shape.

    The geometry and appearance of the circle is determined by its position on
    the canvas, its radius and its color.

    Attributes:
        pos_x: The x-coordinate of the circle's center on the canvas.
        pos_y: The y-coordinate of the circle's center on the canvas.
        radius: The radius of the circle.
        color: The color of the circle.
    """
    pos_x:  float
    pos_y:  float
    radius: float
    color:  str

    def add_to_canvas(self, cv: tk.Canvas):
        """Draw the circle on the canvas."""
        self.cid = cv.create_oval(
            self.pos_x - self.radius,
            self.pos_y - self.radius,
            self.pos_x + self.radius,
            self.pos_y + self.radius,
            fill = self.color)

@dataclass
class Square(TkShape):
    """Class for a square shape.

    The geometry and appearance of the square is determined by its position
    of it's center on the canvas, its size and its color.

    Attributes:
        pos_x: The x-coordinate of the square's center on the canvas.
        pos_y: The y-coordinate of the square's center on the canvas.
        size: The size of the square.
        color: The color of the square.
    """
    pos_x: float
    pos_y: float
    size:  float
    color: str

    def add_to_canvas(self, cv: tk.Canvas):
        """Draw the square on the canvas."""
        self.cid = cv.create_rectangle(
            self.pos_x - self.size,
            self.pos_y - self.size,
            self.pos_x + self.size,
            self.pos_y + self.size,
            fill = self.color)

@dataclass
class Triangle(TkShape):
    """Class for a triangle shape.

    The geometry and appearance of the circle is determined by the position of
    its corners on the canvas and its color.

    Attributes:
        pos_x1: The x-coordinate of the object's first corner.
        pos_y1: The y-coordinate of the object's first corner.
        pos_x2: The x-coordinate of the object's second corner.
        pos_y2: The y-coordinate of the object's second_ corner.
        pos_x3: The x-coordinate of the object's third corner.
        pos_y3: The y-coordinate of the object's third corner.
        color: The color of the circle.
    """
    pos_x1: float
    pos_y1: float
    pos_x2: float
    pos_y2: float
    pos_x3: float
    pos_y3: float
    color:  str

    def add_to_canvas(self, cv: tk.Canvas):
        """Draw the triangle on the canvas."""
        self.cid = cv.create_polygon(
            self.pos_x1, self.pos_y1,
            self.pos_x2, self.pos_y2,
            self.pos_x3, self.pos_y3,
            fill = self.color)

## Physics #####################################################################

@dataclass
class PhysicsObject:
    """Common base class for objects, which are influenced by physics and can be
    drawn on a screen.

    Attributes:
        pos_x: The x-coordinate of the object's position on the surface.
        pos_y: The y-coordinate of the object's position on the surface.
        vel_x: How fast the object moves horizontally.
        vel_y: How fast the object moves vertically.
    """
    pos_x: float
    pos_y: float
    vel_x: float
    vel_y: float

    def update(self, dt: float, gravity: float):
        """Simulate what physically happens to the object in the next `dt`
        seconds. The object's position is changed according to its velocity,
        which in turn is changed according to an external `gravity` constant."""
        self.pos_x += dt * self.vel_x
        self.pos_y += dt * self.vel_y
        self.vel_y += dt * gravity

    def render(self) -> list[TkShape]:
        """Describes how and where to draw this object by returning a list of
        shapes. Subclasses are expected to override this method."""
        return []

    def is_alive(self) -> bool:
        """Check if the object ist still alive. Overwritten by derived
        classes. PhysicsObjects which are dead will be removed from the
        simulation for performance reasons."""
        return True

## Particles ###################################################################

@dataclass
class Particle(PhysicsObject):
    """Common base class for fireworks particles, e.g. sparks flying off a
    rocket or coming out of a volcano.

    Any Particle is also a PhysicsObject, since they fly around and can be seen,
    but they also have a life time, after which they burn out, and a certain
    color and size. The precise shape of a Particle is determined by its
    subclasses below.

    Arguments:
        remaining_time: How many seconds until this particle is burnt out.
        color: The color of the particle.
        size: The size of the particle.
    """
    remaining_time: float
    color: str
    size: float

    def update(self, dt: float, gravity: float):
        """A particle is influenced by physics, just like any other
        PhysicsObject, but additionally the passed time `dt` influences the
        `remaining_time` before the particle burns out."""
        super().update(dt, gravity)
        self.remaining_time -= dt

    def is_alive(self):
        """Check if the particle is still alive or already burned out."""
        return self.remaining_time >= 0.0

@dataclass
class CircularParticle(Particle):
    """A Particle which has the shape of a Circle."""
    def render(self) -> list[TkShape]:
        """Draw the particle as a single circle shape."""
        return [
            Circle(
                pos_x = self.pos_x,
                pos_y = self.pos_y,
                radius = self.size,
                color = self.color
            )
        ]

@dataclass
class SquareParticle(Particle):
    """A Particle which has the shape of a Square."""
    def render(self) -> list[TkShape]:
        """Draw the particle as a single square shape."""
        return [
            Square(
                pos_x = self.pos_x,
                pos_y = self.pos_y,
                size = self.size,
                color = self.color
            )
        ]

@dataclass
class TriangleParticle(Particle):
    """A Particle which has the shape of a Triangle."""
    def render(self) -> list[TkShape]:
        """Draw the particle as a single triangle shape."""
        return [
            Triangle(
                pos_x1 = self.pos_x - self.size,
                pos_y1 = self.pos_y - self.size,
                pos_x2 = self.pos_x + self.size,
                pos_y2 = self.pos_y - self.size,
                pos_x3 = self.pos_x,
                pos_y3 = self.pos_y + self.size,
                color = self.color
            )
        ]

## Fireworks ###################################################################

@dataclass
class Firework(PhysicsObject):
    """Common base class for a Firework maintaining a list of Particles.

    Classes inheriting from a Firework, like our Volcano, are expected to
    override the `update` method to dynamically spawn new particles.

    Attributes:
        particles: list of the currently burning Particles, which belong to this
                   firework. At the beginning this should usually be the empty
                   list, because fireworks tend to spawn their own particles.
    """
    particles: list[Particle]

    def update_particles(self, dt: float, gravity: float):
        # Update all particles.
        for p in self.particles:
            p.update(dt, gravity)

        # Remove dead particles.
        alive_particles = []
        for p in self.particles:
            if p.is_alive():
                alive_particles += [p]
        self.particles = alive_particles

    def update(self, dt: float, gravity: float):
        # Simulate the physics for the fireworks object itself.
        super().update(dt, gravity)

        # Simulate the physics for all its particles.
        self.update_particles(dt, gravity)

    def render(self) -> list[TkShape]:
        """A Firework is rendered by rendering all its particles. Subclasses may
        want to override this method to render additional shapes for the
        firework body."""
        shapes = []
        for p in self.particles:
            shapes += p.render()
        return shapes

@dataclass
class Volcano(Firework):
    """A Volcano is a Firework, which continuously emits colored particles and
    has a body that looks like a large triangle.

    Attributes:
        particles_per_second: the number of particles to spawn per second.
        colors: the colors of the particles to spawn. Since our Volcano is
            pretty fancy, it spawns particles of different colors as time passes.
        age: how many seconds the Volcano exists.
        _particles_to_spawn: how many fractions of a particle we still need to
            spawn. This is an implementation detail from the physics simulation:
            if the time steps in `update` are very small, then it could be the
            case, that in each time step we would need to spawn 0.001 particles,
            so we need to accumulate those amounts, such that we notice when it
            goes beyond 1.0 and we actually have to spawn a new particle.
    """
    particles_per_second: float      = 100.0
    colors:               tuple[str] = ("red", "green", "silver", "gold")
    age:                  float      = 0.0
    _particles_to_spawn:  float      = 0.0

    def render(self) -> list[TkShape]:
        """A Volcano is drawn as a big triangle with particles coming out of
        the top."""

        # Render the current particles.
        shapes = super().render()

        # Render the volcano itself as one big triangle.
        shapes += [
            Triangle(
                pos_x1 = self.pos_x - 12, pos_y1 = self.pos_y + 12,
                pos_x2 = self.pos_x + 12, pos_y2 = self.pos_y + 12,
                pos_x3 = self.pos_x,      pos_y3 = self.pos_y - 12,
                color = "orange"
            )
        ]

        return shapes

    def update(self, dt: float, gravity: float):
        """Simulate the physics of a Volcano. This will continuously spawn new
        particles and animate them until they burn out.
        """

        # We consider a Volcano to be stationary, so we only simulate the
        # physics of the particles but not of the Volcano itself. Otherwise,
        # we would use `super().update(dt, gravity)` here instead.
        super().update_particles(dt, gravity)

        self.age += dt

        # Calculate how many particles need to be spawned
        self._particles_to_spawn += self.particles_per_second * dt
        color = self.colors[int(self.age / 3) % len(self.colors)]
        while self._particles_to_spawn >= 1.0:
            # Randomly choose which particle to spawn
            TheParticle = choice([SquareParticle, TriangleParticle, CircularParticle])

            # Randomly choose angle and speed of the particle
            angle = uniform(-0.25, 0.25)
            speed = -uniform(80.0, 120.0)

            # Calculate velocity
            vel_x = sin(angle) * speed
            vel_y = cos(angle) * speed

            # Create the new particle
            self.particles.append(
                TheParticle(
                    size=2.0,
                    pos_x=self.pos_x, pos_y=self.pos_y,
                    vel_x=vel_x, vel_y=vel_y,
                    remaining_time=5.0,
                    color=color
                )
            )

            # Now we have one less particle to spawn
            self._particles_to_spawn -= 1.0

## Simulation ##################################################################

def simulate(window: tk.Tk,
             cv: tk.Canvas,
             old_time: float,
             objects: list[PhysicsObject],
             gravity: float):
    # Calculate the time that has passed since the last call of this function
    new_time = time()
    dt = new_time - old_time

    # Simulate physics for each of our PhysicsObject and retrieve the TkShapes
    # which describe how and where the objects should be drawn.
    shapes = []
    for o in objects:
        o.update(dt, gravity)
        shapes += o.render()

    # Draw the shapes of all objects on the window's canvas.
    for s in shapes:
        s.add_to_canvas(cv)
    cv.update() # This actually draws the currently added shapes.
    for s in shapes:
        s.remove_from_canvas(cv)

    # Let the Tk library handle key presses and mouse clicks and, if the window
    # hasn't been closed, call `simulate(window, cv, new_time, objects, gravity)`
    # again to simulate the next point in time.
    window.after(0, simulate, window, cv, new_time, objects, gravity)

if __name__ == '__main__':
    # Create a new window.
    window = tk.Tk()

    # Register a function `close`, which closes the window, if [ESC] key got
    # pressed or the window's close button was clicked.
    def close(*ignore):
        window.quit()
    window.bind('<Escape>', close)
    window.protocol("WM_DELETE_WINDOW", close)

    # Create a canvas on the window to draw on and add background colors.
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.create_rectangle(0, 0, 800, 600, fill="midnight blue")  # sky
    canvas.create_rectangle(0, 450, 800, 600, fill="gray11")       # ground
    canvas.pack()

    # Initialize some fireworks
    v1 = Volcano(
        pos_x=400, pos_y=500,
        vel_x=0,   vel_y=0,
        particles_per_second=100,
        colors=("red", "green", "silver", "gold"),
        particles=[]
    )
    objects = [v1]
    gravity = 30.0  # Feel free to play with this value.

    # Register the `simulate` function to be called in the window's `mainloop`
    # after 0ms. If we would run simulate directly in an endless loop,
    # we wouldn't be able to start the mainloop below, which also listens
    # to mouse and keyboard events.
    window.after(0, simulate, window, canvas, time(), objects, gravity)

    # Enter the mainloop, which listens for mouse and keyboard events, and
    # repeatedly runs our `simulate` function.
    window.mainloop()
