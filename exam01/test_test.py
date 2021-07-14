from test import letter_occurence


def test_1():
    assert(letter_occurence("hallo") == "doppelt")

def test_2():
    assert(letter_occurence("halllo") == "mehrfach")

def test_3():
    assert(letter_occurence("hi") == "einfach")

def test_4():
    assert(letter_occurence("h20") == "error")
