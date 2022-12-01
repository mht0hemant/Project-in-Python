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

try:#test cases
        #error case
        error1= myMatrix(-1,3)
        error2 = myMatrix(1,500001)

        #creating matrices
        mat1 = myMatrix(4, 4)
        mat2 = myMatrix(4, 4)
        print("--> Matrix1 = ", mat1.data)
        print("--> Matrix2 = ", mat2.data)

        #matrix multiplication
        multiplication = mat1 * mat2
        print("--> Matrix1 times Matrix2 = ", multiplication.data)

        #scalar multiplication with matrix
        result1 = 5 * mat1
        print("--> Integer '5' multiplication with matrix1 = ", result1.data)
        result2 = 5 * mat2
        print("--> Integer '5' multiplication with matrix1 = ", result2.data)

        #raise matrix to the power of
        power1 = mat1 ** 2
        print("--> Matrix1 raised to the power of 2 = ", power1.data)
        power2 = mat2 ** 2
        print("--> Matrix2 raised to the power of 2 = ", power2.data)
        
        #Integer division to matrix
        division1 = mat1 / 3
        print("--> Matrix1 divided by 3 = ", division1.data)
        division2 = mat2 / 3
        print("--> Matrix2 divided by 3 = ", division2.data)
       

        #sum of all elements of a matrix
        print("--> Sum of all elements of matrix1 = ", mat1.sum())
        print("--> Sum of all elements of matrix2 = ", mat2.sum())

        #division by zero
        division3 = mat1 / 0
        print("--> Matrix1 divided by 0 = ", division3.data)
        print("Nothing is divisible by 0. Go see a doctor.")
        division4 = mat2 / 0
        print("--> Matrix2 divided by 0 = ", division4.data)
        print("Nothing is divisible by 0. Go see a doctor.")

except ZeroDivisionError:
	print("Nothing is divisible by 0. Go see a doctor.")
        
