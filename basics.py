def mean(value):
    if type(value) == dict:
        ave = sum(value.values())/len(value)
    else:
        ave = sum(value)/len(value)
    return ave
studentscore = {"Joe": 8.9, "Fred": 9.3, "Zel": 5.6, "Matt": 7.4}
grades = [1, 2, 3, 4]
print(mean(studentscore))
print(mean(grades))

