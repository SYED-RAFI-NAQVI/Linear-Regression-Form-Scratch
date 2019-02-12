#importing the required packages
import numpy as np

def error_of_line(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x =  points[i, 0]
        y = points[i, 1]
        totalError += (y- (m * x + b)) ** 2
        return totalError/ float(len(points))


def run():
    #Step 1 gathering the data
    points = np.genfromtxt('data.csv', delimiter=',')

    #Step 2 required parameters
    learning_rate = 0.001
    init_b = 0
    init_m = 0
    num_iterations = 1000
    #Step 3 finding the error for the intial line or intial gradient.
    print("intial gradient decent at b = {0}, m = {1}, error = {2}".format(init_b, init_m, error_of_line(init_b, init_m, points)))



def main():
    run()