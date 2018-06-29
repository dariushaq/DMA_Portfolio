#a = [[1, 2, 3], [4, 5, 6]]
#print(a[0])

#days = [["Sunday"], ["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"], ["Friday"], ["Saturday"]]
#for x in days:
#    row = ""
#    for y in x:
#        row +=y
#        print y

#SFFF
#FHFH
#FFFH
#HFFG

#print("S F F F F H F H F F F H H F F G")

#l = ["S", "F", "H", "G"]
#print(l[0] + 3*l[1])
#print(l[1] + l[2] + l[1] + l[2])
#print(3*l[1] + l[2])
#print(l[2] + 2*l[1] + l[3])

#grid = [["S", 3*"F"], ["F", "H", "F", "H"], [3*"F", "H"], ["H", 2*"F", "G"]]

grid = [["SFFF"], ["FHFH"], ["FFFH"], ["HFFG"]]
for c in grid:
    row = ""
    for r in c:
        row +=r
        print r

grid = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]                #
for i in range(len(grid)):                              #
    for j in range(len(grid[i])):                       #
        print(grid[i][j]),                              #
    print(" ")                                          #

grid = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]                #
for row in grid:                                        #  These three sections all do the exact same thing
    for elem in row:                                    #
        print(elem),                                    #
    print(" ")                                          #

grid = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]                #
for row in grid:                                        #
    print(" ".join([str(elem) for elem in row]))        #
