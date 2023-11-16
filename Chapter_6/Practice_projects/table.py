def printTable(tableData):
    max_l_list = []
    for  list in tableData:
        max_length = 0
        for str in list:
            if len(str) > max_length:
                max_length = len(str)
        max_l_list.append(max_length)

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(max_l_list[j]), end =" ")
        print("\n")

table = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']] 

printTable(table)