import re
import pickle
class CLI:
    def __init__(self,filename):
        self.filename=filename
        self.dictionary={str():set()}
        self.load_dictionary()
        self.current_name='Not entered'
        
    def add(self,object):
        if self.current_name in self.dictionary.keys():
            if type(object) is list:
                for item in object:
                    self.dictionary.get(self.current_name).add(item)
            else:
                self.dictionary.get(self.current_name).add(object)
        else:
            print('You shoud switch or registrate a new user to call this function')

    def remove_object(self,object):
        if self.current_name in self.dictionary.keys():
            self.dictionary.get(self.current_name).discard(object)
        else:
            print('You shoud switch or registrate a new user to call this function')

    def find(self,object):
        if self.current_name in self.dictionary.keys():
            if object in self.dictionary.get(self.current_name):
                print(str(object))
            else:
                print('No such elements')
        else:
            print('You shoud switch or registrate a new user to call this function')

    def list(self):
        print(self.dictionary.get(self.current_name),sep=': ')

    def print_all_dict(self):
        print('Content of dictionary')
        for key in self.dictionary.keys():
            print(key,end=': ')
            print(self.dictionary.get(key))
            
    def grep(self,regex):
        if self.current_name in self.dictionary.keys():
            list=[]
            for word in self.dictionary.get(self.current_name):
                list.extend(re.findall(regex,str(word)))
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
        else:
            print("this user doesn't exist")

    def print_all_users(self):
        print('Available names:')
        for name in self.dictionary.keys():
            print(name,end=',')
        print()

    def current_user(self):
        print(self.current_name)

    def switch_user(self,name):
        if name in self.dictionary:
            self.current_name=name
        else:
            print("No user with such name")

    def save(self):
        with open(r"C:\Users\avdot\Desktop\PythonLabs\LabRab2\CLIData.txt",'wb') as fs:
            pickle.dump(self.dictionary,fs)
        print('Saving done')

    def load_dictionary(self):
        try:
            with open(r"C:\Users\avdot\Desktop\PythonLabs\LabRab2\CLIData.txt",'rb') as fs:
                self.dictionary = dict(pickle.load(fs))
        except:
            print('File is unable to read')
def info():
    print('\nIf you want to switch user press 0')
    print('If you want to add new user press 1')
    print('If you want to delete user press 2')
    print('If you want to see current user press 3')
    print('If you want to add object press 4')
    print('If you want to delete object press 5')
    print('If you want to add list of objects press 6')
    print('If you want to find object press 7')
    print('If you want to print all elements of container press 8')
    print('If you want to check the value in the container by regex press 9')
    print('If you want to save changes press 10')
    print('If you want to load state press 11')
    print('If you want to see all users press 12')
    print('If you want to see all content press 13')
    print('If you want to call info press 14')
    print('If you want to exit press 15')
if __name__=="__main__":
    filename=r'C:\Users\avdot\Desktop\PythonLabs\LabRab2\CLIData.txt'
    client=CLI(filename)
    client.print_all_dict()
    client.print_all_users()
    info()
    while True:
        x=0;
        try:
            x=int(input())
        except:
            print('Invalid Input,try again')
            continue
        match x:
            case 0:
                print('If you want to save changes press yes')
                if input() == 'yes':
                    client.save()
                print('Enter user_name')
                client.switch_user(input())
            case 1:
                print('Enter user_name')
                client.registrate_new_user(input())
            case 2:
                print('Enter user_name')
                client.remove_user(input())
            case 3:
                client.current_user()
            case 4:
                client.add(input())
            case 5:
                print('Enter object')
                client.remove_object(input())
            case 6:
                print('Enter list of object separated by space')
                client.add(list(input().split()))
            case 7:
                print('Print object')
                client.find(input())
            case 8:
                client.list()
            case 9:
                 print("Enter regular expression")
                 reg=input()
                 client.grep(reg)
            case 10:
                client.save()
            case 11:
                client.load()
            case 12:
                client.print_all_users()
            case 13:
                client.print_all_dict()
            case 14:
                info()
            case _:
                print('If you want to save changes press yes')
                if input()=='yes':
                    client.save()
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

