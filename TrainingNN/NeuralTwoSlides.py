'''def MatrixVector(Matrix: list, Vector: list):
    ProductMatrix = []
    for i in range(len(Vector)):
        tempArray = []
        for j in range(len(Matrix[i])):
            tempArray.append(Matrix[i][j] + Matrix[i][j] * Vector[i])
        ProductMatrix.append(tempArray)
    return ProductMatrix''' 
#Данная функция должны была умножать матрицу на вектор, но она не пригодилась, а удалять не хочется.
        
def Output(Weights1: list, Weights2: list, TestData: list):
    preOut = []
    Out = 0
    for i in range(len(Weights1)):
        temp = 0
        for j in range(len(Weights1[i])):
            temp += Weights1[i][j] * (TestData[0] + TestData[1])
        preOut.append(temp)
    for i in range(len(preOut)):
        Out += preOut[i] * Weights2[i]
    return Out

def Error(NeuralResult: float, TrueResult: float):
    return (TrueResult - NeuralResult) * 0.1

def UpdateWeights(Weights1: list, Weights2: list, Error: float): #Функция обновления весов
    updWeights2 = []
    updWeights1 = []
    for i in range(len(Weights2)):
        updWeights2.append(Weights2[i] + Weights2[i] * Error * 0.001)
    err = 0
    for i in range(len(updWeights2)):
        err += updWeights2[i] - Weights2[i]
    for i in range(len(Weights1)):
        tempWeights1 = []
        for j in range(len(Weights1[i])):
            tempWeights1.append(Weights1[i][j] + Weights1[i][j] * err * 0.0025)
        updWeights1.append(tempWeights1)
    return [updWeights1, updWeights2]
        
def NeuralEdu(Weights1: list, Weights2: list, TestInput: list, TrueResults: list, Loop: int): #Функция обучения
    eduWeights1 = Weights1
    eduWeights2 = Weights2
    for i in range(Loop):
        for j in range(len(TestInput)):
            Out = Output(eduWeights1, eduWeights2, TestInput[j])
            Err = Error(Out, TrueResults[j])
            UpdateW = UpdateWeights(eduWeights1, eduWeights2, Err)
            eduWeights1, eduWeights2 = UpdateW[0], UpdateW[1]
    return [eduWeights1, eduWeights2]

def NeuralWork(Weights1: list, Weights2: list, InputData: list): #Функция запуска нейронки
    Result = []
    for i in range(len(InputData)):
        Result.append(Output(Weights1, Weights2, InputData[i]))
    return Result

import random as rd

def main():

    Weights1 = [
        [rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100],
        [rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100],
        [rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100]
    ]

    Weights2 = [rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100]

    TestArray = [ [1,1], [0,0], [1,0], [1,1], [0,1], [0,0], [1,1], [0,1], [0,1], [1,1], [1,0] ]
    #ResultArray = [1,0,1,1,1,0,1,1,1,1,1] #Массив конъюкции
    ResultArray = [1,0,0,1,0,0,1,0,0,1,0] #Массив дизъюнкции

    Edu = NeuralEdu(Weights1, Weights2, TestArray, ResultArray, 10000)
    Weights1, Weights2 = Edu[0], Edu[1]
    
    TestData = [ [1,1], [0,1], [0,0], [1,1], [1,0], [1,1] ]

    print(NeuralWork(Weights1, Weights2, TestData)) #Вывод результата работы

if __name__ == "__main__":
    main()