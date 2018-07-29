import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter



def plot_joint_hists(conjunta_H, frec_alt_H, frec_pesos_H):
    nullfmt = NullFormatter()         # no labels

    # definitions for the axes
    rect_scatter = [0, 0, 0.8*53/72, 0.8*72/53]
    rect_histx = [0, 0, 0.8*53/72, 0.2]
    rect_histy = [0.8*53/72+0.05, 0.2, 0.2, 53/72]
    # start with a rectangular Figure
    plt.figure(figsize=(8, 8))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    # no labels
    #axHistx.xaxis.set_major_formatter(nullfmt)
    #axHisty.yaxis.set_major_formatter(nullfmt)

    # the scatter plot:
    axScatter.matshow(np.flip(conjunta_H, axis=0), cmap='gray')
    axScatter.xaxis.set_major_formatter(nullfmt)
    axScatter.yaxis.set_major_formatter(nullfmt)

    axHistx.bar(frec_alt_H.keys(), frec_alt_H.values())
    axHisty.barh(list(frec_pesos_H.keys()),list(frec_pesos_H.values()))
    #axScatter.set_xlim(np.array(axHistx.get_xlim())-144.96)
    #axHisty.set_ylim(axScatter.get_ylim())

    plt.show()