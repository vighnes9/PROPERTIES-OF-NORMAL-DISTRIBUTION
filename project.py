import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
data = df["Reading score"].tolist()



mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev()

first_std_dev_start,first_std_dev_end = mean-std_dev,mean+std_dev
second_std_dev_start,second_std_dev_end = mean-(2*std_dev),mean+(2*std_dev)



fig = ff.create_distplot([data], ["result"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines", name="std_dev1"))
fig.add_trace(go.Scatter(x = [first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines", name="std_dev1"))
fig.add_trace(go.Scatter(x = [second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines", name="std_dev2"))
fig.add_trace(go.Scatter(x = [second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines", name="std_dev2"))
fig.show()

list_of_data_within_1_std_dev = [result for result in data if result>first_std_dev_start and result<first_std_dev_end]
list_of_data_within_2_std_dev = [result for result in data if result>second_std_dev_start and result<second_std_dev_end]

print("mean = {} ".format(mean))
print("median = {} ".format(median))
print("mode = {} ".format(mode))
print("std_dev = {} ".format(std_dev))
print("{}% of data lies within 1 std_dev".format(len(list_of_data_within_1_std_dev)*100.0/len(data)))
print("{}% of data lies within 2 std_dev".format(len(list_of_data_within_2_std_dev)*100.0/len(data)))