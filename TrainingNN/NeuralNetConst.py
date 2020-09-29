def Output(InputData: float, Weights: list): #Функция прогона нейронки
    Out = 0
    for i in range(len(Weights)):
        Out += Weights[i] * InputData
    return Out

def Error(Output: float, TrueOutput: float): #Функция выделения ошибки
    return (TrueOutput - Output) * 0.1 
    #Данная нейронка слишком быстро "учится" поэтому если нужно посмотреть процесс обучения, то умножайте ошибку на еще меньшее значение
    #Но тогда повышется процент ошибки 

def WeightsUpdate(Weights: list, Error: float): #Функция обновления весов, через метод обратного распространения ошибки
    UpdateWeights = []
    for i in range(len(Weights)):
        UpdWeight = Weights[i]
        WeightSum = 0
        for j in range(len(Weights)):
            WeightSum += Weights[j]
        UpdateWeights.append(UpdWeight + UpdWeight / WeightSum * Error)
    return UpdateWeights

def NeuralNetwork(Weights: list, InputArray: list): #Точка входа нейронки
    Result = []
    for i in range(len(InputArray)):
        Result.append(Output(InputArray[i], Weights))
    return Result

import random as rd

def main():
    #TestArray и ResultArray можно увеличть по желанию и менять данные в TestArray
    TestArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
    ResultArray = []
    for i in range(len(TestArray)):
        ResultArray.append(TestArray[i] * 2) 
    #вместо двойки можно вписать любую константу
    #Можно удалить данный цикл и вписать в ResultArray данные с "шумами", а также с ошибками
    #Или можно воспользоватся этой конструкцией
    '''
    for i in range(len(TestArray)):
        ResultArray.append(TestArray[i] * Const + rd.randint(0, 100) / 100 - rd.randint(0,100) / 100)
    '''
    #Что обечпечивает "шумы" в диапозоне [Number * Const - 1; Number * Const + 1]

    Weight = [rd.randint(1,10) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100,
                rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100, rd.randint(1,100) / 100] 
    #Веса нейронов (деление на 100 можно убрать, а также использовать вместо функции randint функцию random, ибо это ничего принципиально не меняет)

    for i in range(10000): #Цикл обучения. Можно вписать любое количество итераций 
        for j in range(len(TestArray)):
            Out = Output(TestArray[j], Weight)
            Err = Error(Out, ResultArray[j])
            Weight = WeightsUpdate(Weight, Err)

    TestInputs = [
        [1,6,8,9,3,5], 
        [7,3,4,5,6,7],
        [88,23,512,1,2,7],
        [67,22,1,67,22,4] 
    ] #Данный для проверки обучения нейронной сети (можно вписать любые)

    for i in range(len(TestInputs)):
        print(NeuralNetwork(Weight,TestInputs[i])) #Вывод результата работы нейронки
        
if __name__ == "__main__":
    main()
