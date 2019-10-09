
import cProfile
import pstats


def sort_by_length():
    """sort a words by len1"""
    t = []
    words = open('words.txt')
    for word in words:
        line = word.strip()
        t.append((len(line), line))
    t.sort(reverse=False)

    res = []
    for length, line in t:
        res.append(line)
    return(res)


pr = cProfile.Profile()
pr.enable()

print(sort_by_length.__doc__)
print(sort_by_length())

pr.disable()
pr.dump_stats('prof_data')
ps = pstats.Stats('prof_data')
ps.sort_stats('cumulative')
ps.print_stats()
