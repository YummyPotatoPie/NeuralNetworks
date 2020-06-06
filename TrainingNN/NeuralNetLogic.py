def Output(Weights: list, DataArray: list): #Функция прогонки нейронки
    Out = 0
    InputSum = 0
    for j in range(len(DataArray)):
            InputSum += DataArray[j]
    for i in range(len(Weights)):
        Out += Weights[i] * InputSum
    return Out

def Error(Output: float, TrueResult: float): #Функция выделения ошибки
    return (TrueResult - Output) * 0.1

def WeightsUpdate(Weights: list, Error: float):
    WeightsUpd = []
    for i in range(len(Weights)):
        Sum = 0
        for j in range(len(Weights)):
            Sum += Weights[j]
        WeightsUpd.append(Weights[i] + Weights[i] / Sum * Error)
    return WeightsUpd

def NeuralEdu(Weights: list, EduArray: list, ResultArray: list, Loop: int): #Функция обучения нейронки
    EduWeights = Weights
    for i in range(Loop):
        for j in range(len(EduArray)):
            Out = Output(EduWeights, EduArray[j])
            Err = Error(Out, ResultArray[j])
            EduWeights = WeightsUpdate(EduWeights, Err)
    return EduWeights

def NeuralWork(Weights: list, InputArray: list): #Функция запуска обученной нейронки
    Result = []
    for i in range(len(InputArray)):
        Result.append(Output(Weights, InputArray[i]))
    return Result

def NearInt(ResultArray: list):
    ResultInt = []
    for i in range(len(ResultArray)): #Если результат больше 0.5, то будем считать, что результатом логической операции будет 1
        if ResultArray[i] > 0.5:
            ResultInt.append(1)
        else:
            ResultInt.append(0)
    return ResultInt

import random as rd

def main():
    Weights = [rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100]
    #Количество нейронов может быть любым
    #Вместо rd.randint(a,b) можно использовать rd.random()

    TestArray = [ [1,1], [0,0], [1,0], [1,1], [0,1], [0,0], [1,1], [0,1], [0,1], [1,1], [1,0] ] 

    #ResultArray = [1,0,1,1,1,0,1,1,1,1,1] #Массив конъюкции
    ResultArray = [1,0,0,1,0,0,1,0,0,1,0] #Массив дизъюнкции
    #По желанию можно использовать любой массив, а также увеличить количество входных данных в TestArray и ResultArray

    Weights = NeuralEdu(Weights, TestArray, ResultArray, 1000)

    Data = [ [1,1], [0,1], [0,0], [1,1], [1,0], [1,1] ] #Тестовый массив 

    Result = NeuralWork(Weights, Data)

    print(Result) #Выводит результат работы нейронки
    print(NearInt(Result)) #Выводит результат округления

if __name__ == "__main__":
    main()