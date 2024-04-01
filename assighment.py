import queue
my_queue = queue.Queue()
userName=input("Enter your name: ")
def call():
    print(" ")
    password = input("Enter the password: ")


    def check_repeating_chars(password):
        for i in range(len(password) - 2):
            if password[i] == password[i + 1] == password[i + 2]:
                return True
        return False

    def has_consecutive_sequence(password):
        for i in range(len(password)-2):
            for j in range(len(userName)-2):
                if password[i] == userName[j] and password[i+1]==userName[j+1] and password[i+2]==userName[j+2]:
                    return True
        return False


    def is_valid_password(password):
        if has_consecutive_sequence(password):
            return False
        return True

    if len(password) >= 10:
        uppercase_count = sum(1 for char in password if char.isupper())
        lowercase_count = sum(1 for char in password if char.islower())
        digit_count = sum(1 for char in password if char.isdigit())
        special_char_count = sum(1 for char in password if char in '!@#$%^&*()')

        if uppercase_count < 2:
            print("Invalid password: At least 2 uppercase letters required.")
            call()
        elif lowercase_count < 2:
            print("Invalid password: At least 2 lowercase letters required.")
            call()
        elif digit_count < 2:
            print("Invalid password: At least 2 digits required.")
            call()
        elif special_char_count < 2:
            print("Invalid password: At least 2 special characters required.")
            call()
        elif has_consecutive_sequence(password):
            print("Invalid password: Consecutive sequence of characters from user name not allowed.")
            call()
        elif check_repeating_chars(password):
            print("Invalid password: Repeating characters not allowed.")
            call()
        else:
            is_present = password in list(my_queue.queue)
            if is_present:
                print("Already used password")
                call()
            else:
                print("Valid password")
                my_queue.put(password)
                if my_queue.qsize() > 3:
                    my_queue.get()
                print("-------------------")
                reply=input("type yes to continue : ")
                if reply.lower()=="yes":
                    call()
                else:
                    exit()
    else:
        print("Invalid password: Password should be at least 10 characters long.")
        call()


call()

