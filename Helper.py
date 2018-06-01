import csv
import re
import math
import time
import random
import numpy as np
import sys
import os
from shapely.geometry import shape, Point 
from matplotlib.pyplot import axis
from numpy import shape
import matplotlib
import datetime
import matplotlib as mpl
import pandas as pd

class Helper:
    Kafkas = {"dev":"smartaqnet-dev.teco.edu","dev01":"smartaqnet-dev01.teco.edu"}
    
    Frosts = {"dev":"smartaqnet-dev.teco.edu","dev01":"smartaqnet-dev01.teco.edu"}
    
    DataHome = "data/"
    DeutschlandJSON="deutschlandGeoJSON/"
    
    
    #MA Flavor plot
    def create_axes(title, figsize=(8, 8)):
        fig = plt.figure(figsize=figsize)
        #fig.suptitle(title)

        # define the axis for the first plot
        left, width = 0.01, 0.88
        bottom, height = 0.01, 0.88

        rect_scatter = [left, bottom, width, height]
        ax_scatter = plt.axes(rect_scatter)

        left, width = 0.92, 0.02
        bottom, height = 0.1, 0.75
        rect_colorbar = [left, bottom, width, height]
        ax_colorbar = plt.axes(rect_colorbar)

        return ax_scatter, ax_colorbar

    def plot_interpolationResult(axes, points, title="",
                      x0_label="", x1_label="",cbTitle="Temperature",marker='o'):
        ax = axes[0]

        ax.set_title(title)
        ax.set_xlabel(x0_label)
        ax.set_ylabel(x1_label)
        y = np.copy(points[:,2])
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        textstr = '$max=%.2f$\t$min=%.2f$\t$\mu=%.2f$\t$\sigma=%.2f$'%(y.max(),
                                                                     y.min(),
                                                                     y.mean(),
                                                                     y.var())
        #y[y>30] = 25
        ax.text(0.05, 1, textstr, transform=ax.transAxes, fontsize=8,
            verticalalignment='top', bbox=props)
        if(True):
            cbar = axes[1]
            ax.scatter(points[:,1],points[:,0], alpha=0.5, marker=marker, s=15, lw=0,c=y,cmap='coolwarm')
            norm = mpl.colors.Normalize(y.min(), y.max())
            cb = mpl.colorbar.ColorbarBase(cbar,norm = norm, cmap='coolwarm',
                                    orientation='vertical',
                                 label= cbTitle )

        else:
            latN, lonN =int(math.sqrt(points.shape[0])),int(math.sqrt(points.shape[0]))
            pcm = ax.pcolormesh(points[:,0].reshape(latN, lonN),points[:,1].reshape(latN, lonN),y.reshape(latN, lonN),
                           vmin=12., vmax=35., cmap='coolwarm')
            fig.colorbar(pcm, ax=ax, extend='both')

        # Removing the top and the right spine for aesthetics
        # make nice axis layout
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        #ax.get_xaxis().tick_bottom()
        #ax.get_yaxis().tick_left()
        #ax.spines['left'].set_position(('outward', 5))
        #ax.spines['bottom'].set_position(('outward', 5))
        ##norm = mpl.colors.Normalize(y.min(), y.max())
        ##cb = mpl.colorbar.ColorbarBase(cbar,norm = norm, cmap='coolwarm',
        ##                            orientation='vertical',
        ##                         label= cbTitle )
    