import bisect
def sort_by_age(person_list):
    return sorted(person_list, key=lambda x: x[1])
scores =[(60, 'Nonzamo'),(80, 'willy'),(56,'rono')]
bisect.insort(scores, (67,'amali'))
print(scores)