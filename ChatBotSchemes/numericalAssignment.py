def assignNumberGender(op):
    switcher = {
        1 : 2,
        2 : 0,
        3 : 1
    }

    return switcher.get(op, 0)

def assignNumberReligion(op):

    switcher = {
        1 : 9,
        2 : 5,
        3 : 11,
        4 : 1
    }
    return switcher.get(op, 0)

def assignNumberCommunity(op):
    switcher = {
        1 : 4,
        2 : 6,
        3 : 7,
        4 : 0,
        5 : 3
    }
    return switcher.get(op, 0)

def assignMaleProfession(op):
    switcher = {
        1 : 18,
        2 : 22,
        3 : 5,
        4 : 6,
        5 : 26,
        6 : 25,
        7 : 7,
        8 : 11,
        9 : 16,
        10 : 12,
        11 : 24,
        12 : 1,

        }
    return switcher.get(op, 0)

def assignFemaleProfession(op):
    switcher =  {
        1 :  19,
        2 : 23,
        3 : 13,
        4 : 8,
        5 : 19,
        6 : 3,
        7 : 16,
        8 : 2,
        9 : 12,
        10 : 27,
        11 : 23,
        12 : 24,
        13 : 1
        }
    return switcher.get(op, 0)
