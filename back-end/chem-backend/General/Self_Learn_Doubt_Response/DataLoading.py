from pathlib import Path
import pandas as pd


class DataLoading(object):

    def load_file(self):
        my_dir_path = Path("D:\SLIIT\Y4S1\CDAP\Develop\Data")
        df = pd.DataFrame(columns=['name', 'html_text'])
        for file in my_dir_path.iterdir():
            my_file = open(file, 'r')
            my_text = my_file.read()
            my_file.close()
            df.loc[len(df)] = [file.name, my_text]
        return df
