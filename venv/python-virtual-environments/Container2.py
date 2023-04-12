import re
import pickle
class CLI:
    enpty_name='Not entered'
    def __init__(self,filename):
        self.filename=filename
        self.dictionary={str():set()}
        self.load_dictionary()
        self.current_name=CLI.enpty_name
        self.active_container=set()
        self.loaded=False
        
    def add(self,object):
        if self.current_name in self.dictionary.keys():
            if type(object) is list:
                for item in object:
                    self.active_container.add(item)
            else:
                self.active_container.add(object)
        else:
            print('You shoud switch or registrate a new user to call this function')

    def remove_object(self,object):
        if self.current_name in self.dictionary.keys():
            self.active_container.discard(object)
        else:
            print('You shoud switch or registrate a new user to call this function')

    def find(self,object):
        if self.current_name in self.dictionary.keys():
            if object in self.active_container:
                print(str(object))
            else:
                print('No such elements')
        else:
            print('You shoud switch or registrate a new user to call this function')

    def list(self):
        print(self.active_container,sep=',')

    def print_all_dict(self):
        print('Content of dictionary')
        for key in self.dictionary.keys():
            print(key,end=': ')
            print(self.dictionary.get(key))
            
    def grep(self,regex):
        if self.current_name in self.dictionary.keys():
            list=[]
            for word in self.active_container:
                list.extend(re.findall(regex,str(word)))
            if len(list)==0:
                print('No such elements')
            else:
                print(list)
        else:
            print('You shoud switch or registrate a new user to call this function')
        
    def registrate_new_user(self,name):
        if name in self.dictionary.keys():
            print('this name has already taken, choose another')
        else:
            self.dictionary.update({name:set()})

    def remove_user(self,name):
        if name in self.dictionary.keys():
            del self.dictionary[name]
            self.active_container.clear()
            self.current_name='Not Entered'
        else:
            print("this user doesn't exist")

    def print_all_users(self):
        print('Available names:')
        for name in self.dictionary.keys():
            print(name,end=' ')
        print()

    def current_user(self):
        print(self.current_name)

    def switch_user(self,name):
        self.loaded=False
        self.active_container=set()
        if name in self.dictionary:
            self.current_name=name
            print("Do you want to load container [yes/no]")
            if input()=='yes':
                self.active_container=self.dictionary[self.current_name]
                self.loaded=True
        else:
            self.current_name=CLI.enpty_name
            print("No user with such name")
    def load_container(self):
        if self.current_name in self.dictionary.keys():
            if not self.loaded:
                self.active_container.update(self.dictionary[self.current_name])
                self.loaded=True
            else:
                print('Container has already loaded')
        else:
             print('You shoud switch or registrate a new user to call this function')
    def save_changes(self):
        if self.current_name !=CLI.enpty_name:
            self.dictionary[self.current_name]=self.active_container
            print('changes saved')
    def save_in_file(self):
        with open(self.filename,'wb') as fs:
            pickle.dump(self.dictionary,fs)
        print('Saving done')

    def load_dictionary(self):
        try:
            with open(self.filename,'rb') as fs:
                self.dictionary = dict(pickle.load(fs))
        except:
            print('File is unable to read')
def info():
    print('\nTo switch user press 0')
    print('To see all users press 1')
    print('To add new user press 2')
    print('To delete user press 3')
    print('To see current user press 4')
    print('To load the container press 5')
    print('To add object press 6')
    print('To add list of objects press 7')
    print('To delete object press 8')
    print('To find object press 9')
    print('To print all elements of container press 10')
    print('To check the value in the container by regex press 11')
    print('To save changes press 12')
    print('To save changes in file press 13')
    print('To see all content press 14')
    print('To call info press 15')
    print('To exit press 16\n')
if __name__=="__main__":
    filename=r"/home/vboxuser/PythonLabs/Lab2/SaveLoad/CLIData.txt"
    client=CLI(filename)
    client.print_all_dict()
    client.print_all_users()
    info()
    first=True
    while True:
        x=0;
        try:
            x=int(input())
        except:
            print('Invalid Input,try again')
            continue
        match x:
            case 0:
                if not first:
                    print('If you want to save changes press yes')
                    if input()=='yes':
                        client.save_changes()
                print('Enter user_name')
                client.switch_user(input())
                first=False
            case 1:
                client.print_all_users()
            case 2:
                print('Enter user_name')
                client.registrate_new_user(input())
            case 3:
                print('Enter user_name')
                client.remove_user(input())
            case 4:
                client.current_user()
            case 5:
                client.load_container()
            case 6:
                print('Enter object')
                client.add(input())
            case 7:
                print('Enter list of object separated by space')
                client.add(list(input().split()))
            case 8:
                print('Enter object')
                client.remove_object(input())
            case 9:
                 print("Enter object")
                 client.find(input())
            case 10:
                client.list()
            case 11:
                print("Enter regular expression")
                reg=input()
                client.grep(reg)
            case 12:
                client.save_changes()
            case 13:
                client.save_in_file()
            case 14:
                client.print_all_dict()
            case 15:
                info()
            case _:
                print('If you want to save changes to file press yes')
                if input()=='yes':
                    client.save_changes()
                    client.save_in_file()
                break
    #client.add(485)
    #client.add("str")
    #client.add([1,5,'str2',9])
    #client.add("Last April, John took a trip to Las Vegas, Nevada. Las Vegas is a popular destination in the western portion of the United States.")
    #client.add(486.368)
    #client.add('A stay in Las Vegas can feel similar to a visit to many popular cities worldwide.')
    #client.list()
    #client.grep(r'(April)|(can)')
    #client.registrate_new_user("Ivan")
    #client.print_all_users()
    #client.switch_user("Ivan")
    #client.add(777)
    #client.list()
    #client.save()
    #client.load_dictionary()
    #client.load_dictionary()

