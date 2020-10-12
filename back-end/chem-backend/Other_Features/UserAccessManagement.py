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

    def retrieveUserDetails(self, userObject):
        """
           retrieving user profile details
           :param userObject: username
           :return: response of user profile details
        """
        db = firestore.client()
        doc_ref = db.collection('user').document(userObject['username'])
        doc = doc_ref.get()
        if doc.exists:
            print("User exists")
            data_dic = doc.to_dict()
            response = {
                'firstName': data_dic["firstName"],
                'lastName': data_dic["lastName"],
                'username': data_dic["username"],
                'dob': data_dic["dob"],
                'email': data_dic["email"]
            }
            return response;
        else:
            print("User does not exists")
            return ""

    def updateUserDetails(self, userObject):
        """
           Updating user profile details
           :param userObject: username
           :return: user details updating response
        """
        db = firestore.client()
        doc_ref = db.collection('user').document(userObject['username'])
        doc = doc_ref.get()
        if doc.exists:
            print("User exists")
            first_name = userObject["firstName"]
            last_name = userObject["lastName"]
            username = userObject["username"]
            dob = userObject["dob"]
            email = userObject["email"]
            if first_name != "" and last_name != "" and dob != "" and email != "":
                field_updates = {'firstName': first_name, 'lastName': last_name, 'dob': dob, 'email': email}
                doc_ref.update(field_updates)
                return "User successfully updated"
            else:
                return "User not successfully updated"
        else:
            print("User does not exists")
            return "User does not exists to update"
