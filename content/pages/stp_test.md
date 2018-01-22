---
title: Spanning Tree Protocol Testing Code
date: 2018-01-19
status: hidden
slug: stptest
---

[Download Here]({filename}/stptest.zip)
## Prerequired
1. **Only** copy your `Switch.py` to this test suite. Do NOT overwrite `Topology.py`
2. Please add a `Switch.activeLinks` attribute to your Switch class. As an example:
```py
class Switch:
    @property
    def activeLinks(self):
        # Your code to get active Links
```
`property` decorator ensures that you can write object.activeLinks instead of object.activeLinks()

## How to use
Then there are two ways to run `check_answer.py`:

+ Simply run `python check_answer.py` to test randomly generated cases
+ Run `python check_answer.py <topology_file> <log_file>` to check for some specific topology 
