import numpy as np

def threshold(imgArray):
    arrayOfAverageNumber = []
    newArray = imgArray
    for eachRow in imgArray:
        for eachPixel in eachRow:
            averageNumber = np.mean(eachPixel[:3])
            arrayOfAverageNumber.append(averageNumber)
    balance = np.mean(arrayOfAverageNumber)

    for eachRow in newArray:
        for eachPixel in eachRow:
            if np.mean(eachPixel[:3]) > balance:
                eachPixel[0] = 255
                eachPixel[1] = 255
                eachPixel[2] = 255
                eachPixel[3] = 255
            else:
                eachPixel[0] = 0
                eachPixel[1] = 0
                eachPixel[2] = 0
                eachPixel[3] = 255
    return newArray