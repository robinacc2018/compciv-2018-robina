from datastubs import PEOPLE_LIST

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    # fill it out

    def age_getter(a):
        return a['age']
    return sorted(PEOPLE_LIST, key=age_getter)

def oldest():
    """
    sort by age in descending order
    """
    # fill it out
    return sorted(PEOPLE_LIST, key=lambda x: x['age'], reverse = True)


def name_reverse_alpha():
    # fill it out

    def name_getter(n):
        return n['name']
    return sorted(PEOPLE_LIST, key=name_getter, reverse=True)

def country_then_age():
    # fill it out
    return sorted(PEOPLE_LIST, key=lambda x: [x['country'], x['age']])

