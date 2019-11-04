import csv

# this variable can be modified to change how many words you want to print into the freq.csv file
top_words_print = 10


def csv_writer(freq_words):
    with open('freq.csv', 'w') as csvfile:
        fieldnames = ['Word', 'Frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        word_list = list(freq_words.keys())
        freq_list = list(freq_words.values())
        count = 0

        while count < top_words_print or count < len(word_list):
            writer.writerow({'Word': word_list[count], 'Frequency': freq_list[count]})
            # for each round of the loop, add 1 to the counter list so that the loop finishes with the length of the
            count += 1
