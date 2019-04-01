import cProfile
import pstats


def fill_in_dict():
    """fill in dictionary with key walues from a txt file"""
    # assign a 'data' list from the txt file
    data = open('words.txt')
    # assign an empty 'my_dict' dictionary
    my_dict = dict()

    for word in data:
        # fill in dictionarys wit a keys and empty values
        my_dict[word] = ''
    return(my_dict)


pr = cProfile.Profile()
pr.enable()

fill_in_dict()
print('test: ', fill_in_dict.__doc__)

pr.disable()
pr.dump_stats('prof_data')
ps = pstats.Stats('prof_data')
ps.sort_stats('cumulative')
ps.print_stats()
