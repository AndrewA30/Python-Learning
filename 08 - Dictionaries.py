purse = dict()
purse["money"] = 12
purse["coin"] = 15

print(purse)

purse['money'] = purse["money"]+2
print(purse)
#cara lain nambah data
# purse = {"makeup":12,"kalung":1}

counts = dict()
# names = ['andrew','andre','andreas','andrew','andre']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1;
# print(counts)

# cara lain lebih simple tidak usah pake if     
# for name in names:
#     counts[name] = counts.get(name,0) +1
# print(counts)

#coba input ke dict
while True:
    inp = input("Masukkan nama = ")
    if inp =="done":
        break;
    counts[inp] = counts.get(inp,0) +1
print(counts)
