import json
import random 


#Writes the words into words.json file
def write_json(new_data, filename='words.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.update(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
 
#Call this function when you want to add to the json file
#input 0 for continue and 1 for exit
def input_words():     
    exit = 0 
    data = {}    
    while exit == 0 :
        word = input("Enter GRE Word: ")
        assert len(word) > 0, "Provided Empty string"
        meaning = input("Enter the meaning ")
        assert len(meaning) > 0, "Provided Empty string"
        data[word]=meaning
        write_json(data)
        exit = int(input("exit? "))

#call this function when you want to practice from the test set
#input 0 for continue and 1 for exit
def practice(correct, total, filename='words.json'):
    exit = 0
    with open(filename,'r') as file:
        f = json.load(file)
        while(exit==0):
            word = random.choice(list(f))
            print(word)
            total+=int(1)
            input()
            print(f[word])
            correct += int(input("Correct? "))
            exit = int(input("exit? "))
    print("Correctly answered: ",correct)
    print("Total Questions: ", total)
               
if __name__ == "__main__":
    correct=0
    total = 0
    #practice(correct,total)
    input_words()


    
