import pandas as pd

emp2018 = pd.read_csv("../data/ACSDP1Y2018.DP03-2024-05-09T012103.csv")
emp2022 = pd.read_csv("../data/ACSDP1Y2022.DP03-2024-05-09T012010.csv")

print (emp2018.tail(20))
print (emp2022.tail(20))