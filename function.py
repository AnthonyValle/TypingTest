import time
import os
from paragraphs import ran_paragraph
from IPython.display import clear_output

timed_list = []
def Start():
  
    global errors
    errors = 0

    #Countdown
    print(ran_paragraph)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)

    #Splitting paragraph
    split_paragraph = ran_paragraph.split(' ')
    
    for index, element in enumerate(split_paragraph):

        #While loop key
        done = False

        while done == False:

            #Clears Screen (Prevnting Stacking)
            try:
              os.system('clear')
            except:
              os.system('cls')
            clear_output()

            #Copy of split paragraph, used to outline the word needed to be typed (eg. | hello | there what ...)
            split_paragraph_copy = [x for x in split_paragraph]

            #Replacing the element/word with itself inbetween |  |
            split_paragraph_copy[index] = ('| ' + split_paragraph[index] + ' |')

            #Joining the copy of the split paragraph to display whole paragraph
            print(' '.join(split_paragraph_copy))

            #Clocks the start of typing time
            start = time.time()

            #Input
            print('-'*len(element))
            answer = input()

            #If statement to verify typed answer
            if answer == element:

                #If it's right it clocks out the time, calculates difference (start - end), and appends it to list of all times 
                end = time.time()
                timed_list.append(end-start)

                #Breaks for loop
                done = True
            else:

              #If it's wrong it appends 1 to errors and repeats the loop
              errors += 1
              pass

    #Clears screen to display results
    clear_output()
    try:
      os.system('clear')
    except:
      os.system('cls')

    print("---------RESULTS AND ANALYSIS---------")

    #Time for each word
    for index, element in enumerate(split_paragraph):
        print(element + '-->' + str(round(timed_list[index], 2)) + ' seconds')
    print("--------------------------------------")

    #Total time
    print("TOTAL TIME")
    total = 0
    for i in timed_list:
        total += i
    print(round(total,2))
    print("--------------------------------------")

    #Error count
    print("TOTAL ERRORS")
    print(errors)
    print("--------------------------------------")

    #WPS
    wps = round(len(split_paragraph)/total, 2)
    print("WORDS PER SEC")
    print(wps)
    print("--------------------------------------")

    #WPM
    wpm = round((len(split_paragraph)/total*60), 2)
    print("WORDS PER MINUTES")
    print(wpm)
    print("--------------------------------------")

    #Analysis
    if wpm < 40:
      print("You are a slow typer")
    elif wpm > 40 and wpm < 60:
      print("You are an average typer")
    else:
      print("You are a fast typer")
    print("--------------------------------------")




