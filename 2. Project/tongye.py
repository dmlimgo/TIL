import sys
import pprint
sys.stdin = open("lunch_list.txt", encoding='UTF8')

lunch_info = dict()
try:
    while True:
        line = input()
        if len(line) and line[0].isnumeric():
            continue
        else:
            line = line.split()
            for person in line:
                if person not in lunch_info:
                    lunch_info[person] = {person: 0}
                for other_person in line:
                    if other_person in lunch_info[person]:
                        lunch_info[person][other_person] += 1
                    else:
                        lunch_info[person][other_person] = 1
except EOFError:
    pass

pprint.pprint(lunch_info)