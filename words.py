def factorial(num):
    factCal=1
    num1=1
    while(num1<=num):
        factCal*=num1
        num1+=1
    return factCal
    #summary open a url and get the files from that file and then break into line and slip in words
def fetch_word():
    from urllib.request import urlopen
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words=[]
        for line in story:
            #print(line)
            line_words= line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    

    for word in story_words:
        print(word)
#printing loop with the indexes
    presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
    for i in range(len(presidents)):
        print("President {}: {}".format(i + 1, presidents[i]))
    
    print (factorial(6))

if __name__=='__main__': # 1. if we are running it directly then __name will come as __main__ 
    fetch_word()            
print(__name__)  #tell us whether it is being imported or used as script
                    #2. and if we are importing it then it will retun the name of the file imported