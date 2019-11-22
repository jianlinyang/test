import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data = data.cumsum()

data.plot()
pl.show()
