import csv

def extract_velocity_from_file(name_of_file):
    with open('./data files/' + name_of_file) as csvfile:
        readCSV = csv.reader(csvfile)
        index = 0
        list_of_velocities = []
        for row in readCSV:
            if index == 3:
                list_of_velocities.append(row[index])
            if "X [ m ]" in row:
                index = 3
        return list_of_velocities

def create_matrix(list1, list2):
    if(len(list1) == len(list2)):
        matrix = []
        for i in range(len(list1)):
            matrix.append([list1[i], list2[i]])
    else:
        return 'Error'
    return matrix



#file_name = str(input("Enter Filename \n> "))
outer_vel = extract_velocity_from_file('Array1.csv')
#file_name = str(input("Enter Filename \n> "))
inner_vel = extract_velocity_from_file('Array1inner.csv')
matrix1 = create_matrix(outer_vel, inner_vel)


#file_name = str(input("Enter Filename \n> "))
outer_vel = extract_velocity_from_file('Array2.csv')
#file_name = str(input("Enter Filename \n> "))
inner_vel = extract_velocity_from_file('Array2inner.csv')
matrix2 = create_matrix(outer_vel, inner_vel)


# Array1.csv and Array1inner.csv Works
# Tests Array2.csv and Array2inner.csv
# test Array3.csv and Array3inner.csv
#file_name = str(input("Enter Filename \n> "))
outer_vel = extract_velocity_from_file('Array3.csv')
#file_name = str(input("Enter Filename \n> "))
inner_vel = extract_velocity_from_file('Array3inner.csv')
matrix3 = create_matrix(outer_vel, inner_vel)


print(matrix1[0])
print(matrix2[0])
print(matrix3[0])
