import os,glob,subprocess

def to_html(file = None,path = '.'):
    """[summary]
    Args:
        file ([type], optional): [description]. Defaults to None.
        path (str, optional): [description]. Defaults to '.'.
    """
    try:
        if file != None:
            subprocess.run(['jupyter','nbconvert',file])
            print('Convert %s to .html file successful' %str(file))
        else:
            pattern = os.path.join(path,'*.ipynb')
            nb_lst = glob.glob(pattern)
            for nb in nb_lst:
                subprocess.run(['jupyter','nbconvert',nb])
                print('Convert %s to .html file successful' %str(nb))
    except Exception as e:
        print(e.strerror)


def to_script(file = None,path = '.'):
    """[summary]
    Args:
        file ([type], optional): [description]. Defaults to None.
        path (str, optional): [description]. Defaults to '.'.
    """
    try:
        if file != None:
            subprocess.run(['jupyter','nbconvert','--to','script',file])
            print('Convert %s to .py file successful' %str(file))
        else:
            pattern = os.path.join(path,'*.ipynb')
            nb_lst = glob.glob(pattern)
            for nb in nb_lst:
                subprocess.run(['jupyter','nbconvert','--to','script',nb])
                print('Convert %s to .py file successful' %str(nb))
    except Exception as e:
        print(e.strerror)

if __name__ == "__main__":
    input_path = r'G:\Books\Data-Analysis-With-Python\Notebooks\ch-04-Numpy'
    to_html(path = input_path)
    file = r'G:\Books\Data-Analysis-With-Python\Notebooks\ch-04-Numpy\4-5-Linear-algebra.ipynb'
    to_script(file)