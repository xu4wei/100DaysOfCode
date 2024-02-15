#list sort by index[1]
def compare_num_of_two(listx):
    return listx[1]

num_list = [[1,2,3],[2,1,3],[4,0,1]]
num_list.sort(key=compare_num_of_two)
print(num_list)
