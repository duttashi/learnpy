# load library
import pandas as pd, numpy as np, matplotlib.pyplot as plt
# create some dummy data
ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
# show the data
print(ts)
# make a line plot
ts.plot(x="some text",y="some more text")
plt.show()
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
#df2.plot.box()
#df.plot.hist()
df.plot.line()
plt.show()
