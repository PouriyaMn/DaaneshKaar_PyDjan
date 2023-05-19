from uuid import uuid4
import hashlib


class User:
    users_object_dict = {}

    def __init__(self, username, password, phone_number=None):
        self.username = username
        self.__password = password
        self.phone_number = phone_number
        self.id = self.generate_id()
        self.users_object_dict[self.username] = self

    @staticmethod
    def generate_id():
        temp = str(uuid4()).split("-")
        return temp[0]
    
    @classmethod
    def sign_up(cls, username, password, phone_number=None):
        message = "\n!!! WARNING !!!\n"
        if cls.is_username_exist(username):
            message += "this username already taken!\n"
        if not cls.is_pass_valid(password):
            message += "length of password must be more than 4 character!!\n"
        
        if message != "\n!!! WARNING !!!\n":
            return message
        password = cls.hashed_password(password)
        cls(username, password, phone_number)
        return "\nSign Up was successful ^____^"
    
    @classmethod    
    def is_username_exist(cls, username) -> bool:
        if username in cls.users_object_dict or len(username) == 0:
            return True
        return False

    @staticmethod
    def is_pass_valid(password) -> bool:
        if len(password) < 4:
            return False
        return True

    @staticmethod
    def hashed_password(psw: str) -> str:
        password = psw.encode('utf-8')

        # Create a SHA-256 hash object
        hash_object = hashlib.sha256()

        # Update the hash object with the password
        hash_object.update(password)

        # Get the hashed password as a hex string
        hashed_password = hash_object.hexdigest()

        return hashed_password   
    
    @classmethod
    def log_in(cls, input_username, input_password):
        if input_username not in cls.users_object_dict:
            raise KeyError
        
        info = cls.users_object_dict[input_username]
        
        if info.__password != cls.hashed_password(input_password):
            raise ValueError
        
        return info

    def change_phone_number(self,input_phone_number):
        info = self.users_object_dict[self.username]
        # change = info.phone_number = input_phone_number
        # return change
        info.phone_number = input_phone_number

    def change_username(self,new_username):
        if new_username in self.users_object_dict:
            raise KeyError
        
        info = self.users_object_dict[self.username]
        oldname = info.username
        info.username = new_username
        new_info = info
        new_key_values_dict = {new_username: new_info}
        self.users_object_dict.pop(oldname) 
        return self.users_object_dict.update(new_key_values_dict)

    def __str__(self) -> str:
       return f"Username\t>>>\t{self.username}\n\
Phone Number\t>>>\t{self.phone_number}\n\
ID\t\t>>>\t{self.id}"


def main():
    print()
    user1 = User('pouriya', 123123, 989357974386)
    user2 = User('pariya', 9875)
    user3 = User('amir', 818181, 91234534)
    # print(vars(user1))
    # print()
    # print(user1.users_dict)
    # my_dict = {}
    # my_dict[user1.username] = user1
    # my_dict[user2.username] = user2
    # my_dict[user3.username] = vars(user3)
    # print(my_dict)
    print(f"{user1= }")
    print(f"{user1.phone_number= }")
    print()
    user1.change_phone_number("0912399942222")
    print(f"{user1= }")
    print(f"{user1.phone_number= }")


    # print(Users.users_dict)
    # print(Users.users_dict.keys())
    # names =Users.users_dict.keys()
    # print(names)
    # print("pouriya" in names)


if __name__ == "__main__":
    main()