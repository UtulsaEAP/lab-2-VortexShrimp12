def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    phone_number = str(phone_number)
    print("(" + phone_number[0:3] + ")" + " " + phone_number[3:6] + "-" + phone_number[6:10])
if __name__ == "__main__":
    telephone()