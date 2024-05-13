import pandas as pd

Education2018 = pd. read_csv("../data/Education_2018.csv")
Education2022 = pd. read_csv("..data/Eduacation_2022.csv")

print (Education2018.tail(20))
print (Education2022.tail(20))