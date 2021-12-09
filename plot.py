import pandas as pd
import plotly.graph_objects as go
import statsmodels.api as sm
import plotly.express as px
import plotly

df = pd.read_csv('dataset.csv')

# Change name of columns
df = df.rename(columns={"2020 [YR2020]":"BNP"})

fig = px.scatter(df, 
    x="BNP",
    y="people_fully_vaccinated_per_hundred",
    color="Country Name",
    labels=dict(x="Fully Vaccinated (per hundred)", y="BDP", color="Country")
    )
fig.update_layout(xaxis_title ='BNP', yaxis_title = "Fully Vaccinated (per hundred)")

# Using statsmodel for regression and add to figure

model = sm.OLS(df['people_fully_vaccinated_per_hundred'],sm.add_constant(df['BNP'])).fit()
print(model.summary())


fig.add_trace(go.Scatter(name='line of best fit', x=df['BNP'], y=model.fittedvalues, mode='lines'))



# show 
plotly.offline.plot(fig)
