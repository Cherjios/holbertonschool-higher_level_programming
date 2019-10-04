#!/usr/bin/python3
"""Function that  prints a text with 2 lines after finding this characters .: ?"""


def text_indentation(text):
    """ Prints a text with 2 lines after finding this characters .: ?


    Arg:
    text: String value, otherwise raise TypeError with message text must be a
    string"""

    if not isinstance(text, str) or text is None or len(text) < 0:
        raise TypeError("text must be a string")

    for text2 in ".?:":
        text = (text2 + "\n\n").join(
            [line.strip(" ") for line in text.split(text2)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt") 
