import sys
import numpy as np

print('\n')
print('import numpy as np <- fundemental package for scientific computing with python')
print('we"re going to use it to create and manipulate with arrays')
print('Numpy: {}'.format(np.__version__))
print('\n')
input()

### SCALARS 
x=6
print('SCALARS')
print('Defining a scalar: x=6 and you can use print(x)')
print('\n')
input()

### VECTOR
print('VECTORS')
x=np.array((1,2,3))		# CODE
print('Defining a one dimensional vector: x=np.array((1,2,3))')
dimensions=x.shape		# CODE
print('Vector Dimensions: {}'.format(x.shape))
size=x.size
print('Vector size: {}'.format(x.size))
print('\n')
input()

print('The unit vector - vector with unit form')
print('A unit vector can be obtained by normalizing any vector')
print('Vector normalization is the process of dividing a vectorby its magnitude, which produces a unit vector')
x=[1,1,1,1]
print ('vector x -> ' , x)
print('example of normalization -> x/((1^2+1^2+1^2+1^2)^1/2)=x/(4^1/2)=1/2')
x=[1/2,1/2,1/2,1/2]
print('Unit vector-> ' ,x)
print('normalization improve the perfomance of ML algorithms')
print('We use euclidian norm - > between (0,1)')
print('Normalization is used between the layers of the NN')
print('\n')
input()


### MATRICE
print('MATRICES')
X = np.matrix([[2,4,6],[3,5,7],[8,5,3]])
print('Defining a matrix X = np.matrix([[2,4,6],[3,5,7],[8,5,3]])')
print(X)
print('Matrix dimensions: {}'.format(X.shape))
print('Matrix size: {}'.format(X.size))
# again you can save these parameters like we did with vectors
print('\n')
input()

print('MATRIX OPERATIONS')
Y = np.matrix([[10,11,12],[13,14,15],[16,17,18]])
print('Define a matrix Y = np.matrix([[10,11,12],[13,14,15],[16,17,18]]')
print('Matrices:')
print(X, '\n''\n', Y)

input()
print('Addition: X+Y')
print(X+Y)
 
input()
print('Addition: X-Y')
print(X-Y)

input()
print('Addition: X*Y')
print(X*Y)

input()
print('Addition: X/Y')
print(X/Y)

input()
print('Matrix transponse')
A=np.array(range(9))
print('A=np.array(range(9))')
print(A)
print('A=A.reshape(3,3)')
A=A.reshape(3,3)
print(A)
print('B=A.T')
B=A.T
print(B)
print('transponse of transponse = ORIGINAL matrix')

print('\n')
input()
print('Some matrices and vectors occurmore commonly than others or are particulary useful in ML')
print('Diagonal Matrices - > Dij = 0 for all i!=j ')
print('All the elements equals to 0 except allong the main diagonal')
A=np.matrix([[1,0,0],[0,2,0],[0,0,3]])
print(A)
print('\n')

input()
print('Symetric matrices - across the main diagonal')
print('A symmetric matrix is any matrix that is equal to its transpose')
A=np.matrix([[1,2,3],[2,3,4],[3,4,5]])
print(A)
print('For example distance measurement matrix')

input()
print('Calculate the determinant of matrix X // np.linalg.det(X) // : ')
print(np.linalg.det(X))
input()

print('Defining a matrix of a given dimension')
print('x=np.ones(5,5) or zeros(3,3)')
x=np.ones((5,5))
y=np.zeros((3,3))
print(x,'\n', '\n',y)


input()

print('TENSORS')
x=np.ones((3,3,3))
print('3 dimensional tensor x=np.ones((3,3,3))')
print(x)
print('You can add 4-5-6... dimesional tensors')
print('It gets harder and harder to visualize (2-D screen)')
print('Tensor dimensions: {}'.format(x.shape))
print('Tensor size: {}'.format(x.size))
# Again you can save this like x=x.size or x=x.shape
print('With adding dimensions -> we have exponential increase of number of parameters')

# INDEXING
input()
A=np.ones((5,5), dtype=np.int)
print('A=np.ones((5,5), dtype=np.int)-> data type integers - default FLOAT')
print(A)
print('Idexing starts at 0 -> first element is A[0,0]')
print('print(A[:,0]) -> prints first column or you can assign values')
print('print(A[:,:])')

input()
print('Higher dimension -> A=np.ones((5,5,5), dtype=np.int)')
A=np.ones((5,5,5), dtype=np.int)
print('Assig first row a new value -> A[:,0,0]=6')
A[:,0,0]=6
print(A)

print('\n')
input()
# tensors
print('A=np.ones((3,3,3,3,3,3,3,3,3,3)) - 10d tensor')
A=np.ones((3,3,3,3,3,3,3,3,3,3))

print('Again A.shape for printing dimensions ->' ,len(A.shape))
print('A.size print number of elements - exponential growth ->', A.size)
print('TENSORS- > AI')

