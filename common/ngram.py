def ngram(text_array, ns):
    '''
    Convert a sentence (given as an array) to a dictionary of n-grams
    @params
        text_array: list<str>: a sentence split on spaces, e.g.
                   ['this', 'is', 'sample', 'input']
        ns: list<int>: the desired n-grams in the output
    @return
        an array of dictionary: counts of occurrence of each n-gram; if
           ns = [1, 2, 3], the returned array will be of the form:
           [{1-grams}, {2-grams}, {3-grams}], e.g:
           ngram(['this', 'is', 'a', 'test'], [1, 2, 3]) returns:
           [{ 'this': 1, 'is': 1, 'a': 1, 'test': 1 }, 
            { 'this is': 1, 'is a': 1, 'a test': 1},
            { 'this is a': 1, 'is a test': 1 }]
    '''
    n_words = len(text_array)
    ngram_dicts = []
    
    for n in ns:
        ngram_dict = {}
        
        for i in range(n_words + 1 - n):
            seq = ' '.join(text_array[i:(i + n)])
            
            if seq in ngram_dict:
                ngram_dict[seq] += 1
            else:
                ngram_dict[seq] = 1

        ngram_dicts.append(ngram_dict)
        
    return ngram_dicts
