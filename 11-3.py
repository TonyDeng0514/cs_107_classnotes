'''
Test cases:

>>> assert anagram('cat','act')
>>> assert anagram('Bored', 'Robed')
>>> assert anagram('Save', 'Vase')
'''


# anagram

def anagram(a: str, b: str) -> bool:
    

    a = list(a.lower())
    b = list(b.lower())

    for i in a:
        if i == " ":
            a.remove(i)
    for i in b:
        if i == " ":
            b.remove(i)

    if len(a) != len(b):
        return False
    else:
        for i in a:
            for j in b:
                if i == j:
                    b.remove(j)
    
    if b != []:
        return False
    else:
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")