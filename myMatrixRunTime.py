class myMatrix:
    def __init__(self, m, n, empty = False):#initializing
            if m <= 0 or n <= 0 or m > 500000 or n > 500000: 
                print("Matrix demensions should be between 0 and 500000. Try again!")
                self.data = None
                return None
            else: #matrix creation
                self.data = []
                for i in range(m):
                    self.data.append([])
                    for j in range(n):
                        if empty is True:
                            self.data[i].append(0)
                        else:
                            self.data[i].append((i + 1) * (j + 1))

    def __mul__(self, matrix): #multiply one matrix with another matrix
        if type(matrix) == int or type(matrix) == float:
            result = myMatrix(m = len(self.data), n = len(self.data[0]), empty = True)
            result.data = [[self.data[i][j] * matrix2 for j in range(len(self.data[i]))] for i in range(len(self.data))]
            return result
        else:
            result = myMatrix(m = len(self.data), n = len(matrix.data[0]), empty = True)
            for i in range(len(self.data)):
                    for j in range(len(matrix.data[0])):
                        for k in range(len(matrix.data)):
                            result.data[i][j] += self.data[i][k] * matrix.data[k][j]
            return result

    def __rmul__(self, value): #multiply matrix with a integer scalar value
        result = myMatrix(m = len(self.data), n = len(self.data[0]), empty = True)
        result.data = [[self.data[i][j] * value for j in range(len(self.data[i]))] for i in range(len(self.data))]
        return result

    def __pow__(self, power): #raise matrix to power on an integer value
        result = myMatrix(m = len(self.data), n = len(self.data[0]), empty = True)
        result.data = [[self.data[i][j] ** power for j in range(len(self.data[i]))] for i in range(len(self.data))]
        return result

    def __truediv__(self, divisor): # divide matrix by a integer value
        if divisor == 0:#check for divide by 0 and catch error
            raise ZeroDivisionError
        result = myMatrix(m = len(self.data), n = len(self.data[0]), empty = True)
        result.data = [[self.data[i][j] / divisor for j in range(len(self.data[i]))] for i in range(len(self.data))]
        return result

    def sum(self): #sum of all elements of a matrix
        total = 0
        for i in range(len(self.data)):
            total += sum(self.data[i])
        return total
#------------------------------------------------------------------------------------------------------------------------
import time

class runTime:
	def __init__(self, m, n):
		self.mat1 = myMatrix(m, n)
		self.mat2 = myMatrix(m, n)

	def multiplicationRunTime(self):
		start = time.time()
		mulResult = self.mat1 * self.mat2
		end = time.time()
		return (end - start) * 1000


dimensionArray = [5, 10, 20, 50, 100, 250]
for value in dimensionArray:
	result1 = runTime(value, value)
	timeSpent = result1.multiplicationRunTime()
	print(value, "X", value, " = ", timeSpent)
