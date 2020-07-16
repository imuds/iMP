# -*- coding: utf-8 -*-
import numpy as np
import subprocess
import matplotlib.pyplot as plt
import glob
import os
from matplotlib.ticker import MultipleLocator
from matplotlib import mathtext
mathtext.FontConstantsBase = mathtext.ComputerModernFontConstants
"""
lysocline and CaCO3 burial fluxes 
"""

################ Setting up working directory ###################

python = False   # if plotting python results make this True
matlab = True    # if plotting matlab results make this True

#### OM degradation scheme 
org = 'ox'  
# org = 'oxanox'

### if output directory has a specific name add the string 
addname = 'test_co2sys_v2'
### you need to change the directory name depending on the mixing style 
mixing = ''
##mixing = 'turbo2'

Workdir = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Workdir += '/imp_output/'
if python or matlab: 
    if python: Workdir+='python/'
    elif matlab: Workdir+='matlab/'
else:
    Workdir+='fortran/'
    
if not addname =='':
    Workdir += addname
    
Workdir += '/res/'

if not mixing=='':
    Workdir += org+'-'+mixing
else:
    Workdir += org
    
Workdir += '/'
    

# Or you can just specify the working directory here
#  (where result files are restored)
# Workdir += './'

################ Setting up working directory ###################

rrlist = ['0.00E+0','0.50E+0','0.67E+0','0.10E+1','0.15E+1']  # You may need change this list if out put results use different formats
if python:rrlist = ['0.0e+00','5.0e-01','6.7e-01','1.0e+00','1.5e+00']
if matlab:rrlist = ['0.00','0.50','0.67','1.00','1.50']

flxlist = ['6.0e-06','1.2e-05','1.8e-05','2.4e-05','3.0e-05' \
           ,'3.6e-05','4.2e-05','4.8e-05','5.4e-05','6.0e-05']

flx = [6,12,18,24,30,36,42,48,54,60]
rrt = [0,0.5,0.67,1,1.5]

#### plotting parameters 
plt.rcParams['font.family'] = 'Arial' 
plt.rcParams['font.size'] = 20

linewidth = 1.5

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

nx = 5
ny=2

fig = plt.figure(figsize=(9,10))

# file size determined by 5 rain ratios, 10 cc flxes, 25 water depths
#    and 10 and 5 data for CaCO3 wt% and bur flx, respectively
#   (thus, 10 and 5 may change depending on the number of data
#       you restore: previously these are 7 and 2)
data_lys = np.zeros((5,10,25,11),dtype=np.float)
data_bur = np.zeros((5,10,25,5),dtype=np.float)
if python or matlab:
    data_lys = np.zeros((5,10,25,7),dtype=np.float)
    data_bur = np.zeros((5,10,25,2),dtype=np.float)

cmap = plt.cm.get_cmap('jet')

# First read data 
for j in range(5):
    rr = rrlist[j]
    if python or matlab:
        filelist = ['']*10
        for k in range(10):
            ff = flxlist[k]
            filelist[k]=Workdir+'lys_sense_cc-'+ff \
                         +'_rr-'+rr+'.txt'
    else :
        filelist = glob.glob(Workdir+'lys_sense_cc-*_rr-'+rr+'.res')
        filelist[0], filelist[1:] = filelist[-1], filelist[:-1]

    datatmp = np.loadtxt(filelist[0])
    data = np.zeros((len(filelist),datatmp.shape[0],datatmp.shape[1])\
                    ,dtype=np.float)

    for i in range(len(filelist)):
        data_lys[j,i,:,:]=np.sort(np.loadtxt(filelist[i]),axis=0)

    if python or matlab:
        filelist = ['']*10
        for k in range(10):
            ff = flxlist[k]
            filelist[k]=Workdir+'ccbur_sense_cc-'+str(int((k+1)*6)*1e-6) \
                         +'_rr-'+rr+'.txt'
            filelist[k]=Workdir+'ccbur_sense_cc-'+ff \
                         +'_rr-'+rr+'.txt'
    else :
        filelist = glob.glob(Workdir+'ccbur_sense_cc-*_rr-'+rr+'.res')
        filelist[0], filelist[1:] = filelist[-1], filelist[:-1]
    
    for i in range(len(filelist)):
        data_bur[j,i,:,:]=np.sort(np.loadtxt(filelist[i]),axis=0)

