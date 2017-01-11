# Visualizing sorting algorithms
# Jason Dean
# Jan 11, 2017


import random
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# _____________ Variables ___________________

randList = []

# _____________ Processing ___________________

# create a list of random numbers to sort
def randNums(size):
    randList = []
    for j in range(0, size):
        randList.append(random.randrange(0, size + 1, 1))

    return randList


# bubble sort
def bubbleSort(randList, fig1):

    counter = 0
    for i in range(len(randList)):
        for j in range(len(randList) - 1):
            counter += 1
            if randList[j] > randList[j + 1]:
                temp = randList[j + 1]
                randList[j + 1] = randList[j]
                randList[j] = temp

        fig1.scatter(xaxis, randList)
        fig1.set_title('Bubble Sort')
        fig1.set_xticklabels([])
        fig1.set_yticklabels([])
        fig1.axis([0, 400, 0, 400])
        plt.pause(0.005)
        fig1.clear()

    fig1.scatter(xaxis, randList)
    fig1.set_title('Bubble Sort')
    fig1.set_xticklabels([])
    fig1.set_yticklabels([])
    fig1.axis([0, 400, 0, 400])
    plt.pause(0.005)

    return randList

# selection sort
def selectionSort(randList, fig2):

    counter =0

    index = 0
    for i in range(len(randList)):
        min = randList[i]
        for j in range(i, len(randList) - 1):
            counter += 1
            if min > randList[j + 1]:
                min = randList[j + 1]
                index = j + 1

        temp = randList[i]
        randList[i] = min
        randList[index] = temp

        fig2.scatter(xaxis, randList)
        fig2.set_title('Selection Sort')
        fig2.set_xticklabels([])
        fig2.set_yticklabels([])
        fig2.axis([0, 400, 0, 400])
        plt.pause(0.005)
        fig2.clear()

    fig2.scatter(xaxis, randList)
    fig2.set_title('Selection Sort')
    fig2.set_xticklabels([])
    fig2.set_yticklabels([])
    fig2.axis([0, 400, 0, 400])
    plt.pause(0.005)

    return randList

def mergeSort(randList, fig3):

    middle = int(len(randList) / 2)

    if (len(randList) < 2):
        return randList

    left = randList[:middle]
    right = randList[middle:]

    mergeSort(left, fig3)
    mergeSort(right, fig3)

    i = 0
    j = 0
    counter = 0

    while j < (len(right)) and i < (len(left)):
        if left[i] < right[j]:
            randList[counter] = left[i]
            i += 1
        else:
            randList[counter] = right[j]
            j += 1
        counter += 1

    while j < len(right):
        randList[counter] = right[j]
        j += 1
        counter += 1

    while i < len(left):
        randList[counter] = left[i]
        i += 1
        counter += 1

    plot = plotMerge(randList)
    plot.plotMS(sortList, randList)

    return randList


class plotMerge(object):

    counter = 0

    def __init__(self, randList):
        plotMerge.counter += len(randList)

    @staticmethod
    def plotMS(randomNums, list):

        for i in range(0, len(list)):
            randomNums[i] = list[i]

        fig3.scatter(xaxis, randomNums)
        fig3.set_title('Merge Sort')
        fig3.set_xticklabels([])
        fig3.set_yticklabels([])
        fig3.axis([0, 400, 0, 400])
        plt.pause(0.005)
        fig3.clear()

# _____________ Input/Output ___________________


# generate a list of random numbers to sort
sortList = randNums(400)

xaxis = list(range(0, 400))

# generate a figure instance and add subplots
fig = plt.figure(figsize=(12, 4))
plt.ion()
gs = gridspec.GridSpec(1, 6)

#fig1 = fig.add_subplot(331)
fig1 = plt.subplot(gs[:, 0:2])
fig1.set_title('Bubble Sort')
fig1.set_xticklabels([])
fig1.set_yticklabels([])
fig1.axis([0, 400, 0, 400])
fig1.scatter(xaxis, sortList)

fig2 = plt.subplot(gs[:, 2:4])
fig2.set_title('Selection Sort')
fig2.set_xticklabels([])
fig2.set_yticklabels([])
fig2.axis([0, 400, 0, 400])
fig2.scatter(xaxis, sortList)

fig3 = plt.subplot(gs[:, 4:])
fig3.set_title('Merge Sort')
fig3.set_xticklabels([])
fig3.set_yticklabels([])
fig3.axis([0, 400, 0, 400])
fig3.scatter(xaxis, sortList)

# sort and visualize
bubbleSort(sortList[:], fig1)
selectionSort(sortList[:], fig2)
mergeSort(sortList[:], fig3)
