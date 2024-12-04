import numpy as np
import time





def main():
    # load and seperate lists
    id_list = np.loadtxt('./Day1.txt')
    id_list_1 = id_list[:,0]
    id_list_2 = id_list[:,1]

    # part one, sort lists 
    for j in range(len(id_list_1)):
        for i in range(len(id_list_1)-1-j):
            
            if id_list_1[i] > id_list_1[i+1]:
                temp = id_list_1[i]
                id_list_1[i] = id_list_1[i+1]
                id_list_1[i+1] = temp

            if id_list_2[i] > id_list_2[i+1]:
                temp = id_list_2[i]
                id_list_2[i] = id_list_2[i+1]
                id_list_2[i+1] = temp    
    # sum the difference of the list 
    temp_sum = 0
    for i in range(len(id_list_1)):
        temp_sum += np.abs(id_list_2[i]-id_list_1[i])
    

    # part two
    temp_sim = 0
    for i in range(len(id_list_1)):
        temp_sim += id_list_1[i]*len(id_list_2[id_list_2==id_list_1[i]])
    return temp_sum, temp_sim


### 
start = time.time()

if __name__ == "__main__":
    total_id_diff, total_id_sim = main()
    print("The first result is: {:.0f}".format(total_id_diff))
    print("And the second: {:.0f}".format(total_id_sim))
end = time.time()
print('Calculated in an elapsed time of {:.3f} seconds.'.format(end-start))