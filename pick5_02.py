ff = open("data/formatedpick5winningnumbers.txt", "r")


an = set(range(1,44))
wn = set()

wnd = {}
fwn  = {}
swn = {}
twn = {}
fown = {}
fivwn = {}

fr = True 
fl = []

for row in ff.readlines():
	for i, item in enumerate(row.strip().split(' ')):
		if i > 0:
			wnd[int(item)] = wnd.get(int(item), 0) + 1
			wn.add(int(item))

			if i == 1:
				fwn[int(item)] = fwn.get(int(item), 0) + 1
			
			if i == 2:
				swn[int(item)] = swn.get(int(item), 0) + 1
			
			if i == 3:
				twn[int(item)] = twn.get(int(item), 0) + 1

			if i == 4:
				fown[int(item)] = fown.get(int(item), 0) + 1

			if i == 5:
				fivwn[int(item)] = fivwn.get(int(item), 0) + 1

			if fr:
				fl.append(int(item))

	fr = False
			
ff.close()

for v in range(100,0,-1):
	for k in sorted(wnd.keys()):
		if v == wnd[k]:
			if (k== fl[0] or k == fl[1] or k == fl[2] or k == fl[3] or k == fl[4]):
				print('========> ' + str(k) + ' ' + str(wnd[k]))

			else:
				print(str(k) + ' ' + str(wnd[k]))

print("---------------------------")
for v in (an - wn):
	print(v, '0')

print("------- 1st Winning Number --------------------")
for v in range(100,0,-1):
	for k in sorted(fwn.keys()):
		if v == fwn[k]:
			print(str(k) + ' ' + str(fwn[k]))

print("---------------------------")
for k in sorted(fwn.keys()):
	print(str(k) + ' ' + str(fwn[k]))


print("------------ 2nd Winning Number ---------------")
for v in range(100,0,-1):
	for k in sorted(swn.keys()):
		if v == swn[k]:
			print(str(k) + ' ' + str(swn[k]))

print("---------------------------")
for k in sorted(swn.keys()):
	print(str(k) + ' ' + str(swn[k]))

print("--------- 3rd Winning Number ------------------")
for v in range(100,0,-1):
	for k in sorted(twn.keys()):
		if v == twn[k]:
			print(str(k) + ' ' + str(twn[k]))

print("---------------------------")
for k in sorted(twn.keys()):
	print(str(k) + ' ' + str(twn[k]))

print("----------- 4th Winning Number ----------------")
for v in range(100,0,-1):
	for k in sorted(fown.keys()):
		if v == fown[k]:
			print(str(k) + ' ' + str(fown[k]))

print("---------------------------")
for k in sorted(fown.keys()):
	print(str(k) + ' ' + str(fown[k]))

print("----------- 5th Winning Number ----------------")
for v in range(100,0,-1):
	for k in sorted(fivwn.keys()):
		if v == fivwn[k]:
			print(str(k) + ' ' + str(fivwn[k]))

print("---------------------------")
for k in sorted(fivwn.keys()):
	print(str(k) + ' ' + str(fivwn[k]))