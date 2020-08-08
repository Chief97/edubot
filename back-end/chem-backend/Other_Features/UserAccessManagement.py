import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class UserAccessManagement(object):

    def initialization(self):
        """
        Initialising firebase
        :return:
        """
        cred = credentials.Certificate('../firebase-sdk.json')
        firebase_admin.initialize_app(cred)

    def registerUser(self, userObject):
        """
        Inserting user to database
        :param userObject: user details
        :return: response of user registration(successful or failed)
        """
        db = firestore.client()
        doc_ref = db.collection('user').document(userObject['username'])
        doc = doc_ref.get()
        if doc.exists:
            print("Username already exists")
            return "Username already Exists"
        else:
            doc_ref = db.collection('user').document(userObject['username'])
            result = (doc_ref.set({
                'firstName': userObject["firstName"],
                'lastName': userObject["lastName"],
                'age': userObject["age"],
                'username': userObject["username"],
                'password': userObject["password"],
                'gender': userObject["gender"],
                'dob': userObject["dob"],
                'email': userObject["email"]
            }))
            if result != "":
                return "User was successfully registered"
            else:
                return "User was not successfully registered. Please try again"

    def validateUserCredentials(self, credentials):
        """
        validating user credentials
        :param credentials: username and password
        :return: response of user login(successful or failed)
        """
        usersUsername = credentials['username']
        usersPassword = credentials['password']
        db = firestore.client()
        doc_ref = db.collection('user').document(usersUsername)
        doc = doc_ref.get()
        if doc.exists:
            data_dic = doc.to_dict()
            if data_dic["password"] == usersPassword:
                print("User successfully logged in")
                return "User is successfully logged in"

            else:
                print("Invalid password")
                return "Invalid Password"
        else:
            print("User does not exists")
            return "User does not exists"
