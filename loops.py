def index_of_by_index(word, list, index):
    i=index
    while i < len(list):
        if list[i] == word:
            return i
        else:
            i=i+1
    if i>=len(list):
        return -1


def index_of_empty(list):
    a=""
    for i, current_elem in enumerate(list):
        if current_elem == a:
            return i
    return -1
def index_of(word, list):
    i=0
    while i <len(list):
        if list[i]==word:
            return i
        else:
            i=i+1
    if i>=len(list):
        return -1

def put(word, list):
    a=""
    for i, current_elem in enumerate(list):
        if current_elem == a:
            list[i]=word
            return i
    return -1

def remove(word, list):
    a=""
    m=0
    for i, current_elem in enumerate(list):
        if current_elem == word:
            list[i]=a
            m=m+1
    return m
