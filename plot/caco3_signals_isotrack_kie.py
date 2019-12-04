# -*- coding: utf-8 -*-
import numpy as np
import subprocess
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

"""
caco3 signal profiles including clumped isotopes
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

def sigplot(multi,python,test,ox,oxanox,labs,turbo2,nobio
            ,filename,i,ax1,ax2,ax3,ax4,ax5,ax6
            ,filename_kie
            ,realtime
            ):
    
    # the following part is used to specify the location of individual result data 
    # in consistent with how and where to record the results 
    Workdir = 'C:/cygwin64/home/YK/imp_output/'
    Workdir += 'fortran/profiles/'
    if python: Workdir += 'python/'
    if multi: Workdir += 'multi/'
    if test: Workdir += 'test/'
    if labs:
        if oxanox:Workdir += 'oxanox_labs/'
        else:Workdir += 'ox_labs/'
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

    Workdir_kie = Workdir + filename_kie 
    Workdir_kie += '/'
    
    Workdir += filename
    Workdir += '/'
    
    # Otherwise, specify here directly the directory which store calculation results and remove comment-out
##    Workdir = './MATLAB/resprofiles/'
    # Workdir = './'
    
    rectime = np.loadtxt(Workdir+'rectime.txt')
##    frac = np.loadtxt(Workdir+'frac.txt')
    sig = np.loadtxt(Workdir+'sigmly.txt')
    bound = np.loadtxt(Workdir+'bound.txt')
    
    rectime_kie = np.loadtxt(Workdir_kie+'rectime.txt')
    sig_kie = np.loadtxt(Workdir_kie+'sigmly.txt')
    bound_kie = np.loadtxt(Workdir_kie+'bound.txt')

    print 'end input-',i

    ckie = 'g'


    ls = np.array([':','--','-'])
    dsp = [(1,2),(5,2),[5,2,1,2]]

    if realtime:

        ax1.plot(sig[:,1],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax1.plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )

        ax2.plot(sig[:,2],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax2.plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )
        ax3.plot(sig[:,3],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
                     
        ax4.plot(sig[:,5]/1e3,(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
                     
        ax5.plot(sig[:,6],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax5.plot(bound[:,3],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )
                     
        ax6.plot(sig[:,6],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        ax6.plot(sig_kie[:,6],(sig_kie[:,7]-rectime_kie[4])/1e3
                 ,ls[i],c=ckie, dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax6.plot(bound[:,3],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )

    else:

        ax1.plot(sig[:,1],(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax1.plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )

        ax2.plot(sig[:,2],(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax2.plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )
        ax3.plot(sig[:,3],(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
                     
        ax4.plot(sig[:,5]/1e3,(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
                     
        ax5.plot(sig[:,6],(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax5.plot(bound[:,3],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )
                     
        ax6.plot(sig[:,6],(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        ax6.plot(sig_kie[:,6],(sig_kie[:,0]-rectime_kie[4])/1e3
                 ,ls[i],c=ckie, dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax6.plot(bound[:,3],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
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
##    python= True

    multi[:]=True
    if not python:test[:]=True
    ox[:]=True
    oxanox[:]=True
    if nexp>1:nobio[0]=True
    if nexp>2:turbo2[2]=True
    # simulation file names are listed below
    filename=[
        'cc-0.12E-4_rr-0.70E+0_chk_iso_d5.0'
        ]*nexp
    filename_kie=[
        'cc-0.12E-4_rr-0.70E+0_chk_kie_d5.0'
        ]*nexp
##    filename[2]='cc-0.12E-4_rr-0.70E+0_test_t_iso_dis5.0'
##    filename_kie[2]='cc-0.12E-4_rr-0.70E+0_test_t_iso_dis5.0'
    # name below are used for figure
    outname = 'chk_iso_kie_rtime'

    realtime=True

    fs=12

    nx = 3
    ny =2
    fig = plt.figure(figsize=(7,10)) # long
    ax1 = plt.subplot2grid((ny,nx), (0,0))
    ax2 = plt.subplot2grid((ny,nx), (0,1))
    ax3 = plt.subplot2grid((ny,nx), (0,2))
    ax4 = plt.subplot2grid((ny,nx), (1,0))
    ax5 = plt.subplot2grid((ny,nx), (1,1))
    ax6 = plt.subplot2grid((ny,nx), (1,2))
    for i in range(nexp):
        sigplot(multi[i],python,test[i],ox[i],oxanox[i]
                ,labs[i],turbo2[i],nobio[i],filename[i]
                ,i,ax1,ax2,ax3,ax4,ax5,ax6
                ,filename_kie[i]
                ,realtime
                )

    ax1.set_xlim(-1.3,2.3)
    ax1.set_ylim(-40,90)
    ax1.set_xticks([-1,0,1,2])
    ax1.set_yticks([0,50])
    ax1.yaxis.set_ticks_position('both')
    ax1.xaxis.set_ticks_position('both')
    ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax1.yaxis.set_minor_locator(MultipleLocator(10))

    ax2.set_xlim(-1.2,1.2)
    ax2.set_ylim(-40,90)
    ax2.set_xticks([-1,0,1])
    ax2.set_yticks([0,50])
    ax2.set_yticklabels([])
    ax2.yaxis.set_ticks_position('both')
    ax2.xaxis.set_ticks_position('both')
    ax2.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax2.yaxis.set_minor_locator(MultipleLocator(10))

    ax3.set_xlim(-5,100)
    ax3.set_ylim(-40,90)
    ax3.set_xticks([0,50,100])
    ax3.set_yticks([0,50])
    ax3.set_yticklabels([])
    ax3.yaxis.set_ticks_position('both')
    ax3.xaxis.set_ticks_position('both')
    ax3.xaxis.set_minor_locator(MultipleLocator(25))
    ax3.yaxis.set_minor_locator(MultipleLocator(10))

    ax4.set_xlim(-3,60)
    ax4.set_ylim(-40,90)
    ax4.set_xticks([0,50])
    ax4.set_yticks([0,50])
##    ax4.set_xscale('log')
    ax4.yaxis.set_ticks_position('both')
    ax4.xaxis.set_ticks_position('both')
    ax4.xaxis.set_minor_locator(MultipleLocator(10))
    ax4.yaxis.set_minor_locator(MultipleLocator(10))

    ax5.set_xlim(0.49,0.61)
    ax5.set_ylim(-40,90)
    ax5.set_xticks([0.5,0.6])
    ax5.set_yticks([0,50])
    ax5.set_yticklabels([])
    ax5.yaxis.set_ticks_position('both')
    ax5.xaxis.set_ticks_position('both')
    ax5.xaxis.set_minor_locator(MultipleLocator(0.025))
    ax5.yaxis.set_minor_locator(MultipleLocator(10))

    ax6.set_xlim(0.4,1.1)
    ax6.set_ylim(-40,90)
    ax6.set_xticks([0.5,1.0])
    ax6.set_yticks([0,50])
    ax6.set_yticklabels([])
    ax6.yaxis.set_ticks_position('both')
    ax6.xaxis.set_ticks_position('both')
    ax6.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax6.yaxis.set_minor_locator(MultipleLocator(10))

##    ax6.set_xlim(-5,100)
##    ax6.set_ylim(70,-70)
##    ax6.set_xticks([0,50,100])
##    ax6.set_yticks([-50,0,50])
##    ax6.set_yticklabels([])
##    ax6.yaxis.set_ticks_position('both')
##    ax6.xaxis.set_ticks_position('both')
##    ax6.xaxis.set_minor_locator(MultipleLocator(25))
##    ax6.yaxis.set_minor_locator(MultipleLocator(10))

    
##    ax6.legend(facecolor='None',edgecolor='None'
##               ,fontsize=14,ncol=1
##               ,loc='lower center'
##            , bbox_to_anchor=(0.67, 0.5)
##               )
##    
##    tx = 2.8
##    ty = -1.0
##    ax6.text(tx, ty
##         ,'Blue : with KIE ('+r'$\mathregular{-5}$'+r'$\cdot$'
##             +r'$\mathregular{10^{-5}}$'+')'
##         ,horizontalalignment='center',verticalalignment='center'\
##         , transform=ax1.transAxes
##         ,fontsize=14
##             ,color='b'
##         )
##    
##    tx = 2.65
##    ty = -1.08
##    ax6.text(tx, ty
##         ,'Black: without KIE'
##         ,horizontalalignment='center',verticalalignment='center'\
##         , transform=ax1.transAxes
##         ,fontsize=14
##             ,color='k'
##         )

##    ax6.tick_params(labelbottom="off",bottom="off")
##    ax6.tick_params(labelleft="off",left="off")
##    ax6.set_xticklabels([])
##    ax6.set_yticklabels([])
##    ax6.spines["right"].set_color("none")  
##    ax6.spines["left"].set_color("none")   
##    ax6.spines["top"].set_color("none")    
##    ax6.spines["bottom"].set_color("none")
##    ax6.set_xlim(-50,-20)

    ##fig.tight_layout()
    fig.subplots_adjust(left=0.1,bottom=0.1,wspace=0.06,hspace=0.3)
    # You need specify the directory where output is made 
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
