# -*- coding: utf-8 -*-
import numpy as np
import os
import subprocess
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib import mathtext
mathtext.FontConstantsBase = mathtext.ComputerModernFontConstants

"""
caco3 signal profiles 
"""

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

def sigplot(code,ox,oxanox,labs,turbo2,nobio,simname,filename
            ,i,axes,pltstyle):
    
    # the following part is used to specify the location of individual result data 
    # in consistent with how and where to record the results 
    Workdir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    Workdir += '/imp_output/'
    # Workdir = 'C:/cygwin64/home/YK/imp_output/'
    Workdir += code+'/'
    Workdir += simname+'/profiles/'
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
        if len(axes)==3:
            label='Homogeneous\nmixing'
    else: 
        if oxanox:Workdir += 'oxanox/'
        else: Workdir += 'ox/'
        label ='Fickian mixing'
        
    Workdir += filename
    Workdir += '/'
    
    rectime = np.loadtxt(Workdir+'rectime.txt')
    sig = np.loadtxt(Workdir+'sigmly.txt',skiprows =20)
    bound = np.loadtxt(Workdir+'bound.txt')
    recz = np.loadtxt(Workdir+'recz.txt')

    print 'end input-',i



    ls = np.array([':','-','-','--'])
    dsp = [(1,3),(5,0),(5,5),[5,3,1,3]]
    cls = ['k']*4
    
    ls = ['-']*4
    dsp = [(5,0)]*4
    cls = ['hotpink','royalblue','limegreen','orange']
    refc = 'k'
    refls = ':'
    refds = (1,1)
    reflw = 2

    if pltstyle=='diagdep_time':
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[0,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,9]*0.5*(sig[k+1,10]+sig[k+1,10]) \
                      *(sig[k+1,11]-sig[k,11])

        xp = sig[:,7]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)

        if i==0:axes[0].plot(bound[:,1],zrecb,refls,c=refc,lw = reflw
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2],zrecb,refls,c=refc,lw = reflw
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[2].plot((bound[:,0]-rectime[4])/1e3
                         ,zrecb,refls,c=refc,lw = reflw
                         ,label='Input'
                     )
        axes[2].plot((sig[:,7]-rectime[4])/1e3,zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[3].plot(sig[:,3],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
    elif pltstyle=='time':

        if i==0:axes[0].plot(bound[:,1]
                             ,(bound[:,0]-rectime[4])/1e3,refls,c=refc,lw = reflw
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1]
                     ,(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2]
                             ,(bound[:,0]-rectime[4])/1e3,refls,c=refc,lw = reflw
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[2].plot(sig[:,3],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
    elif pltstyle=='diagdep':
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[0,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,9]*0.5*(sig[k+1,10]+sig[k+1,10]) \
                      *(sig[k+1,11]-sig[k,11])

        xp = sig[:,7]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)

        if i==0:axes[0].plot(bound[:,1]
                             ,zrecb,refls,c=refc,lw = reflw
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1]
                     ,zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2]
                             ,zrecb,refls,c=refc,lw = reflw
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[2].plot(sig[:,3],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
    elif pltstyle=='diagtime':

        if i==0:axes[0].plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,refls,c=refc,lw = reflw
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1],(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,refls,c=refc,lw = reflw
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[2].plot((bound[:,0]-rectime[4])/1e3,(bound[:,0]-rectime[4])/1e3,refls,c=refc,lw = reflw
                         ,label='Input'
                     )
        axes[2].plot((sig[:,7]-rectime[4])/1e3,(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[3].plot(sig[:,3],(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

def main():
    nexp = 4  # Here you can specify the number of plot, 1 to 3 

    ox = np.zeros(nexp,dtype=bool)
    oxanox = np.zeros(nexp,dtype=bool)
    labs = np.zeros(nexp,dtype=bool)
    turbo2 = np.zeros(nexp,dtype=bool)
    nobio = np.zeros(nexp,dtype=bool)


    ox[:]=True
    oxanox[:]=True
    if nexp>1:nobio[0]=True
    if nexp>2:turbo2[2]=True
    if nexp>2:labs[3]=True
    # name below are used for figure
    outname = 'biot_reading'

    dep = False
    realtimeplot = False
    
    legend = True
    # legend = False
    
    pltstyle = 'diagdep' # plotting against diagnosed depth without tracking model time
    # pltstyle = 'diagdep_time' # plotting against diagnosed depth with tracking model time as a proxy 
    # pltstyle = 'time'  # plotting against model time when tracked 
    # pltstyle = 'diagtime'  # plotting against diagnosed time  
    
    outname += '_'+pltstyle
    
    fs=12
    
    if pltstyle=='time' or pltstyle =='diagdep':
        nx = 3
        figsize = (8*3/4.,7)
        tx = 3.3
        ty = 0.5
    else :
        nx = 4
        figsize = (8,7)
        tx = 4.4
        ty = 0.5
    ny =2
    fig = plt.figure(figsize=figsize) # long
    axes = [[plt.subplot2grid((ny,nx), (j,i)) for i in range(nx)]
            for j in range(ny)]
    
    # specigy code used, ('fortran', 'python' or 'matlab')
    # simulation name and filename 
    # in lists code, simname, and filename respectively
    # following are three sets of examples 
    # when fortran, matlab and python are used 
    
    # fortran example
    
    # code = [
        # ['fortran']*4
        # ,['fortran']*4
        # ]
    # simname=[['test_biot_read_nd_v2']*4
              # ,['test_biot_read_v2']*4]    
    # filename=[['cc-0.12E-4_rr-0.70E+0_chk_biot_nd']*4
              # ,['cc-0.12E-4_rr-0.70E+0_chk_biot_d']*4]
              
    # python example
    code = [
        ['python']*4
        ,['python']*4
        ]
    simname=[['test_time_biot_nd_v2']*4
              ,['test_time_biot_v2']*4]
    filename=[['cc-1.2e-05_rr-7.0e-01_dep-3.5e+00']*4
              ,['cc-1.2e-05_rr-7.0e-01_dep-3.5e+00']*4]
              
    # matlab example
    code = [
        ['matlab']*4
        ,['matlab']*4
        ]
    simname=[['test_reading_time_biot_nd']*4
              ,['test_reading_time_biot']*4]
    filename=[['cc-1.2e-05_rr-0.7_dep-3.5']*4
              ,['cc-1.2e-05_rr-0.7_dep-3.5']*4]
    
    if 'fortran' in np.array(code): outname += '_fortran'
    if 'python' in np.array(code): outname += '_python'
    if 'matlab' in np.array(code): outname += '_matlab'
    
    if pltstyle =='diagdep' or pltstyle=='diagdep_time':dep = True
    if pltstyle =='diagdep' or pltstyle=='time':realtimeplot = True
    
    for j in range(ny):
        for i in range(nexp):
            sigplot(code[j][i],ox[i],oxanox[i]
                    ,labs[i],turbo2[i],nobio[i],simname[j][i],filename[j][i]
                    ,i,axes[j],pltstyle)
        if j==0:txtmsg = "Dissolution 'off'"
        if j==1:txtmsg = "Dissolution 'on'"
        axes[j][-1].text(tx, ty
             ,txtmsg
             ,horizontalalignment='center',verticalalignment='center'\
             , transform=axes[j][0].transAxes
             ,rotation=90
             )

        if legend and j==0:
            if nx ==4: posi = (0.0, 1.0)
            if nx ==3: posi = (-0.4, 1.0)
            axes[j][0].legend(facecolor='None',edgecolor='None'
                ,loc='lower left'
                , bbox_to_anchor=posi
                ,ncol=2
                )
                
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
                # axes[j][ii].set_ylim(-25,30)
                axes[j][ii].set_ylim(-12,18)
                # axes[j][ii].yaxis.set_minor_locator(MultipleLocator(5))
                axes[j][ii].yaxis.set_minor_locator(MultipleLocator(5))
                # axes[j][ii].set_yticks([-20,-10,0,10,20,30])
                axes[j][ii].set_yticks([-10,0,10])
            else:
                if j==0:
                    # axes[j][ii].set_ylim(30,42)
                    # axes[j][ii].set_yticks([30,35,40])
                    axes[j][ii].set_ylim(33,45)
                    axes[j][ii].set_yticks([35,40,45])
                else:
                    # axes[j][ii].set_ylim(20,34)
                    axes[j][ii].set_ylim(22,36)
                axes[j][ii].invert_yaxis()
                axes[j][ii].yaxis.set_minor_locator(MultipleLocator(1))
            # x tick labels 
            if j!=1:
                axes[j][ii].set_xticklabels([])
            else:
                if ii==0:
                    axes[j][ii].set_xticklabels(['-1','0','1','2'])
                    axes[j][ii].set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{13}}$C'+' ('+u'$‰$'+')')
                elif ii==1:
                    axes[j][ii].set_xticklabels(['-1','0','1'])
                    axes[j][ii].set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{18}}$O'+' ('+u'$‰$'+')')
                elif ii==2:
                    if not realtimeplot:
                        axes[j][ii].set_xticklabels(
                            ['','-20','','0','','20','']
                            )
                        axes[j][ii].set_xlabel('Time (kyr)',labelpad = 15)
                    else:
                        axes[j][ii].set_xticklabels(['','80','','100'])
                        axes[j][ii].set_xlabel('CaCO'+r'$\mathregular{_{3}}$'+' wt%')
                elif ii==3:
                    axes[j][ii].set_xticklabels(['','80','','100'])
                    axes[j][ii].set_xlabel('CaCO'+r'$\mathregular{_{3}}$'+' wt%')
            # y tick labels 
            if ii!=0:
                axes[j][ii].set_yticklabels([])
            else:
                if dep:axes[j][ii].set_ylabel(r'$\mathregular{\it{z}_{\rm{diag}}}$'+' (cm)')
                if not dep:axes[j][ii].set_ylabel('Time (kyr)')
            # ticks locations  
            axes[j][ii].yaxis.set_ticks_position('both')
            axes[j][ii].xaxis.set_ticks_position('both')
            
    for ax in axes[1]:
        labelx = 0.5
        labely = -0.2
        ax.xaxis.set_label_coords(labelx, labely)
        
    #fig.tight_layout()
    if not legend:fig.subplots_adjust(left=0.15,bottom=0.12,wspace=0.06,hspace=0.06)
    if legend:fig.subplots_adjust(left=0.15,bottom=0.12,wspace=0.06,hspace=0.06,top=0.8)
    # fig.align_xlabels([axes[1][0],axes[1][1],axes[1][2],axes[1][3]])
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
