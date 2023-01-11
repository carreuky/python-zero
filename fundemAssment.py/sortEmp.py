def sort_employees(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    return sorted_employees

#lambda
#def function(x):
# return x[soreted_index]

words =[ 'touchMe','heroHero', 'Sebsatain', 'touchMe' ,'heroHero', 'yuri alpha', 'Aura']

n =3
def get_n_longest_unique_words(words, n):
    
    unique_words = get_unique_words(words)
    longest_words = []

    while len(longest_words) < n:
            current_longest = ""
            for word in unique_words:
                if len(word) > len(current_longest):
                    current_longest = word
#this will remove the last biggest word fron unique
            unique_words.remove(current_longest)
#this will add to the resutl arr
            longest_words.append(current_longest)

    return longest_words


def get_unique_words(words):
    unique_words = []
    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)

    return unique_words



obj = {'victim': 8, 'marie':'super child prodagey', 1: 'superem one'}
objNum= {'yuri':1, 'Lups Regaina': 2, 'Naraberl':3, 'solution':4}

print(sum(objNum.values()))