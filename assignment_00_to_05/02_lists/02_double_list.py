#Write a program that doubles each element in a list of numbers. For example, if you start with this list:

def double_list():
    list_num : list = [ 2 ,3 ,4 ,5 ]
    for i in range(len(list_num)):
        list_double = list_num[i]        #store varibale
        list_num[i] = list_double * 2    # double list

    print(list_num)

if __name__ =='__main__':
    double_list()