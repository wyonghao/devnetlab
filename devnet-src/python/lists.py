devices=['R1','R2','R3','S1','S2']
for items in devices:
    if 'R' in items:
        print(items)
switches=[]
for items in devices:
    if 'S' in items:
        switches.append(items)

switches