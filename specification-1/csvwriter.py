import csv

# this variable can be modified to change how many words you want to print into the words_freq.csv file
top_words_print = 10


# create a cvs file to display a certain number of most frequent words in a text file (my start value will be 10)
def csv_writer(freq_words):
    # open a chosen cvs file in which the programme is going to write in
    # new line='' to get rid of blank lines in between rows of data
    with open('words_freq.csv', 'w', encoding='utf8', newline='') as csvf:
        # fieldnames are going to be the headers of the columns in the cvs file
        fieldnames = ['Word', 'Frequency']
        # use a DictWriter to write in this csv file using the dictionary containing words and their frequencies
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        # write the fieldnames as headers
        writer.writeheader()
        # assign the keys and values of the dictionary which was the result of the freq_words function
        word_list = list(freq_words.keys())
        freq_list = list(freq_words.values())
        # start the count of number of most frequent words already written into the csv file
        count = 0

        # keep writing row into the csv file unless the desired number of most frequent words is reached or the end
        while count < top_words_print:
            writer.writerow({'Word': word_list[count], 'Frequency': freq_list[count]})
            # for each round of the loop, add 1 to the counter list
            count += 1
