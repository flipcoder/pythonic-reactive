#!/usr/bin/python3
import webcolors
import glm

EPSILON = 0.0001

def map_range(val, r1, r2):
    return (val - r1[0]) / (r1[1] - r1[0]) * (r2[1] - r2[0]) + r2[0]

class Color(glm.vec4):
    def __init__(self, *args, **kwargs):
        if args:
            v = args[0]
            try:
                a = args[1]
            except IndexError:
                a = 1.0
            ta = type(v)
            if ta in (tuple, list):
                super().__init__(*Color(*v))
            if v:
                lenargs = len(args)
                if ta is str:
                    r = webcolors.html5_parse_legacy_color(v)
                    super().__init__(glm.vec3(*r) / 255.0, a)
                elif ta in (float, int):
                    super().__init__(glm.vec3(v), a)
                elif ta == glm.vec3:
                    super().__init__(v, a)
                elif ta == glm.vec4:
                    super().__init__(v)
                else:
                    if lenargs == 4:
                        super().__init__(*args)
                    elif lenargs == 3:
                        super().__init__(glm.vec3(v), a)
                        return glm.vec4(glm.vec3(*args), a)
                    elif lenargs == 1:
                        super().__init__(glm.vec3(v), a)
                    elif lenargs == 2:
                        super().__init__(glm.vec3(v), args[1])
                    else:
                        raise ValueError("invalid color")
            else:
                super().__init__(0, 0, 0, 1)
        else:
            super().__init__(0, 0, 0, 1)

    def __eq__(self, b):
        return fcmp(self, Color(b))

    def __ne__(self, b):
        return not fcmp(self, Color(b))

