from pathlib import Path
import pandas as pd
from firebase_admin import firestore


class DataLoading(object):

    def load_file(self):
        db = firestore.client()
        doc_ref = db.collection(u'syllabus').stream()
        # my_dir_path = Path("D:\SLIIT\Y4S1\CDAP\Develop\Data")
        df1 = pd.DataFrame(columns=['name', 'html_text', 'grade', 'chapter', 'section'])
        for file in doc_ref:
            # for file in my_dir_path.iterdir():
            # my_file = open(file, 'r')
            # my_text = my_file.read()
            # my_file.close()
            df1.loc[len(df1)] = [file.id, file.to_dict()['content'], file.to_dict()['grade'], file.to_dict()['chapter'],
                                 file.to_dict()['section']]

        print('data loaded')
        return df1
