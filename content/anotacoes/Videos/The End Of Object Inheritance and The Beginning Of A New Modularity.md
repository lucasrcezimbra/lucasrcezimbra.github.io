---
title: "The End Of Object Inheritance & The Beginning Of A New Modularity"
date: 2024-08-11
lastmod: 2024-08-12
---

[The End Of Object Inheritance & The Beginning Of A New Modularity](https://www.youtube.com/watch?v=3MNVP9-hglc)

## Composition over Inheritance
(4:30)
"If you are explaining, even if you are write, you are losing.".

Inheritance approach:
```python
class MyAbstractBase:
    def OrangeMethod(self):
        ...

    def GreenMethod(self):
        """
        Do not call OrangeMethod() in your implementation...
        """
        raise NotImplementedError()

    def BlueMethod(self):
        ...
```

vs composition approach:

```python
class Green:
    def GreenMethod(self):
        raise NotImplementedError()

class ImplementedGreen(Green):
    def __init__(self, blue):
        self._blue = blue

    def GreenMethod(self):
        ...
```


## Object Inheritance Fails At Fault Intolerance
(12:55)

- What happens if an extending class violates its parent's stages of abstraction?
    - You might get silent state corruption if the class stores mutable state.
    - You might get an infinite loop.
    - You might get perfect behavior until a year later when the library in
      which the superclass is defined is upgraded.


## Composition Fails At Fault Tolerance
(14:25)
- Doing the illegal is impossible because composition substitutes unidirectional
  references for bidirectional references.
- "Make Illegal States Unrepresentable" (Yaron Minsky)
- "Make Illegal Behavioral Interactions Impossible"


## The right way to break code into small methods and small objects
(16:10)
1. Break it so that relationships are minimized among the resulting pieces.
2. Break it so that unidirectional relationships dominate and bidirectional
   relationships are absent.
- bidirectional relationships (inheritance approach) are never necessary - "in
  10 years I haven't seen one that I haven't been able to eliminate"
