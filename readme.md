# Linear-Regression-From-Scratch


# step - 1 :

Collect our data - to collect our data we use famous library NUMPY, so import numpy

collect the data from data.csv which is comma seperated values

the data is about the hours of study of students and the scores they got in exam 

# step - 2 :

Defining the hyperparameters such as learning rate, b , m , number of iterations.

where learning rate is the rate of learning which say to learn from given data with certain rate or speed,

where b is the bias or y-intercept which is the point of intersection at y-axis,

m is the slope of the given line, where slope is the rate of change of line,

m and b is derived from a fromula y = mx + b.

num of iterations is the parameter to indicate how much time to take to train the model

# step - 3 :


Finding the mean square error of the line for the given data points by using the formula (y - mx + b) **2 / N ====> averaging the error with the total number of points 

where N is the number of points in the data set 

this step finds the mean square error of the intial line. 

# step - 4 :

Finding the best m, b for the best fit line

this step under goes recursiveness to find m, b where the line moves forward and backword with respect to the data points when there is less mean square error then we will get the best m, b values

this step is the actual gradient decent which finds the best fit line for the data points

      b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
      m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))

      these formulas helps to find the m and b

# step - 5 :

The main function grabs all the hyperparameters which are initialized in step 2 and pass it to the respective function to find the best fit line with gradient decent.

