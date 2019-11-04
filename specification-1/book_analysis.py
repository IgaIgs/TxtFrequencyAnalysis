import freq
import csvwriter

book = "C:/Users/Kirai/PycharmProjects/CSC1034-team-project/practical-3/resources/txt/book.txt"
# input the file path of the file you want to analyse
analysed_file = 'C:/Users/Kirai/PycharmProjects/CSC1034-team-project/practical-3/resources/txt/test_file.txt'


f = open(analysed_file, "r", encoding='utf8')
analysed_file_read = f.read().splitlines()

if __name__ == '__main__':
    freq_words = freq.count_words(analysed_file_read)
    freq_char = freq.count_characters(analysed_file_read)
    print(freq_words)
    print(freq_char)
    csvwriter.csv_writer(freq_words)


