import collections
import string
import char_freq_plot
import csvwriter

freq_counter = collections.Counter

# file path of an example book to be analysed
analysed_file = '../resources/txt/book.txt'

# open the text file, read it, decode the encoding, make all characters lower case and split the lines.
# Then save it in this way under the variable analysed_file_read
f = open(analysed_file, "r", encoding='utf8')
analysed_file_read = f.read().lower().splitlines()


# count how many times does each word appear in the text file
def count_words():
    # create an empty dictionary to which the words and their counts will be added
    words_freq = dict()
    for line in analysed_file_read:
        # split the lines into words and get rid of the punctuation using the string library
        words = line.translate(str.maketrans('', '', string.punctuation)).split()
        for w in words:
            # check whether the word is in the dictionary and up its counter by 1 if it is
            if w in words_freq:
                words_freq[w] += 1
            # if the word is not in the dictionary, don't up it's counter
            else:
                words_freq[w] = 1
    # put the frequency of words in order from the most frequent to the least frequent by turning the dictionary
    # into a list of tuples
    words_dict = {}
    # sort the dictionary by its values and in descending order using the sorted() method
    words_freq_sorted = sorted(words_freq.items(), key=lambda kv: kv[1], reverse=True)
    # turn the sorted list of tuples back to a, now sorted, dictionary to be used for csv writer later
    for i in words_freq_sorted:
        words_dict[i[0]] = i[1]
    # return the final sorted dictionary of word frequencies
    return words_dict


# counting the instances of each of the characters in the file using the Counter method from the collections library
def count_characters():
    # open the file again and strip it from all spaces to avoid having spaces (' ') being taken into account when
    # calculating the most common characters
    f1 = open(analysed_file, "r", encoding='utf8')
    analysed_file_read_no_space = f1.read().lower().replace(' ', '').splitlines()
    # add all the words in the text into one long string
    temp_string = "".join(analysed_file_read_no_space)
    # return a Counter of character frequency
    return freq_counter(temp_string)


# compile all of the working functions' calls in one place
if __name__ == '__main__':

    info_words = 'This is a list of all words in the file ordered from the most to the least frequent:'
    freq_words = count_words()
    info_char = 'This is a counter containing a list of all the characters from the file ordered from the most to the ' \
                'least frequent: '
    freq_char = count_characters()

    print(info_words, freq_words)
    print(info_char, freq_char)

    csvwriter.csv_writer(freq_words)

    char_freq_plot.plot_bar_graph(freq_char)
