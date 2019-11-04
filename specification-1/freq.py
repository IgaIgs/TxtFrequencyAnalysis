import collections

freq_counter = collections.Counter


# counting how many instances of each word are in the file using the counter function in collections library
def count_words(analysed_file_read):
    return freq_counter(analysed_file_read)


# counting the instances of each of the characters in the file
def count_characters(analysed_file_read):
    count = 0
    temp_string = ""
    # adding each line to one long string
    for i in analysed_file_read:
        temp_string = temp_string + analysed_file_read[count]
        count += 1
        return freq_counter(temp_string)
