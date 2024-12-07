with open(r'C:\Users\JANDRE21\projects\.vscode\AoC24\1\input.txt', "r") as f:
    total = 0
    id1 = []
    id2 = []
    for i in range(1000):
        id = f.readline().split()
        id1.append(int(id[0]))
        id2.append(int(id[1]))
        
    id1.sort()
    id2.sort()
    
    for i in range(len(id1)):
        multiples = 0
        for j in range(len(id2)):
            if id1[i] == id2[j]:
                multiples+=1
        total += id1[i] * multiples

    print(total)