# Week 0 Problem Set

## 1. Deep Thought

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

Hints:
1. Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
2. Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.

## 2. Playback Speed

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

## 3. Making Faces

Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

Hints:
1. Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
2. Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
3. An emoji is actually just a character, so you can quote it like any str, a la "😐". And you can copy and paste the emoji from this page into your own code as needed.

## 4. Einstein

Even if you haven’t studied physics (recently or ever!), you might have heard that 𝐸 =𝑚⁢𝑐2, wherein 𝐸 represents energy (measured in Joules), 𝑚 represents mass (measured in kilograms), and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

Hints:
1. Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
2. Recall that int can convert a str to an int, per docs.python.org/3/library/functions.html#int.
3. Recall that Python comes with several built-in functions, per docs.python.org/3/library/functions.html.

## 5. Tip Calculator

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO

main()


Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

dollars_to_float, which should accept a str as input (formatted as $xx.xx, wherein each x is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as xx%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
Assume that the user will input values in the expected formats.

Hints:
1. Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
2. Recall that float can convert a str to a float, per docs.python.org/3/library/functions.html#float.
3. Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
