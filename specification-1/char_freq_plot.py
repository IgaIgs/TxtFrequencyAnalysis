import matplotlib.pyplot as plt
import numpy as np

top_char_display = 10


def plot_bar_graph(freq_char):
    fig, ax = plt.subplots()

    for character, frequency in freq_char.most_common(10):

        characters = list(character)
        frequency = list(frequency)
        print(characters)
        print(frequency)
    # most_freq_char = characters[0:11]
        y_pos = np.arange(len(characters))


   # most_freq_char_freq = frequency[0:11]

        ax.barh(y_pos, frequency, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(characters)
        ax.invert_yaxis()  # labels read top to bottom
        ax.set_xlabel('Frequency')
        ax.set_title('Character Frequency')

    plt.show()
