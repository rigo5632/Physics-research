import csv

def extract_velocity_from_file(name_of_file):
    with open('./data files/' + name_of_file) as csvfile:
        file = csv.reader(csvfile)
        index = 0
        list_of_velocities = []
        for row in file:
            if index == 3:
                axis = row[2]
                list_of_velocities.append(row[index])
            if "X [ m ]" in row:
                index = 3
        return list_of_velocities, axis

def create_sub_matrix(list1, axis1, list2, axis2):
    if(axis1 != axis2):
        return 'Error. Please Enter Files with the same Z Index.'
    if(len(list1) == len(list2)):
        matrix = []
        for i in range(len(list1)):
            matrix.append([list1[i], list2[i]])
    else:
        return 'Error. Make sure that sample size is of same size'
    return matrix

def create_matrix():
    sub_matrix = []
    for file in range(3):
        print('Enter file with Outer Velocities')
        outer_file_name = str(input('> '))
        print('Enter file with Inner Velocities')
        inner_file_name = str(input('> '))
        if(outer_file_name == inner_file_name):
            print('Please enter different files')
            exit()
        outer_vel, outer_vel_axis = extract_velocity_from_file(outer_file_name)
        inner_vel, inner_vel_axis = extract_velocity_from_file(inner_file_name)
        sub_matrix.append(create_sub_matrix(outer_vel, outer_vel_axis, inner_vel, inner_vel_axis))
    return sub_matrix

def make_csv_file(m):
    print('Enter matrix file name. EX: Matrix.csv')
    new_file_name = str(input('> '))
    with open(new_file_name, mode='w', newline='') as newFile:
        writer = csv.writer(newFile)
        for i in range(len(m[0])):
            writer.writerow(['Outer Velocity', 'Inner Velocity'])
            for j in range(len(m)):
                writer.writerow(m[j][i])
            writer.writerow([' '])
                    

# MAIN
matrix = create_matrix()
make_csv_file(matrix)
