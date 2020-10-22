"""The solution to the ModuleNotFoundError during class:

move the testing_module folder inside the oop folder. Since the testing_module
folder was outside of oop folder, main.py could not find the testing_module.
"""

from testing_module.testing import test

def main(arg):

    t = test(arg)
    t.debug()

if __name__ == "__main__":
    main(1)