## Pythonic-Reactive

This python module contains the reactive programming components I developed as
part of my qork game engine project, and now they're separated here into their own module.

Be aware that the test coverage is incomplete and many features are not documented.

It is not suitable for use right now, unless you intend to continue its development
with me!

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

Lazy values can depend on other lazy or reactive values:

```
x = Reactive(2)
y = Reactive(3)
equation = Lazy(lambda: x() + y(), [x, y])

equation() # 5 (computed and cached)
equation() # 5 (return cached value)

x(1) # invalidates the equation

equation() # 4 (recomputes since it was invalidated)
```

