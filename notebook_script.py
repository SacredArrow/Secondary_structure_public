import numpy as np
import pandas as pd
import seaborn as sns

sns.set(rc={'figure.figsize':(11.7,8.27)})
df = pd.read_csv("Csvs/out_50_90.csv")
df_out = df[(df.Length <=90) & (df.Length >=50)]
df_out = df_out.reset_index().drop(["index", "ID"], axis = 1)
df_test_knots = df_out[df_out.has_knots == 1].sample(len(df_out[df_out.has_knots == 1])//5) # 20%
df_test_noknots = df_out[df_out.has_knots == 0].sample(len(df_out[df_out.has_knots == 0])//5)
df_test = pd.concat([df_test_knots, df_test_noknots])
df_out = df_out.drop(df_test.index)

df_validate_knots = df_out[df_out.has_knots == 1].sample(len(df_out[df_out.has_knots == 1])//10) # 10%
df_validate_noknots = df_out[df_out.has_knots == 0].sample(len(df_out[df_out.has_knots == 0])//10)
df_validate = pd.concat([df_validate_knots, df_validate_noknots])
df_out = df_out.drop(df_validate.index)

df_out.to_csv("train.csv")
df_test.to_csv("test.csv")
df_validate.to_csv("validate.csv")
