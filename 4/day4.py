with open(r'path/to/input.txt', "r") as f:
    words = f.read().splitlines()
xmas = 0
cross = 0

for i, line in enumerate(words):
    for j in range(len(line)):
        #Horizontal, back and forth. 
        if j+4 <= len(line) and line[j:j+4] in ["XMAS", "SAMX"]:
            xmas += 1
        #Vertical and diagonal, back and forth.
        vertical, diagonal_l, diagonal_r = "", "", ""
        if i+4 <= len(words):
            for k in range(4):
                vertical += words[i+k][j]
                
                if j-k >= 0:
                    diagonal_l += words[i+k][j-k]
                    
                if j+4 <= len(line):
                    diagonal_r += words[i+k][j+k]

            if vertical in ["XMAS", "SAMX"]:
                xmas += 1
            if diagonal_l in ["XMAS", "SAMX"]:
                xmas += 1
            if diagonal_r in ["XMAS", "SAMX"]:
                xmas += 1
        
        if i >= 1 and i < len(words)-1 and j >= 1 and j < len(line)-1:
            diag_l, diag_r = "", ""
            for k in range(-1, 2):
                diag_l += words[i+k][j+k]
                diag_r += words[i+k][j-k]
            if diag_l in ["MAS", "SAM"] and diag_r in ["MAS", "SAM"]:
                cross += 1
print(xmas)
print(cross)
#2554
#1916