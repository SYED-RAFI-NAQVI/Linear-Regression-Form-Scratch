from numpy import *

#step 4
#calculating the error of the line by the formula ((y - mx + b) ^2 )/ number of data points ===> average of all the data points
#mean square error
def error_of_line(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

#step 5
#finding the m, b of the given line to find the best fit line 
#this helps to move the line to forward or backward repective to the data points for finding the best fit line
def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]



def gradient_descent(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def run():
    
    
    #Step 1 gathering the data
    points = genfromtxt("data.csv", delimiter=",")
    
    
    #Step 2 required parameters
    learning_rate = 0.0001
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 10000

    
    
    #Step 3 finding the error for the intial line or intial gradient.
    print ("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, error_of_line(initial_b, initial_m, points)))
    
    # Returning b, m form the function
    [b, m] = gradient_descent(points, initial_b, initial_m, learning_rate, num_iterations)
    
    #final step 6 displaying the error, slope, bias, number of iterations of the line ====> i.e best fit line for the given data set
    print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, error_of_line(b, m, points)))

if __name__ == '__main__':
    run()
