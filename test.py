def search_dictionary(dict, search_term, similar = 85):
    """
    takes in a dictionary to search and a search term.
    
    Will return a dictionary of terms that either have the exact
    value searched, are at least given percent similar similar 
    (in letters contained).
    """
    
    output = {}
    for key, value in dict.items():
        # Check if the search term is in the current key
        letters_similar = 0
        for letter in search_term:
           if letter in key: letters_similar += 1
           
        if letters_similar/len(key) >= similar/100:
            output[key] = value
    
    return output

dict = {
    'dog' : 'an animal',
    'cat' : 'another animal',
    'computer' : 'a device',
    'mouse' : 'a device',
    'cord' : 'a thing',
    'accord' : 'agreement',
    'concord' : 'a place',
    'another' : 'one more',
    'this' : 'a enlish word'
}

print(search_dictionary(dict, 'taco'))