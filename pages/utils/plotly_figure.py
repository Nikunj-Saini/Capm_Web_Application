import plotly.graph_objects as go
import dateutil
import datetime

def plotly_table(dataframe):
    headerColor = 'grey'
    rowEvenColor = '#f8fafd'
    rowOddColor = '#e6efff'   # fixed invalid color

    fig = go.Figure(data=[
        go.Table(
            header=dict(
                values=["<b>Index</b>"] + ["<b>" + str(i)[:10] + "</b>" for i in dataframe.columns],
                line_color="#92abc7",
                fill_color='#0078ff',
                align='center',
                font=dict(color='white', size=15),
                height=35
            ),
            cells=dict(
                values=[
                    ["<b>" + str(i) + "</b>" for i in dataframe.index]
                ] + [dataframe[col] for col in dataframe.columns],
                fill_color=[[rowOddColor, rowEvenColor] * (len(dataframe) // 2 + 1)],
                align='left',
                line_color='white',
                font=dict(color='black', size=15)
            )
        )
    ])

    fig.update_layout(height=400, margin=dict(l=0, t=0, b=0))

    return fig