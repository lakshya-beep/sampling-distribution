import random
import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff


df=pd.read_csv("newdata.csv")
data=df['average'].tolist()
fig=ff.create_distplot([data],["average"],show_hist=False)
#fig.show()

avg_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("the mean of the data is ->           ",avg_mean)
print("standard deviation of the data is -> ",std_deviation)

#dataset=[]
#for i in range(0,100):
#    random_index=random.randint(0,len(data))
#    value=data[random_index]
#    dataset.append(value)
#mean=statistics.mean(dataset)
#std_deviation=statistics.stdev(dataset)
#print("the mean of the data od dataset is ->    ",mean)
#print("standard deviation of the dataset is -> ",std_deviation)

#funtion to get the mean of the given data sample
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

#funtion to phot the mean on the graph
def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([data],["average"],show_hist=False)
    fig.show()


#funtion to get mean of 100 data points 1000 times and plot their graph
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()

#code to find the mean of the raw data
population_mean=statistics.mean(data)
print('population mean -> ',population_mean)

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    standard_deviation=statistics.stdev(mean_list)
    print("standard deviation of sampling distribution ->", standard_deviation)

standard_deviation()
