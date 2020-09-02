# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def plot_settings():

    plt.rcParams['font.family'] = 'Arial' 
    plt.rcParams['font.size'] = 16

    linewidth = 1.

    plt.rcParams['axes.linewidth'] = linewidth

    plt.rcParams['xtick.major.width'] = linewidth
    plt.rcParams['xtick.major.size'] = 8
    plt.rcParams['xtick.minor.width'] = linewidth
    plt.rcParams['xtick.minor.size'] = 4
    plt.rcParams['xtick.major.pad'] = 8

    plt.rcParams['ytick.major.width'] = linewidth
    plt.rcParams['ytick.major.size'] = 8
    plt.rcParams['ytick.minor.width'] = linewidth
    plt.rcParams['ytick.minor.size'] = 4
    plt.rcParams['ytick.major.pad'] = 8

    plt.rcParams['axes.labelpad'] = 8

    plt.rcParams['xtick.direction']='in'
    plt.rcParams['ytick.direction']='in'

    plt.tick_params(top=True)
    plt.tick_params(right=True)
