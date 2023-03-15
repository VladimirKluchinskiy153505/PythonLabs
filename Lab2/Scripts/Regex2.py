from re import*
def declarative_sentences_count(text):
    d_sent=findall(r'(?<!Dr)(?<!Esq)(?<!Hon)(?<!Jr)(?<!Mr)(?<!Mrs)(?<!Messrd)(?<!Mmes)(?<!Msgr)(?<!Prof)(?<!Rev)(?<!Rt)(?<!Hon)(?<!Sr)(?<!St)(?<!sp)(?<!f)(?<!e.g)(?<!etc)(\.)([\s]|$)',text,flags=MULTILINE)
    return len(d_sent)

def non_declarative_sentences_count(text):
    nd_sent=findall(r'([\!\?])\s*[A-Z]?',text)
    return len(nd_sent)

def average_sentece_length(text):
    words=findall(r'([0-9]*[A-Za-z]+[0-9]*)',text)
    sentence_count=declarative_sentences_count(text)+non_declarative_sentences_count(text)
    return len(words)/sentence_count

def average_word_length(text):
    words=findall(r'([0-9]*[A-Za-z]+[0-9]*)',text)
    characters_count=0
    for w in words:
        characters_count+=len(w)
    return characters_count/len(words)

def find_ngrams(text,k,n):
    n_gramm_list=[]
    n_gramm_dict={'':0}
    for i in range(len(text)-n+1):
        word=''
        for j in range(n):
            word+=text[i+j]
        n_gramm_list.append(word)
        if word in n_gramm_dict:
            n_gramm_dict[word]+=1
        else:
            n_gramm_dict[word]=1
    sorted_n_gramm_list=sorted(n_gramm_dict.items(),key=lambda x:x[1],reverse=True)
    if k[0]>len(sorted_n_gramm_list):
        k[0]=len(sorted_n_gramm_list)
    return sorted_n_gramm_list
    #for i in range(k):
    #    print(sorted_n_gramm_list[i])

if __name__=="__main__":
    text=''
    with open(r"/home/vboxuser/PythonLabs/Lab2/TextFiles/Input2.txt","r") as fs:
        while True:
            line = fs.readline()
            text+=line
            if not line:
                break
    print('Text:')
    print(text)

    d_sent_count=declarative_sentences_count(text)
    print('\nAmount Of Declarative', d_sent_count,end='\n\n')

    nd_sent_count=non_declarative_sentences_count(text)
    print('Amount Of Non-Declarative Sentences',nd_sent_count,end='\n\n')

    sent_count=d_sent_count+nd_sent_count;
    print('Amount Of All Sentences',sent_count,end='\n\n')

    av_sent_length=average_sentece_length(text)
    print('Average sentence length:',av_sent_length,'words',end='\n\n')
    
    av_word_length=average_word_length(text)
    print('Average word length:',av_word_length,'characters',end='\n\n')

    print('Input K and N')
    while True:
        try:
            k,n=[int(input())],int(input())
        except ValueError:
            print("Invalid Input.Try again")
        else:
            break
    print('Top',k,'N-Grams:')
    sorted_ngrams=find_ngrams(text,k,n)
    for i in range(k[0]):
        print(sorted_ngrams[i])

