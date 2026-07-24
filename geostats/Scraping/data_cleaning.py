import pandas as pd
import os,re,string

def clean_index(df,pattern = 'Unnamed'):
    """[summary]

    Args:
        df ([type]): [description]
        pattern (str, optional): [description]. Defaults to 'Unnamed'.

    Returns:
        [type]: [description]
    """
    try:
        cname = df.columns
        cIndex = [s for s in cname if pattern in s]
        for index in cIndex[1:]:
            del df[index]
        return df
    except Exception as e:
        print(e.strerror)

def dfmerge(df1,df2,keys,method = 'rbind'):
    """[summary]

    Args:
        df1 ([type]): [description]
        df2 ([type]): [description]
        keys ([type]): [description]
        method (str, optional): [description]. Defaults to 'rbind'.

    Returns:
        [type]: [description]
    """
    try:
        if(method == 'rbind'):
            df3 = pd.concat([df1, df2], axis=0, sort=False).drop_duplicates(keys,keep='last').reset_index(drop=True)
        elif (method == 'cbind'):
            df3 = pd.concat([df1.reset_index(drop=True), df2], axis=1, sort=False).drop_duplicates(keys,keep='last').reset_index(drop=True)
        else:
            print('Please Select Right Merge Method (rbind / cbind)')
        return df3
    except Exception as e:
        print(e.strerror)

def list2string(list1,Combin_Oprator = ' ',pattern = u'\xa0'):
    """[summary]

    Args:
        list1 ([type]): [description]
        Combin_Oprator (str, optional): [description]. Defaults to ' '.
        pattern (unicode, optional): [description]. Defaults to u'\xa0'.

    Returns:
        [type]: [description]
    """
    try:
        k=[]
        for word in list1:
            word_clean = str(word).replace(pattern, u'')
            if(word_clean):
                k.append(word_clean)
        k = Combin_Oprator.join(k)
        return k
    except Exception as e:
        print(e.strerror)

def clean_punctuation(article):
    """[summary]

    Args:
        article ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        clean1 = re.sub(r'['+string.punctuation + '’—”'+']', "", article)
        return re.sub(r'\W+', ' ', clean1)
    except Exception as e:
        print(e.strerror)

def clean_punctuationList(stringList):
    """[summary]

    Args:
        stringList ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        return list(map(clean_punctuation,stringList))
    except Exception as e:
        print(e.strerror)