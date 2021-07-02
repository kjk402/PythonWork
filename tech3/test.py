matrix =[
            [ 0, 1, 2,],
            [ 3, 4, 5 ],
            [ 6, 7, 8 ],
        ]
rows =4
columns =4

solution =[[] for i in range(rows +columns -1)]

for i in range(rows):
    for j in range(columns):
        sum = i +j
        if(sum %2 ==0):

            # add at beginning
            solution[sum].insert(0 ,matrix[i][j])
        else:

            # add at end of the list
            solution[sum].append(matrix[i][j])


        # print the solution as it as
for i in solution:
    for j in i:
        print(j ,end=" ")