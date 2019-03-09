# ECS 32A
# Assignment 6
# Raunak Anand
# Word Counting Class
from wordle import wordleFromObject
from cleanWord import clean

# the Count class.  The wordleFromObject function takes a Count object as
# input, and calls its getTopWords method. 
class Count:
        # dictionary of word counts
        wordCounts = None

        # method to initialize any data structures, such as a dictionary to
        # hold the counts for each word, and a list of stop words
        def __init__(self):
                print("Initializing Word Counter")
                infile = open("stopWords.txt")
                #Initializing list
                self.stopWordList = []
                #for loop to add each word to a list
                for line in infile:
                    line = line.strip()
                    self.stopWordList.append(line)
                #print(self.stopWordList)
                # set the attrbute wordCounts to an empty dictionary
                self.wordCounts = {}

        # method to add one to the count for a word in the dictionary.
        # if the word is not yet in the dictionary, we'll need to add a
        # record for the word, with a count of one. 
        def incCount(self,word):
                # Add code to clean the word
                word  =  clean(word)
                # Do not add the empty string to the dictionary
                if word == "":
                        return
                #elif statement to check if the word is part of the stop word list
                elif word in self.stopWordList:
                    return
                
                # Add code here to update the dictionary
                elif word in self.wordCounts:
                        self.wordCounts[word] += 1
                else:
                        self.wordCounts[word] = 1

        # method to look up the count for a word
        def lookUpCount(self,word):
                if word in self.wordCounts:
                        return self.wordCounts[word]
                else:
                        return 0

        # method to get the most frequent words out of the dictionary.
        # The argument "num" indicates how many words to return. 
        def getTopWords(self,num):
            #Initializing the list
            num_list = list()
            #Using a for loop to add values to the list
            for key, value in self.wordCounts.items():
                num_list.append((value, key))
            #sorting values in the list
            num_list.sort(reverse=True)       
            return num_list[:num]
        

                
# The main program 
def main():
                                
        # Make a new counter object 
        # the counter holds the counts for all the words
        counter = Count()

        # These lines test out the methods
        # you write in part 1.  
        # remove all this testing code once you are sure the methods
        # work properly. If the methods are working, it should print
        # 1, 2, 0, and finally 0.
        # Kodethon will test other forms of the words with punctuation. 
        #counter.incCount("Well,")
        #counter.incCount("oven")
        #counter.incCount("well")
        #counter.incCount("....'")
        #print(counter.lookUpCount("oven"))
        #print(counter.lookUpCount("well"))
        #print(counter.lookUpCount("pizza"))
        #print(counter.lookUpCount(""))


        # open the file
        infile = open("Alice.txt","r")

        # put a loop here that extracts all words and
        # inserts each word into the counter object by calling
        # the counter.incCount() method
        for line in infile:
                line = line.split()
                for i in line:
                    counter.incCount(i)
                continue # replace this
        
        infile.close() # close file

        #print(counter.lookUpCount("alice"))
        #print(counter.lookUpCount("rabbit"))
        #print(counter.lookUpCount("and"))
        #print(counter.lookUpCount("she"))

        # test code for getTopLines.  Uncomment in Part 4.
        top_10 = counter.getTopWords(10)
        print(top_10)

        # Finally, uncomment the call to the wordle function! 
        wordleFromObject(counter,30)


# run the main program
main()
        
