import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from mpl_toolkits.mplot3d import Axes3D

def plot_joint_3d(conjunta_dict, bins_width = 1, az=50, el=-5):
    conj_array = np.array([[p,a] for p,a in conjunta_dict.keys()])
    p_max, a_max = np.max(conj_array, axis=0)
    p_min, a_min = np.min(conj_array, axis=0)
    espacio_muestral_pesos = np.linspace(p_min, p_max, p_max - p_min + 1)
    espacio_muestral_alturas = np.linspace(a_min, a_max, a_max - a_min + 1)
    xpos, ypos = np.meshgrid(espacio_muestral_pesos, espacio_muestral_alturas)
    xpos = xpos.flatten('F')
    ypos = ypos.flatten('F')
    zpos = np.zeros_like(xpos)
    dx = bins_width * np.ones_like(zpos)
    dy = dx.copy()
    
    conjunta_H = np.zeros([p_max - p_min + 1, a_max-a_min + 1])
    height, width = conjunta_H.shape
    for (p,a), f in conjunta_dict.items():
        conjunta_H[p - p_min, a - a_min] = f
        
    dz = conjunta_H.astype(int).flatten()
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b')
    ax.view_init(az, el)
    plt.show()

def plot_joint_hists_dicts(conjunta_dict):
    conj_array = np.array([[p,a] for p,a in conjunta_dict.keys()])
    p_max, a_max = np.max(conj_array, axis=0)
    p_min, a_min = np.min(conj_array, axis=0)
    conjunta_H = np.zeros([p_max - p_min + 1, a_max-a_min + 1])
    height, width = conjunta_H.shape
    for (p,a), f in conjunta_dict.items():
        conjunta_H[p - p_min, a - a_min] = f
    
    
    
    nullfmt = NullFormatter()         # no labels

    # definitions for the axes
    left = 0
    top = 0
    rect_scatter = [0, 0, width/height, 1]
    rect_histx =   [0, -0.2 -0.01, width/height , 0.2]
    rect_histy =   [width/height + 0.01, 0, 0.2, 1]
    # start with a rectangular Figure
    plt.figure(figsize=(6, 6))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)
    # the scatter plot:
    
    axHistx.bar(np.array(range(conjunta_H.shape[1]))+a_min, conjunta_H.sum(axis=0))
    axHisty.barh(np.array(range(conjunta_H.shape[0]))+p_min,conjunta_H.sum(axis=1))
    axHisty.yaxis.tick_right()
    axScatter.matshow(np.flip(conjunta_H, axis=0), cmap='gray')
    axScatter.xaxis.set_major_formatter(nullfmt)
    axScatter.yaxis.set_major_formatter(nullfmt)
    plt.show()
    return conjunta_H.astype(int), p_min, a_min

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