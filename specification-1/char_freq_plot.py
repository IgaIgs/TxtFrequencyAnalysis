import matplotlib.pyplot as plt
import numpy as np


def plot_bar_graph(freq_char):
    fig, ax = plt.subplots()

    characters = list(freq_char.keys())
    y_pos = np.arange(len(characters))
    frequency = list(freq_char.values())

    ax.barh(y_pos, frequency, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(characters)
    ax.invert_yaxis()  # labels read top to bottom
    ax.set_xlabel('Frequency')
    ax.set_title('Character Frequency')

    plt.show()
