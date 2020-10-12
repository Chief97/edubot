from pathlib import Path
import pandas as pd


class DataLoading(object):

    def load_file(self):
        my_dir_path = Path("D:\Data")
        df1 = pd.DataFrame(columns=['name', 'html_text'])
        for file in my_dir_path.iterdir():
            my_file = open(file, 'r')
            my_text = my_file.read()
            my_file.close()
            df1.loc[len(df1)] = [file.name, my_text]
        return df1
