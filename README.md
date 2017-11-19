# Andrew-Ng-course-in-ipython-ML
This collection of ipython notebooks contains my translation of Andrew Ng's Machine Learning Course assignments into python.
Where possible I have attempted to maintain the structure, not only in the content and flow of the code, but also the alignment of arrays (such as each training example will be placed on its own row) similar to the original MATLAB code. The comments and instructions in the notebooks follow those of the original matlab files and therefore may be irrelevant for the python implementation.

In most cases matplotlib has been used for the data visualisations, but where were an animation was required I've used bqplot (such as in programming exercise 7).

As an alternative to MATLAB minimisation functions I have used the scipy.optimise.minimise function.
For reading in the .mat data files I have used scipy.io.
For the support vector machines in programming exercise 6 I have used the sklearn.svm functions, rather than translating the svmTrain.m into python.

Most importantly, if you are currently doing Andrew Ng's Machine Learning course peeking at this code may undermine your own learning process. Although my matlab assignments aren't included in this respository, the python code would give you strong clues on how to answer the assignments.
