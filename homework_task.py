import pandas as pd
import random

"""
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?"""

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

a = []
b = []
for name, values in data["whoAmI"].iteritems():
  if (values == "human"):
    a.append(1)
  else:
    a.append(0)
  if values == "robot":
    b.append(1)
  else:
    b.append(0)
res_df = pd.DataFrame({"human": a, "robot": b})
print(res_df)