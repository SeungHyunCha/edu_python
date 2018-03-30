import pickle

def start_program():
    address_book = {}
#     address_book_size = 0
    
    def register():
        print("**** address reg ****")
        fname = input("name:")
        ftel = input("tel:")
        faddr = input("addr:")
        address_book[fname] = {'fname':fname, 'ftel':ftel, 'faddr':faddr}
#         address_book_size += 1
        
    def print_all():
        print("**** address print ****")
        f = open("address_book", "rb")
        address_book = pickle.load(f)
        key = list(address_book)
        for addr in key:
            print(address_book[addr])
    
    def search():
        print("**** address search ****")
        f = open("address_book", "rb")
        address_book = pickle.load(f)
        key = list(address_book)
        name = input("name?")
        if name in key:
            print(address_book[name])
        else: pass
        
    def save():
        f = open("address_book", "wb")
        pickle.dump(address_book, f)
        f.close()
        print("***** address book save ****")
        
    def show_menu():
        while True: # print menu
            menu = input("1.register, 2.print_all, 3. search, 8. save, 9. exit>")
            menu = int(menu)
            if menu == 9:
                break # while exit
            if menu == 1:
                register()
            elif menu == 2:
                print_all()
            elif menu == 3:
                search()
            elif menu == 8:
                save()
            else: break
    
    show_menu()
    
start_program()