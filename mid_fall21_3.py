#todo
all = []
aDict = {}
n = int(input("n:"))
for i in range(n):
    user = input("Enter:").split()
    all.append(user)
for a_list in all:
    x = a_list[0]
    if x not in aDict:
        aDict[x] = {}
for k,v in aDict.items():

    for a_list in all:
        location = a_list[0]
        if location == k:

            u_id = a_list[1][-2::] + a_list[2] + a_list[3]
            v[u_id] = [a_list[-2], int(a_list[-1])]
            # v = temp_dict

print(aDict)
