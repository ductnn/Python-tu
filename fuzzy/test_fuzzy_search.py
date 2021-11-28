from fuzzy_search_test import(
    fuzzy_search,
    levenshtein_distance,
)


if __name__ == '__main__':
    print("\n")

    # fuzzy_search
    print("======= Fuzzy Search =======")
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

    print("\n")

    # levenshtein distance
    print("======= Levenshtein Distance =======")
    print(levenshtein_distance('a', 'a'))
    print(levenshtein_distance('b', 'abc'))
    print(levenshtein_distance('twl', 'cartwheel'))
    print(levenshtein_distance('cart', 'cartwheel'))
    print(levenshtein_distance('car', 'cartwheel'))
    print(levenshtein_distance('cw', 'cartwheel'))
    print(levenshtein_distance('cwhl', 'cartwheel'))
    print(levenshtein_distance('cwheel', 'cartwheel'))
    print(levenshtein_distance('cartwheel', 'cartwheel'))
    print(levenshtein_distance('cl', 'cartwheel'))
    print(levenshtein_distance('a', ''))
    print(levenshtein_distance('cwheeel', 'cartwheel'))
    print(levenshtein_distance('lw', 'cartwheel'))
    print(levenshtein_distance('thw', 'cartwheel'))
    print(levenshtein_distance('dog', 'cartwheel'))
    print(levenshtein_distance('cartwheell', 'cartwheel'))
