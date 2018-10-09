# ---
# title: Simple file
# ---

# Here we have some text
# And below we have some python code
def f(x):
    return x+1
def h(y):
    return y-1


# Hello

# Demonstrate:
# * conversion of regular python script into _Jupyter notebook_
# * support **Markdown**
# * this is a list


# %% # SCI CELL TEST1

from __future__ import absolute_import, print_function, division

"""
## Hello

This is a *hello world* function.

"""

# %% SCI CELL TEST1
def hello():
    """
    This is a docstring
    """
    print("hello")


"""
## Another Cell 1
"""


def main():
    hello()


"""
### Run this
"""

if __name__ == '__main__':
    def what():
        main()
    print(what())


"""
## Another Cell 2
"""


import pandas as pd
# +
def data():
    return pd.DataFrame({'A': [0, 1]})
data()
# +
def data2():
    return pd.DataFrame({'B': [0, 1]})
data2()
# +
# Finally we have a cell with only comments
# This cell should remain a code cell and not get converted
# to markdown
# + {"endofcell": "--"}
# This cell has an enumeration in it that should not
# match the endofcell marker!
# - item 1
# - item 2
# -
# --
