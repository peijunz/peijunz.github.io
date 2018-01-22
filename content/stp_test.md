---
title: Spanning Tree Protocol Testing Code
date: 2018-01-19
lang: en
slug: stp-test
---
[Download Here]({attach}/static/stptest.zip)
# How to use
There are two ways:
+ simply run `python check_answer.py` to test randomly generated cases
+ run `python check_answer.py <topology_file> <log_file` to check for some specific topology 

# Notes
1. **Only** copy your Switch.py to this test suite
2. Do not over write Topology.py
3. Please add a Switch.activeLinks attribute to your Switch class like:
```py
class Switch:
    @property
    def activeLinks(self):
        # Your code to get active Links
```
`property` decorator ensures that you can write object.activeLinks instead of object.activeLinks()
