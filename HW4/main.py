from pwinput import pwinput # version == 1.0.3
from users import User


while True:
    print("\n\t\t____________________<<<MAIN<>MENU>>>____________________\n")
    print("Welcome to the program :D")
    print("navigate through the menu JUST by enter numbers shortcut^_^")
    option_main = input("\nEnter a number for Sign Up[1], Log In[2] or Exit[0]: ")
    match option_main:
        case "1":
            print("\n\t\t_________________<<SIGN UP>>_________________\n")
            
            print("choose a USERNAME for your account in below")
            sign_up_username = input("Enter your USERNAME here --->>> ")
            
            print("\nchoose a PASSWORD for your account in below")
            print(" * your password must be greater equal 4 characters!")
            sign_up_password = pwinput("Enter your PASSWORD here --->>> ", mask="*")
            
            print("\nenter your Phone Number in below")
            print(" * this field is not necessary, just press ENTER to pass it")
            phone_ = input("Enter your PHONE NUMBER here [ENTER for pass it]--->>> ")
            
            phone_numb = None if phone_ == "" else phone_
            print(User.sign_up(sign_up_username, sign_up_password, phone_numb))

        case "2":
            flag = 0
            while flag == 0:
                print("\n\t\t_________________<<LOG IN>>_________________\n")
                
                username_ = input("enter your USERNAME >>> ")
                password_ = pwinput("enter your PASSWORD >>> ", mask="*")
                
                try:
                    online_user = User.log_in(username_, password_)
                
                except KeyError:
                    print("\n:o :o ERROR >>> User Not Found x_X")
                    question = input("\ndo you want to continue? [Yes=1 or No=0]: ")
                    if question == "1":
                        continue
                    else:
                        break
                
                except ValueError:
                    print("\n:o :o ERROR >>> Incorrect Password :(")
                    question = input("\ndo you want to continue? [Yes=1 or No=0]: ")
                    if question == "1":
                        continue
                    else:
                        break
                else:
                    print("\nLogin Successful ^_^\n")

                while True:
                    print("\n\t------------<Log In Menu>------------\n")
                    print("Enter a number for: ")
                    print("Show Information [1]")
                    print("  Edit Profile   [2]")
                    print(" Change Password [3]")
                    print("     or Exit     [4]")
                    option_log_in = input("\n      --->>>      ")
                    match option_log_in:
                        case "1":
                            print("\n\t--------information--------\n")
                            print(online_user)
                            q1 = input("\ndo you want to continue? [Yes=1 or No=0]: ")
                            if q1 == "1":
                                continue
                            else:
                                flag += 1
                                break
                        case "2":
                            print("\n\t--------edit profile--------\n")
                            print("which field do you want to edit?")
                            field = input("Username[1] or PhoneNumber[2]: ")
                            if field == "1":
                                new_username = input("\nplease enter new Username: ")
                                try:
                                    online_user.change_username(new_username)
                                except KeyError:
                                    print("ERROR >>> this username already exist !!!")
                                    question = input("\ndo you want to continue? [Yes=1 or No=0]: ")
                                    if question == "1":
                                        continue
                                    else:
                                        break
                                else:
                                    print("Username Successfully Changed :D !!")
                                    flag += 1
                                    break

                            elif field == "2":
                                new_phone_number = input("\nplease enter new Phone Number: ")
                                online_user.change_phone_number(new_phone_number)
                            
                            else:
                                print("Error !! Wrong Input !!")
                            
                            q2 = input("\ndo you want to continue? [Yes=1 or No=0]: ")
                            if q2 == "1":
                                continue
                            else:
                                flag += 1
                                break

                        case "3":
                            print("\n\t--------change password--------\n")
                            print("Sorry!! this part is in progress for developing in near future :v ")
                            print("Thank you for your patient in advance ^____^")

                            q3 = input("\ndo you want to continue? [Yes=1 or No=0]: ")
                            if q3 == "1":
                                continue
                            else:
                                flag += 1
                                break

                        case "4":
                            flag += 1
                            break

        case "0":
            break


# print(User.users_object_dict)