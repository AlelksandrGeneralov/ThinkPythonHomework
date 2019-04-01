

import cProfile
import pstats
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['math', 'engineering', 'compsci', 'arts', 'business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'names': random.choice(names),
            'majors': random.choice(majors)
        }
        result.append(person)
    return(result)


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'names': random.choice(names),
            'majors': random.choice(majors)

        }
        yield (person)


def timer():

    pr = cProfile.Profile()
    pr.enable()
    # time_start = time.time()
    people = people_list(100000)
    # time_elapsed = (time.time() - time_start)
    # print(time_elapsed)

    # time_start = time.time()
    people = people_generator(100000)
    # time_elapsed = (time.time() - time_start)
    # print(time_elapsed)
    pr.disable()
# record the profile in to a file 'prof_data'
    pr.dump_stats('prof_data')
# read the profile from file 'prof_data'
    ps = pstats.Stats('prof_data')
# sort the profile list by cumulative time
    ps.sort_stats('cumulative')
    ps.print_stats()


if __name__ == "__main__":
    timer()
