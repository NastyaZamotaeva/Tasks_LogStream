#Даны 3 множества, объедините первый со вторым,
#а полученное множество с третьим. 
# Сделайте список из элементов, 
# которые не вошли в множества, 
# а потом проверьте разницу всех элементов множества и списка.

set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}

combined_set1 = set1 | set2
combined_set2 = combined_set1 | set3
all_elem =[i for i in range(80)]
not_included = [i for i in range(80) if not combined_set2]

differ = set(all_elem) - set(not_included)
differ = list(differ)
print ("Combined 1 ",combined_set1,"\n","Combined 2 ", combined_set2,"\n","difference", differ)
