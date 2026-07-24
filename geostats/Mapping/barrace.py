import numpy as np
import pandas as pd

def randcolor(num = 1,style = 'rgba',precise = 0.001):
    """[summary]

    Args:
        num (int, optional): [description]. Defaults to 1.
        style (str, optional): [description]. Defaults to 'rgba'.
        precise (float, optional): [description]. Defaults to 0.001.

    Returns:
        [type]: [description]
    """
    colors = []

    if len(list(style)) == 4:
        for x in range(0,num):
            colors.append(np.concatenate((np.random.choice(range(int(1./precise)), size=3) / (1./precise),[1.0])))
    elif len(list(style)) == 3:
        for x in range(0,num):
            colors.append(list(np.random.choice(range(int(1/precise)), size=3) / (1/precise)))
    return colors


def top_filter(df,n = 1,ascending = False,axis=0):
    """[summary]

    Args:
        df ([type]): [description]
        n (int, optional): [description]. Defaults to 1.
        ascending (bool, optional): [description]. Defaults to False.
        axis (int, optional): [description]. Defaults to 0.

    Returns:
        [type]: [description]
    """
    f = lambda x: x.where(x > x.sort_values(ascending = ascending)[n+1])
    df1 = df.copy()
    df = df.apply(f,axis=axis)
    df1.drop(df.index[df.isnull().all(1)],inplace=True)
    return df1


def nice_axes(ax):
    ax.set_facecolor('1')
    ax.tick_params(labelsize=8, length=0)
    ax.grid(True, axis='x', color='lightgrey')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]

def prepare_data(df,steps = 10):
    df = df.reset_index()
    df.index = df.index * steps
    last_idx = df.index[-1] + 1
    df_expanded = df.reindex(range(last_idx))
    df_expanded['index'] = df_expanded['index'].fillna(method='ffill')
    df_expanded = df_expanded.set_index('index')
    df_expanded = df_expanded.apply(pd.to_numeric, errors='coerce')
    df_rank_expanded = df_expanded.rank(axis=1, method='first')
    df_expanded = df_expanded.interpolate()
    df_rank_expanded = df_rank_expanded.interpolate()
    return df_expanded, df_rank_expanded

