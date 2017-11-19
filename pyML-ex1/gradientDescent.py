import numpy as np;
from computeCost import * 
 
def gradientDescent(X, y, theta, alpha, num_iters):
    #GRADIENTDESCENT Performs gradient descent to learn theta
    #   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
    #   taking num_iters gradient steps with learning rate alpha
 
    # Initialize some useful values
    m = np.shape(y)[0]; # number of training examples
    n = np.shape(X)[1]; # number of features

    J_history = np.zeros((num_iters, ));
 
    for iter in range(num_iters):
         # ====================== YOUR CODE HERE ======================
        #  Instructions: Perform a single gradient step on the parameter vector
        #               theta. 
        #
        # Hint: While debugging, it can be useful to print out the values
        #       of the cost function (computeCost) and gradient here.
        #
        errorTerm = np.dot(X, theta) - np.vstack(y);
        theta = theta - alpha * np.vstack((np.sum(np.repeat(errorTerm, n, axis=1)*X, 0)/m));
        # ============================================================
 
        # Save the cost J in every iteration    
        J_history[iter] = computeCost(X, y, theta);
    
    return theta, J_history