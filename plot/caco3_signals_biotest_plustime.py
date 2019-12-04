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

def sigplot(multi,python,test,ox,oxanox,labs,turbo2,nobio,filename
            ,i,axes,dep,realtimeplot):
    
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
        label = 'LABS mixing'
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

    print 'end input-',i



    ls = np.array([':','--','-','-'])
    dsp = [(1,3),(5,5),[5,3,1,3],(5,0)]

    if dep:
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[0,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,9]*0.5*(sig[k+1,10]+sig[k+1,10]) \
                      *(sig[k+1,11]-sig[k,11])

        xp = sig[:,0]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)

        if i==0:axes[0].plot(bound[:,1],zrecb,'-',c='hotpink'
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1],zrec,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2],zrecb,'-',c='hotpink'
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],zrec,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[2].plot((bound[:,0]-rectime[4])/1e3
                         ,zrecb,'-',c='hotpink'
                         ,label='Input'
                     )
        axes[2].plot((sig[:,7]-rectime[4])/1e3,zrec,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        
        axes[3].plot(sig[:,3],zrec,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        
    elif realtimeplot:

        if i==0:axes[0].plot(bound[:,1]
                             ,(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1]
                     ,(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2]
                             ,(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        
        axes[2].plot(sig[:,3],(sig[:,7]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
    else:

        if i==0:axes[0].plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1],(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[2].plot((bound[:,0]-rectime[4])/1e3,(bound[:,0]-rectime[4])/1e3,'-',c='hotpink'
                         ,label='Input'
                     )
        axes[2].plot((sig[:,7]-rectime[4])/1e3,(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )
        
        axes[3].plot(sig[:,3],(sig[:,0]-rectime[4])/1e3,ls[i],c='k', dashes=dsp[i]
                 ,label=label
                     )

def main():
    nexp = 4  # Here you can specify the number of plot, 1 to 3 

    multi = np.zeros(nexp,dtype=bool)
    test = np.zeros(nexp,dtype=bool)
    ox = np.zeros(nexp,dtype=bool)
    oxanox = np.zeros(nexp,dtype=bool)
    labs = np.zeros(nexp,dtype=bool)
    turbo2 = np.zeros(nexp,dtype=bool)
    nobio = np.zeros(nexp,dtype=bool)

    python= False

    multi[:]=True
    if not python: test[:]=True
    ox[:]=True
    oxanox[:]=True
    if nexp>1:nobio[0]=True
    if nexp>2:turbo2[2]=True
    if nexp>2:labs[3]=True
    # name below are used for figure
    outname = 'chk-biot_rtime'

    dep = False
    realtimeplot = True
    if realtimeplot: dep = False
    if dep: realtimeplot = False
    
    fs=12

    if not realtimeplot:
        nx = 4
        figsize = (7,6)
        tx = 4.4
        ty = 0.5
        if dep: outname += '_dep'
    else:
        nx = 3
        figsize = (7*3/4.,6)
        tx = 3.3
        ty = 0.5
        outname += '_REAL'
    if python: outname += '_py'
    ny =2
    fig = plt.figure(figsize=figsize) # long
    axes = [[plt.subplot2grid((ny,nx), (j,i)) for i in range(nx)]
            for j in range(ny)]
    filename=[['cc-0.12E-4_rr-0.70E+0_chk_biot_nd']*4
              ,['cc-0.12E-4_rr-0.70E+0_chk_biot_d']*4]
    if python:
        filename=[['cc-1.2e-05_rr-7.0e-01-test_time_biot_nd']*4
                  ,['cc-1.2e-05_rr-7.0e-01-test_time_biot']*4]
    for j in range(ny):
        for i in range(nexp):
            sigplot(multi[i],python,test[i],ox[i],oxanox[i]
                    ,labs[i],turbo2[i],nobio[i],filename[j][i]
                    ,i,axes[j],dep, realtimeplot)
        if j==0:txtmsg = "Dissolution 'off'"
        if j==1:txtmsg = "Dissolution 'on'"
        axes[j][-1].text(tx, ty
             ,txtmsg
             ,horizontalalignment='center',verticalalignment='center'\
             , transform=axes[j][0].transAxes
             ,rotation=90
             )

##        if j==0:ax1.legend(facecolor='None',edgecolor='None'
##           ,loc='center left'
####            , bbox_to_anchor=(0.923, 1.5)
####                           ,ncol=2
##           )
        for ii in range(nx):
            # x range and ticks
            if ii ==0:
                axes[j][ii].set_xlim(-1.3,2.3)
                axes[j][ii].set_xticks([-1,0,1,2])
            elif ii==1:
                axes[j][ii].set_xlim(-1.2,1.2)
                axes[j][ii].set_xticks([-1,0,1])
            elif ii==2:
                if not realtimeplot:
                    axes[j][ii].set_xlim(-30,30)
                    axes[j][ii].set_xticks([-30,-20,-10,0,10,20,30])
                else:
                    axes[j][ii].set_xlim(65,100)
                    axes[j][ii].set_xticks([70,80,90,100])
            elif ii==3:
                axes[j][ii].set_xlim(65,100)
                axes[j][ii].set_xticks([70,80,90,100])
            if ii==0 or ii==1:
                axes[j][ii].xaxis.set_minor_locator(MultipleLocator(0.5))
            if ii==2 or ii==3:
                axes[j][ii].xaxis.set_minor_locator(MultipleLocator(5))
            # y range and ticks
            if not dep:
                axes[j][ii].set_ylim(-25,30)
                axes[j][ii].yaxis.set_minor_locator(MultipleLocator(5))
                axes[j][ii].set_yticks([-20,-10,0,10,20,30])
            else:
                if j==0:
                    axes[j][ii].set_ylim(30,42)
                    axes[j][ii].set_yticks([30,35,40])
                else:
                    axes[j][ii].set_ylim(20,34)
                axes[j][ii].invert_yaxis()
                axes[j][ii].yaxis.set_minor_locator(MultipleLocator(1))
            # x tick labels 
            if j!=1:
                axes[j][ii].set_xticklabels([])
            else:
                if ii==0:
                    axes[j][ii].set_xticklabels(['-1','0','1','2'])
                elif ii==1:
                    axes[j][ii].set_xticklabels(['-1','0','1'])
                elif ii==2:
                    if not realtimeplot:
                        axes[j][ii].set_xticklabels(
                            ['','-20','','0','','20','']
                            )
                    else:axes[j][ii].set_xticklabels(['','80','','100'])
                elif ii==3:
                    axes[j][ii].set_xticklabels(['','80','','100'])
            # y tick labels 
            if ii!=0:
                axes[j][ii].set_yticklabels([])
            # ticks locations  
            axes[j][ii].yaxis.set_ticks_position('both')
            axes[j][ii].xaxis.set_ticks_position('both')
            
    #fig.tight_layout()
    fig.subplots_adjust(left=0.12,bottom=0.1,wspace=0.06,hspace=0.06)
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
