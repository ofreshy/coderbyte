"""
Using the Python language,
have the function StepWalking(num) take the num parameter being passed which will be an integer between 1 and 15
that represents the number of stairs you will have to climb.
You can climb the set of stairs by taking either 1 step or 2 steps,
 and you can combine these in any order.
 So for example, to climb 3 steps you can either do: (1 step, 1 step, 1 step) or (2, 1) or (1, 2).
 So for 3 steps we have 3 different ways to climb them, so your program should return 3.
 Your program should return the number of combinations of climbing num steps.

"""


def StepWalking(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return StepWalking(num-1) + StepWalking(num-2)
