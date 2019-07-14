def square(get):
    get_list=get.replace(" ","").split(',')
    if len(get_list)>1:
        for i in range(len(get_list)):
            print(f"square({get_list[i]}) => {(int(get_list[i]))**2}")
    else:
        get=int(get)
        getup=get**2
        print(f"square({get}) => {getup}")
    
get=input()
square(get)