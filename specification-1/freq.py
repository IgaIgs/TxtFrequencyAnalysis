import collections
import string
import char_freq_plot
import csvwriter

freq_counter = collections.Counter

# file path of an example book to be analysed
analysed_file = '../resources/txt/book.txt'


# counting how many instances of each word are in the file using the counter function in collections library
def count_words(analysed_file_read):
    f = open(analysed_file, "r", encoding='utf8')
    analysed_file_read = f.read().lower().splitlines()
    # create an empty dictionary to which the words and their counts will be added
    words_freq = dict()
    for line in analysed_file_read:
        # split the lines into words
        words = line.translate(str.maketrans('', '', string.punctuation)).split()
        for w in words:
            # check whether the word is in the dictionary and up its counter by 1
            if w in words_freq:
                words_freq[w] += 1
            else:
                words_freq[w] = 1
    # put the frequency of words in order from the most frequent to the least frequent by turning the dictionary
    # into a list of tuples
    output = {}
    words_freq_sorted = sorted(words_freq.items(), key=lambda kv: kv[1], reverse=True)
    # turn the sorted list of tuples back to a dictionary to be used for csv writer later
    for i in words_freq_sorted:
        output[i[0]] = i[1]
    return output


# counting the instances of each of the characters in the file
def count_characters(analysed_file_read):
    f = open(analysed_file, "r", encoding='utf8')
    analysed_file_read = f.read().lower().replace(' ', '').splitlines()

    temp_string = "".join(analysed_file_read)
    return freq_counter(temp_string)


if __name__ == '__main__':

    f = open(analysed_file, "r", encoding='utf8')
    analysed_file_read = f.read().lower().splitlines()

    info_words = 'This is a list of all words in the file ordered from the most to the least frequent:'
    freq_words = count_words(analysed_file_read)
    info_char = 'This is a counter containing a list of all the characters from the file ordered from the most to the least frequent:'
    freq_char = count_characters(analysed_file_read)

    print(info_words, freq_words)
    print(info_char, freq_char)

    csvwriter.csv_writer(freq_words)

    char_freq_plot.plot_bar_graph(freq_char)
