# -*- coding: utf-8 -*-
import numpy as np
import subprocess
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

"""
caco3 signal profiles 
"""

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

def sigplot(multi,python,test,ox,oxanox,labs,turbo2,nobio,filename,i,ax1,ax2,ax3):
    
    # the following part is used to specify the location of individual result data 
    # in consistent with how and where to record the results 
    Workdir = 'C:/cygwin64/home/YK/imp_output/'
    Workdir += 'Fortran/profiles/'
    if python: Workdir += 'python/'
    if multi: Workdir += 'multi/'
    if test: Workdir += 'test/'
    if labs:
        if oxanox:Workdir += 'oxanox_labs/'
        else:Workdir += 'ox_labs/'
        label = 'Mixing by LABS'
    elif nobio:
        if oxanox:Workdir += 'oxanox_nobio/'
        else:Workdir += 'ox_nobio/'
        label = 'No bioturbation'
    elif turbo2:
        if oxanox:Workdir += 'oxanox_turbo2/'
        else:Workdir += 'ox_turbo2/'
        label='Homogeneous mixing'
    else: 
        if oxanox:Workdir += 'oxanox/'
        else: Workdir += 'ox/'
        label ='Fickian mixing'
        
    Workdir += filename
    Workdir += '/'
    
    # Otherwise, specify here directly the directory which store calculation results and remove comment-out
##    Workdir = './MATLAB/resprofiles/'
    # Workdir = './'
    
    rectime = np.loadtxt(Workdir+'rectime.txt')
##    frac = np.loadtxt(Workdir+'frac.txt')
    sig = np.loadtxt(Workdir+'sigmly.txt')
    bound = np.loadtxt(Workdir+'bound.txt')

    print 'end input-',i



    ls = np.array([':','--','-'])
    dsp = [(1,3),(5,5),[5,3,1,3]]



    if i==0:ax1.plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                     ,label = 'Input'
                 )
    ax1.plot(sig[:,1],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
             ,label=label
                 )

    if i==0:ax2.plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                     ,label='Input'
                 )
    ax2.plot(sig[:,2],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
             ,label=label
                 )
    ax3.plot(sig[:,3],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
             ,label=label
                 )

def main():
    nexp = 3  # Here you can specify the number of plot, 1 to 3 

    multi = np.zeros(nexp,dtype=bool)
    test = np.zeros(nexp,dtype=bool)
    ox = np.zeros(nexp,dtype=bool)
    oxanox = np.zeros(nexp,dtype=bool)
    labs = np.zeros(nexp,dtype=bool)
    turbo2 = np.zeros(nexp,dtype=bool)
    nobio = np.zeros(nexp,dtype=bool)

    python= False

    multi[:]=True
    test[:]=True
    ox[:]=True
    oxanox[:]=True
    if nexp>1:nobio[0]=True
    if nexp>2:turbo2[2]=True
    # simulation file names are listed below
    filename=np.array(['cc-1_1E-5_rr-6_9E-1_dis4_8_therm-mod'
                       ,'cc-1_1E-5_rr-6_9E-1_dis4_8_therm-mod'
                       ,'cc-1_1E-5_rr-6_9E-1_dis4_8_therm-mod'])
    # name below are used for figure
    outname = 'chk_50kyr-read_dis_exp_realtime'

    fs=12

    nx = 3
    ny =3
    tx = 3.3
    ty = 0.5
    fig = plt.figure(figsize=(7*3/4.,6*3/2.)) # long
    for j in range(3):
        if j==0:
            filename=[
                'cc-0.12E-4_rr-0.70E+0_chk_d3.5'
                ]*3
        elif j==1:
            filename=[
                'cc-0.12E-4_rr-0.70E+0_chk_d4.5'
                ]*3
        elif j==2:
            filename=[
                'cc-0.12E-4_rr-0.70E+0_chk_d5.0'
                ]*3
        ax1 = plt.subplot2grid((ny,nx), (j,0))
        ax2 = plt.subplot2grid((ny,nx), (j,1))
        ax3 = plt.subplot2grid((ny,nx), (j,2))
        for i in range(nexp):
            sigplot(multi[i],python,test[i],ox[i],oxanox[i]\
                    ,labs[i],turbo2[i],nobio[i],filename[i],i,ax1,ax2,ax3)

        if j==0: text = 'Control'
        else: text = 'Diss. exp.' +str(j)
        
        ax3.text(tx, ty
             ,text
             ,horizontalalignment='center',verticalalignment='center'\
             , transform=ax1.transAxes
             ,rotation=90
             )

##        if j==0:ax1.legend(facecolor='None',edgecolor='None'
##           ,loc='center left'
####            , bbox_to_anchor=(0.923, 1.5)
####                           ,ncol=2
##           )

        ax1.set_xlim(-1.3,2.3)
        ax1.set_ylim(-40,90)
        ax1.set_xticks([-1,0,1,2])
##        ax1.set_yticks([-50,0,50])
        if j!=2:ax1.set_xticklabels([])
        ax1.yaxis.set_ticks_position('both')
        ax1.xaxis.set_ticks_position('both')
        ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
        ax1.yaxis.set_minor_locator(MultipleLocator(10))

        ax2.set_xlim(-1.2,1.2)
        ax2.set_ylim(-40,90)
        ax2.set_xticks([-1,0,1])
##        ax2.set_yticks([-50,0,50])
        if j!=2:ax2.set_xticklabels([])
        ax2.set_yticklabels([])
        ax2.yaxis.set_ticks_position('both')
        ax2.xaxis.set_ticks_position('both')
        ax2.xaxis.set_minor_locator(MultipleLocator(0.5))
        ax2.yaxis.set_minor_locator(MultipleLocator(10))

        ax3.set_xlim(-5,100)
        ax3.set_ylim(-40,90)
        ax3.set_xticks([0,50,100])
##        ax3.set_yticks([-50,0,50])
        if j!=2:ax3.set_xticklabels([])
        ax3.set_yticklabels([])
        ax3.yaxis.set_ticks_position('both')
        ax3.xaxis.set_ticks_position('both')
        ax3.xaxis.set_minor_locator(MultipleLocator(25))
        ax3.yaxis.set_minor_locator(MultipleLocator(10))

    #fig.tight_layout()
    fig.subplots_adjust(left=0.1,bottom=0.1,wspace=0.06,hspace=0.06)
    # You need specify the directory where output is made 
    Workdir = './'
    Workdir = 'C:/Users/YK/Desktop/Sediment/'
    outfilename = Workdir+outname+".svg"
    plt.savefig(outfilename, transparent=True)
    subprocess.call('"C:\Program Files\Inkscape\inkscape.exe" -z -f ' \
                    + outfilename + ' --export-emf '+outfilename+\
                    '.emf',shell=True)
    plt.show()
    plt.clf()
    plt.close()

if __name__ == '__main__':
    main()