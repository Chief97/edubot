from firebase_admin import firestore
import json

from flask import jsonify


class RetrieveFiles(object):

    def load_chapter(self, grade, chapter):
        db = firestore.client()
        documents = db.collection(u'syllabus').where(u'chapter', u'==', chapter).get()

        document = []

        for i in range(0, len(documents)):
            for j in range(i + 1, len(documents)):
                if documents[i].to_dict()["section"] > documents[j].to_dict()["section"]:
                    temp = documents[i]
                    documents[i] = documents[j]
                    documents[j] = temp

        for doc in documents:
            graded = doc.to_dict()["grade"]
            if graded == grade:
                document.append({"sectionName": f'{doc.id}',
                                "content": f'{doc.to_dict()["content"]}',
                                 "section": f'{doc.to_dict()["section"]}'})
            print(f'{doc.id} => {doc.to_dict()}')
            print(document)

        return jsonify(document)
