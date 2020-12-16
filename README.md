# Pythonic-Reactive

NOTE: THIS IS STILL BEING DEVELOPED AND IS THEREFORE NOT RECOMMENDED FOR ANY
SERIOUS DEVELOPMENT AT THIS TIME. TEST COVERAGE IS INCOMPLETE AND FEATURES
ARE CHANGING!

Pythonic-Reactive contains reactive programming components developed
for both the [qork](https://github.com/flipcoder/qork) engine and the
PyWeek29 game [Butterfly Destroyers](https://github.com/pythonixcoders/pyweek29.git).

It's main features are:
- Signals, slots, and connections
- Reactive variables (Variables w/ change listeners)
- Lazy variables (Variables that observe reactive or other lazy variables)
- Reactive timer system with interpolation and easing
- Utility functions that make working with these more "pythonic"

## Basic Features

### Signal

```
sig = Signal()
sig += lambda: print('hello ', end='')
sig += lambda: print('world')
sig() # hello world
```

### Slots

```
# Make a signal

sig = Signal()

# Connect some slots (Note this is different from the above Signal example)

hello += sig.connect(lambda: print('hello ', end=''))
world += sig.connect(lambda: print('world'))

sig() # hello world

# let's remove hello slot

hello.disconnect()

sig() # world

# here's another way to remove a slot

sig -= world

# or...

del world

# Node: The above `del` relies on the garbage collector, which is not fully reliable.

```

### Reactive

Reactive variables are paired with an on_change signal.

```
x = Reactive(1)

x += lambda x: print('x is now', x)

x(2)  # This is sets to 2 and will print: "x is now 2"

# Inc/Dec operators of non-callable values are forwarded to enclosed value:

x += 1 # "x is now 3"
```

### Lazy

Lazy values are functions that are called only when the value is needed

```

equation = Lazy(lambda: 2 * math.pi)
equation() # computed!
equation() # value is returned again, since it has already been computed

```

Both reactive and lazy values can depend on each other and be chained.

```
x = Reactive(2)
y = Reactive(3)
equation = Lazy(lambda: x() + y(), [x, y])

equation() # 5 (computed and cached)
equation() # 5 (return cached value)

x(1) # set x to 1, invalidating the equation

equation() # 4 (recomputes since it was invalidated)
```

## Work-in-progress features

These features are incomplete so they are lacking documentation right now.

### Reactive properties

```
player.team = ReactiveProperty('red')
player.team += lambda team: print('Player switched to', team)
player.team = 'blue' # 'Player switch to blue'
```

### Reactive classes

### Reactive methods

### Reactive vectors

```

# set underlying type for colors, must have r,g,b accessors
Rvec.Type = glm.vec3

# XYZ
point = Rvec(1, 1, 1)

# print contents on change
point += lambda p: print(p.x, p.y, p.z)

# changing an individual property now fires change listeners
point.x = 100

```

### Reactive colors

```

# RGB
rgb = Rcolor(1, 1, 1)

# print contents on change
rgb += lambda c: print(c.r ,c.g, c.b)

# changing an individual property now fires change listeners
rgb.r = .5

```

### "Weak Lambdas" (Lambdas with Weakref Capturing)

### "Weak Method" (self parameter is a weakref)

