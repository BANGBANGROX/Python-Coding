# 2d lists
numberGrid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

print(numberGrid);
print(numberGrid[0][0]);

# nested for loops
for i in range(len(numberGrid)) :
    for j in range(len(numberGrid[i])) :
        print(numberGrid[i][j]);