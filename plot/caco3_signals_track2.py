# -*- coding: utf-8 -*-
import numpy as np
import os
import subprocess
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

"""
caco3 signal profiles 
"""

plt.rcParams['font.family'] = 'Arial' 
plt.rcParams['font.size'] = 16

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

def sigplot(multi,python,test,ox,oxanox,labs,turbo2,nobio,filename,i,ax1,ax2,ax3,j):
    
    # the following part is used to specify the location of individual result data 
    # in consistent with how and where to record the results 
    # if j==0:
    Workdir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    Workdir += '/imp_output/'
    Workdir += 'fortran/'
    # Workdir += 'test-translabs/profiles/'
    if j==0:Workdir += 'track2_42_dis5'     # input simulation name with track method 1
    if j==1:Workdir += 'test_dis5_nonread'  # input simulation name with track method 2
    Workdir += '/profiles/'
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
    recz = np.loadtxt(Workdir+'recz.txt')

    print 'end input-',i,sig.shape

    # inputdata = np.loadtxt('E:/caco3'+str(i)+'.txt')
    # zrec=np.interp(sig[:,3],inputdata[:,0],inputdata[:,1])

    ls = np.array([':','--','-'])
    dsp = [(1,2),(5,2),[5,2,1,2]]
    cc = 'k'
    
    ls = ['-']*4
    dsp = [(5,0)]*4
    # cls = ['b','r','g','m']
    cls = ['hotpink','royalblue','limegreen','orange']
    refc = 'k'
    refls = ':'
    refds = (1,1)
    reflw = 2

    zrec = np.zeros(sig[:,0].shape[0])
    zrec[-1]=recz[0,2]
    for k in reversed(range(sig[:,0].shape[0]-1)):
        zrec[k] = zrec[k+1]+sig[k,9]*0.5*(sig[k+1,10]+sig[k+1,10])*(sig[k+1,11]-sig[k,11]) 

    xp = sig[:,0]
    yp = zrec[:]
    zrecb = np.interp(bound[:,0],xp,yp)



    # if i==0:ax1.plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                     # ,label = 'Input'
                 # )
    ax1.plot(sig[:,1],zrec,ls[i],c=cls[i], dashes=dsp[i]
             ,label=label
                 )

    # if i==0:ax2.plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                     # ,label='Input'
                 # )
    ax2.plot(sig[:,2],zrec,ls[i],c=cls[i], dashes=dsp[i]
             ,label=label
             )
    ax3.plot(sig[:,3],zrec,ls[i],c=cls[i], dashes=dsp[i]
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

    # name below are used for figure
    outname = 'trck2_dep_comp'

    fs=12

    nx = 3
    ny =2
    tx = 3.3
    ty = 0.5
    fig = plt.figure(figsize=(7,6)) # long
    for j in range(2):
        if j==0:
            filename=['cc-0.12E-4_rr-0.70E+0_dep-0.50E+1']*3  # input file names for simulation with track method 1
        if j==1: 
            filename=[
                'cc-0.12E-4_rr-0.70E+0_dep-0.50E+1' # input file names for simulation with track method 2
                ]*3
        ax1 = plt.subplot2grid((ny,nx), (j,0))
        ax2 = plt.subplot2grid((ny,nx), (j,1))
        ax3 = plt.subplot2grid((ny,nx), (j,2))
        for i in range(nexp):
            sigplot(multi[i],python,test[i],ox[i],oxanox[i]\
                    ,labs[i],turbo2[i],nobio[i],filename[i],i,ax1,ax2,ax3,j)
        
        if j==0: text = 'Method 1'
        else: text = 'Method 2'
        tx = 3.3
        ty = 0.5
        
        ax3.text(tx, ty
             ,text
             ,horizontalalignment='center',verticalalignment='center'\
             , transform=ax1.transAxes
             ,rotation=90
             )

        if j==0:
            ax1.legend(facecolor='None',edgecolor='None'
                ,loc='center left'
                , bbox_to_anchor=(-0.1, 1.15)
                ,ncol=2
                ,handlelength=1.7
                ,handletextpad = 0.2
                )

        ax1.set_xlim(-1.3,2.3)
        # ax1.set_ylim(-40,90)
        ax1.set_ylim(40,75)
        ax1.set_xticks([-1,0,1,2])
        ax1.invert_yaxis()
##        ax1.set_yticks([-50,0,50])
        if j==0:ax1.set_xticklabels([])
        if j==1:ax1.set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{13}}$C'+' ('+u'$‰$'+')')
        ax1.set_ylabel(r'$\mathregular{\it{z}_{\rm{diag}}}$'+' (cm)')
        ax1.yaxis.set_ticks_position('both')
        ax1.xaxis.set_ticks_position('both')
        ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
        ax1.yaxis.set_minor_locator(MultipleLocator(5))

        ax2.set_xlim(-1.2,1.2)
        # ax2.set_ylim(-40,90)
        ax2.set_ylim(40,75)
        ax2.set_xticks([-1,0,1])
        ax2.invert_yaxis()
##        ax2.set_yticks([-50,0,50])
##        if j!=2:ax2.set_xticklabels([])
        ax2.set_yticklabels([])
        if j==0:ax2.set_xticklabels([])
        if j==1:ax2.set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{18}}$O'+' ('+u'$‰$'+')')
        ax2.yaxis.set_ticks_position('both')
        ax2.xaxis.set_ticks_position('both')
        ax2.xaxis.set_minor_locator(MultipleLocator(0.5))
        ax2.yaxis.set_minor_locator(MultipleLocator(5))

        ax3.set_xlim(-5,100)
        # ax3.set_ylim(-40,90)
        ax3.set_ylim(40,75)
        ax3.set_xticks([0,50,100])
        ax3.invert_yaxis()
##        ax3.set_yticks([-50,0,50])
##        if j!=2:ax3.set_xticklabels([])
        ax3.set_yticklabels([])
        if j==0:ax3.set_xticklabels([])
        if j==1:ax3.set_xlabel('CaCO'+r'$\mathregular{_{3}}$'+' wt%')
        ax3.yaxis.set_ticks_position('both')
        ax3.xaxis.set_ticks_position('both')
        ax3.xaxis.set_minor_locator(MultipleLocator(25))
        ax3.yaxis.set_minor_locator(MultipleLocator(5))

    #fig.tight_layout()
    fig.subplots_adjust(left=0.15,bottom=0.12,wspace=0.06,hspace=0.06)
    Workdir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    Workdir += '/imp_output/'
    # You can specify the directory where output is made 
    # Workdir = './'
    # Workdir = 'C:/Users/YK/Desktop/Sediment/IMP/'
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
