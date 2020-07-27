from os import system
import os
x = input("Your text here : " )
def my_text(text):
    system("say {}".format(text))

    text = x
    my_text(text)
