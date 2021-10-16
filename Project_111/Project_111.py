import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

dataset = pd.read_csv('medium_data.csv')
dataset = dataset["reading_time"].to_list()

interventionData = pd.read_csv('interventionData.csv')
interventionData = interventionData["reading_time"].to_list()

def oneMeanByOne(dataPoints):
    meanList = []
    for i in range(0, dataPoints):
        randomInteger = random.randint(0, len(dataset)-1)
        meanList.append(dataset[randomInteger])
    mean = statistics.mean(meanList)
    return mean

def graph(list, interventionMean):
    mean = statistics.mean(list)
    standardDeviation = statistics.stdev(list)
    sigma, negativeSigma = mean + standardDeviation, mean - standardDeviation
    sigma2, negativeSigma2 = mean + 2*standardDeviation, mean - 2*standardDeviation
    sigma3, negativeSigma3 = mean + 3*standardDeviation, mean - 3*standardDeviation

    figure = ff.create_distplot([list], ["Reading Time"], show_hist = False)
    figure.add_trace(go.Scatter(x = [mean, mean], y = [0,10], mode = "lines", name = "Mean"))
    figure.add_trace(go.Scatter(x = [interventionMean, interventionMean], y = [0,10], mode = "lines", name = "Intervention Mean"))

    figure.add_trace(go.Scatter(x = [sigma, sigma], y = [0,10], mode = "lines", name = "Sigma"))
    figure.add_trace(go.Scatter(x = [negativeSigma, negativeSigma], y = [0,10], mode = "lines", name = "Negative Sigma"))

    figure.add_trace(go.Scatter(x = [sigma2, sigma2], y = [0,10], mode = "lines", name = "Two Sigma"))
    figure.add_trace(go.Scatter(x = [negativeSigma2, negativeSigma2], y = [0,10], mode = "lines", name = "Negative Two Sigma"))

    figure.add_trace(go.Scatter(x = [sigma3, sigma3], y = [0,10], mode = "lines", name = "Three Sigma"))
    figure.add_trace(go.Scatter(x = [negativeSigma3, negativeSigma3], y = [0,10], mode = "lines", name = "Negative Three Sigma"))

    figure.show()

def setup():
    newMean = statistics.mean(interventionData)
    samplesMean = []
    for i in range(0, 100):
        meanSet = oneMeanByOne(30)
        samplesMean.append(meanSet)
    graph(samplesMean, newMean)

    zScore = (newMean - statistics.mean(samplesMean))/statistics.stdev(samplesMean)
    print(zScore)


setup()