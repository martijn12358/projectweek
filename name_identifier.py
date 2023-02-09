import difflib

# all brand names in a list
brand_names = ["noodle", "nassau", "crivit", "titleist", "trufeel", "dunlop", "miracle distance",
               "srixon", "hogan", "black diamond", "callaway", "top flite", "st andrews", "pro power",
               "inesis", "maxfli", "shamp", "extreme", "wilson", "fantom"]

# types of golfballs
type_names = ["distance", "hi-spin", "wareird", "xl-3000", "xl-distance", "soft 500", "titanium",
              "apex tour", "maximum", "big fairways", "revext", "nxt tour", "qx"]


def best_match(name):
    name = name.lower()

    # if no match can be found, return no match
    close = "no match"

    # if the given name was correct, pass is back
    if (name in brand_names) or (name in type_names):
        return name

    # if not, find a close match
    try:
        close = difflib.get_close_matches(name, brand_names)[0]
    except:
        pass

    # do the same for types
    try:
        close = difflib.get_close_matches(name, type_names)[0]
    except:
        pass

    return close


def number_match(input_num):
    # if the number was read right, return it as an int
    if input_num in ['1', '2', '3', '4']:
        return int(input_num)

    input_num = input_num.lower()

    # all letters numbers may look like
    like_1 = ['l', 'i', 'j', 't']
    like_2 = ['z', 'c']
    like_3 = ['b', '8', 's']
    like_4 = ['a']

    # checking to see if it looks like any of the letters in the lists
    if input_num in like_1:
        return 1
    elif input_num in like_2:
        return 2
    elif input_num in like_3:
        return 3
    elif input_num in like_4:
        return 4

    return "no match"


'''
input_str = "extreme"
print(f"{input_str = }")
print(f"{best_match(input_str) = }")
'''