#my_list = [0,1,2,3]
#my_list.append(6)
#my_list.insert(2,7)
#my_list.remove(1)

#my_list = [0,1,2,3]
#pop_list = my_list.pop(2)

#this_tuple = ("apple", "banana", "cherry", "banana", "cherry")
#print(this_tuple)       

today = input('masukan hari:')

match today:
    case "senin":
        print('Masuk Kuliah')
    case "selasa":
        print('Libur Kuliah')
    case "sabtu":
        print('Masuk Kuliah')
    case _:
        print('Masukan kata dengan benar')