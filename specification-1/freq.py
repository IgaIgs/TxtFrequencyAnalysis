import collections


freq_counter = collections.Counter


# counting how many instances of each word are in the file using the counter function in collections library
def count_words(analysed_file_read):
    #create an empty disctionary to whcih the words and their counts will be added
    words_freq = dict()
    for line in analysed_file_read:
        # split the lines into words
        word = line.split(" ")
        for w in word:
            #check whether the word is in the dictionary and up its counter by 1
            if w in words_freq:
                words_freq[w] += 1
            else:
                words_freq[w] = 1
    return(words_freq)


# counting the instances of each of the characters in the file
def count_characters(analysed_file_read):
    temp_string = "".join(analysed_file_read)
    return freq_counter(temp_string)


if __name__ == '__main__':
    # file path of an example book
    book = "../resources/txt/book.txt"
    # input the file path of the file you want to analyse
    analysed_file = '../resources/txt/test_file.txt'

    f = open(analysed_file, "r", encoding='utf8')
    analysed_file_read = f.read().lower().splitlines()

    freq_words = count_words(analysed_file_read)
    freq_char = count_characters(analysed_file_read)
    print(freq_words)
    print(freq_char)
    #csvwriter.csv_writer(freq_words)
