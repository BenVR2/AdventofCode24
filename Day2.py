import numpy as np
import time





def main():
    check_sum = 0
    for i in range(1000):
        safety_report = np.loadtxt('./Day2.txt', delimiter=' ', max_rows=1, skiprows=i)
        #print('-----')
        #print(safety_report)
        check_sum += check_report(safety_report)


    check_sum_damper = 0
    for i in range(1000):
        safety_report = np.loadtxt('./Day2.txt', delimiter=' ', max_rows=1, skiprows=i)
        check_sum_damper += damper(safety_report)


    #print(np.shape(safety_reports))
    return check_sum, check_sum_damper

def damper(report):
    for k in range(len(report)):
        damped_report = np.delete(report, k)
        if check_report(damped_report):
            return 1
    return 0


def check_report(report):
    dif_one = report[1]-report[0]
    if dif_one > 0 and dif_one < 4:
        #print('Ascending')
        for j in range(len(report)-1):
            dif = report[j+1] - report[j]
            if not (dif > 0 and dif < 4):
                #print('unsafe')
                return 0
        return 1
    if dif_one < 0 and dif_one > -4:
        #print('Descending')
        for j in range(len(report)-1):
            dif = report[j+1] - report[j]
            if not (dif < 0 and dif > -4):
                #print('unsafe')
                return 0
        return 1

    return 0

### 
start = time.time()

if __name__ == "__main__":
    result_one, result_two = main()
    print("The first result is: {:.0f}".format(result_one))
    print("And the second: {:.0f}".format(result_two))
end = time.time()
print('Calculated in an elapsed time of {:.3f} seconds.'.format(end-start))