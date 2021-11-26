from fuzzy_search_test import fuzzy_search


if __name__ == '__main__':
    print(fuzzy_search('a', 'a'))
    print(fuzzy_search('b', 'abc'))
    print(fuzzy_search('twl', 'cartwheel'))
    print(fuzzy_search('cart', 'cartwheel'))
    print(fuzzy_search('car', 'cartwheel'))
    print(fuzzy_search('cw', 'cartwheel'))
    print(fuzzy_search('cwhl', 'cartwheel'))
    print(fuzzy_search('cwheel', 'cartwheel'))
    print(fuzzy_search('cartwheel', 'cartwheel'))
    print(fuzzy_search('cl', 'cartwheel'))
    print(fuzzy_search('a', ''))
    print(fuzzy_search('cwheeel', 'cartwheel'))
    print(fuzzy_search('lw', 'cartwheel'))
    print(fuzzy_search('thw', 'cartwheel'))
    print(fuzzy_search('dog', 'cartwheel'))
    print(fuzzy_search('cartwheell', 'cartwheel'))
