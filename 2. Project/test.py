line = ['임동명', '이민교', '정태현']
lunch_info = dict()

for person in line:
    if person not in lunch_info:
        lunch_info[person] = {person: 0}
    for other_person in line:
        if other_person in lunch_info[person]:
            lunch_info[person][other_person] += 1
        else:
            lunch_info[person][other_person] = 1
