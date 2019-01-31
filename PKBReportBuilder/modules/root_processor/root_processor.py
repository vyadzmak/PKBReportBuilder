from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def check_seq(a,b):

    r = similar(a,b)

    t=0

    pass