# Then plot data
for j in range(5):
    ax = plt.subplot2grid((ny,nx), (0,j))

    color=cmap(np.linspace(0,1,10))

    for i in range(10):
        label=str(flx[i])
        plt.plot(data_lys[j,i,:,5],data_lys[j,i,:,0],'-x',c=color[i]
                 ,label=label
                 )
    ax = plt.gca()
    ax.set_xlim(0,90)
    ax.set_ylim(-40,40)
    ax.set_xticks([0,45,90])
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')
    ax.xaxis.set_minor_locator(MultipleLocator(15))
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    
    if j!=0:
        ax.set_xticks([45,90])
        ax.set_yticklabels([])
        if j==2:ax.set_xlabel('CaCO'+r'$\mathregular{_3}$'+' wt%')
    elif j==0:ax.set_ylabel(r'$\mathregular{\Delta}$'+'CO'+r'$\mathregular{_3}$'+' ('+r'$\mathregular{\mu}$'+'M)')
    
    tx = 0.5
    ty = 1.05
    ax.text(tx,ty,str(rrt[j]),horizontalalignment='center', transform=ax.transAxes)
    if j==2:
        ty = 1.17
        ax.text(tx,ty,'OM/CaCO'+r'$\mathregular{_3}$'+' rain ratio',horizontalalignment='center', transform=ax.transAxes)
    
    if j==4: 
        ax.legend(
            bbox_to_anchor=(1, 0.5), loc='upper left',facecolor = 'None',edgecolor='None'
            ,title = 'CaCO'+r'$\mathregular{_3}$'+' rain\n'+'('+r'$\mathregular{\mu}$'+'mol cm'+r'$\mathregular{^{-2}}$'
                +' yr'+r'$\mathregular{^{-1}}$'+')'
            )

    print data_lys[j,:,:,2].max(),data_lys[j,:,:,2].min()
    print data_lys[j,:,:,4].max(),data_lys[j,:,:,4].min()
    print data_lys[j,:,:,6].max(),data_lys[j,:,:,6].min()


    ax2 = plt.subplot2grid((ny,nx), (1,j))
    color=cmap(np.linspace(0,1,10))

    for i in range(10):
        label=str(flx[i])
        plt.plot(data_bur[j,i,:,1],data_bur[j,i,:,0],'-x',c=color[i]
                 ,label=label
                 )
    ax2 = plt.gca()
    ax2.set_xlim(0,40)
    ax2.set_ylim(-40,40)
    ax2.set_xticks([0,20,40])
    ax2.yaxis.set_ticks_position('both')
    ax2.xaxis.set_ticks_position('both')
    ax2.xaxis.set_minor_locator(MultipleLocator(10))
    ax2.yaxis.set_minor_locator(MultipleLocator(5))
    
    if j!=0:
        ax2.set_yticklabels([])
        ax2.set_xticks([20,40])
        if j==2:ax2.set_xlabel(
            'CaCO'+r'$\mathregular{_3}$'+' burial ('+r'$\mathregular{\mu}$'+'mol cm'+r'$\mathregular{^{-2}}$'
            +' yr'+r'$\mathregular{^{-1}}$'+')'
            )
    elif j==0:ax2.set_ylabel(r'$\mathregular{\Delta}$'+'CO'+r'$\mathregular{_3}$'+' ('+r'$\mathregular{\mu}$'+'M)')


fig.subplots_adjust(left=0.15,bottom=0.1,wspace=0.06,hspace=0.3,right=0.7)

outfilename = Workdir+'lysbur.pdf'
plt.savefig(outfilename, transparent=True)
outfilename = Workdir+'lysbur.svg'
plt.savefig(outfilename, transparent=True)
subprocess.call('"C:\Program Files\Inkscape\inkscape.exe" -z -f ' \
                + outfilename + ' --export-emf '+outfilename+\
                '.emf',shell=True)
plt.show()
plt.clf()
plt.close()
