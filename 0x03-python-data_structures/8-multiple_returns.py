#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    ch = sentence[0] if l > 0 else "None"
    return (l, ch)
