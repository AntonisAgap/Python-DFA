
# open the file object to read
raw_info = open(r"C:\Users\user\Documents\Computational theory\Dfa.txt").readlines()

# convert a string to list

def Convert(string): 
    li = list(string.split(" ")) 
    li = [i for i in li]
    return li 

def check_state(string,delta,F,s):
    current_state = s[0]
    for char in string:
        flag = 1
        for transition in delta:
            if transition[0] == current_state:
                if transition[1] == char:
                    current_state = transition[2]
                    flag = 0
                    break
        if flag:
            return False
    if current_state in F:
        return True
    else:
        return False

info = []
for string in raw_info:
    string = string.replace('\n','')
    info.append(Convert(string))

Q_number = info[0]
Q = []
for i in range(int(Q_number[0])):
    Q.append(str(i))

S = info[1]
s = info[2]
F = info[3]

delta = []
for i in range(4,len(info)):
    delta.append(info[i])

string = ''
while True:

    print("-----MENU-----")
    print("1. Enter a string.")
    print("2. Exit program")
    option = input("Choose an option: ")
    if option == "2":
        print("Exiting Program...")
        break
    if option == "1":
        string = input("Enter a string: ")
        str_lst = []
        for char in string:
            str_lst.append(char)
        if  check_state(str_lst,delta,F,s):
            print('Accepted!')
        else:
            print('Denied!')

    else: 
        print("Wrong option")
