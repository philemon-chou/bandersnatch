from altair import Chart, Tooltip
from pandas import DataFrame

'''This page is meant to connect the graph function with the main.py.
with each of the variables (x,y,color,etc) connecting to what the functionality of main.py is calling for.'''


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    )
    return graph

if __name__ == '__main__':
    pass
