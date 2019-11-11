import matplotlib.pyplot as plt
import numpy as np


def plot_bar_graph(freq_char):

    # create a dictionary to which the 10 most frequent characters in the text will be added
    char_dict = {}
    # use the most_common method from the collections to extract the first 10 characters from the freq_char counter
    most_common_characters = freq_char.most_common(10)
    for i in most_common_characters:
        char_dict[i[0]] = i[1]

    fig, ax = plt.subplots()

    characters = list(char_dict.keys())
    y_pos = np.arange(len(characters))
    frequency = list(char_dict.values())

    ax.barh(y_pos, frequency, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(characters)
    ax.invert_yaxis()  # labels read top to bottom
    ax.set_xlabel('Frequency')
    ax.set_title('Character Frequency')

    plt.show()
