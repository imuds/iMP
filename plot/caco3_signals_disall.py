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

def sigplot(code,ox,oxanox,labs,turbo2,nobio,simname,filename,i,axes,pltstyle):
    
    # the following part is used to specify the location of individual result data 
    # in consistent with how and where to record the results 
    Workdir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    Workdir += '/imp_output/'
    # Workdir = 'C:/cygwin64/home/YK/imp_output/'
    # Workdir = 'E:/imp_output/'
    Workdir += code+'/'+simname+'/'
    Workdir += 'profiles/'
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
    
    rectime = np.loadtxt(Workdir+'rectime.txt')
    sig = np.loadtxt(Workdir+'sigmly.txt',skiprows=20)
    bound = np.loadtxt(Workdir+'bound.txt')
    recz = np.loadtxt(Workdir+'recz.txt')

    print 'end input-',i
    
    ls = np.array([':','-','-','--'])
    dsp = [(1,3),(5,0),(5,5),[5,3,1,3]]
    cls = ['k']*4
    refc = 'hotpink'
    refls = '-'
    refds = (5,0)
    
    ls = ['-']*4
    dsp = [(5,0)]*4
    cls = ['hotpink','royalblue','limegreen','orange']
    refc = 'k'
    refls = ':'
    refds = (1,1)
    reflw = 2

    if pltstyle == 'diagdep':
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[0,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,9]*0.5*(sig[k+1,10]+sig[k+1,10]) \
                      *(sig[k+1,11]-sig[k,11])  #  sporo*wdt (time_below - time)

        xp = sig[:,7]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)

        if i==0:axes[0].plot(bound[:,1],zrecb,refls,c=refc,dashes = refds,lw = reflw
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2],zrecb,refls,c=refc,dashes = refds,lw = reflw
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        axes[2].plot(sig[:,3],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

    if pltstyle == 'diagdep_time':
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[0,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,9]*0.5*(sig[k+1,10]+sig[k+1,10]) \
                      *(sig[k+1,11]-sig[k,11])  #  sporo*wdt (time_below - time)

        xp = sig[:,7]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)

        if i==0:axes[0].plot(bound[:,1],zrecb,refls,c=refc,dashes = refds,lw = reflw
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2],zrecb,refls,c=refc,dashes = refds,lw = reflw
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

    elif pltstyle == 'time':

        if i==0:axes[0].plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,refls,c=refc,dashes = refds,lw = reflw
                         ,label = 'Input'
                     )
        axes[0].plot(sig[:,1],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        if i==0:axes[1].plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,refls,c=refc,dashes = refds,lw = reflw
                         ,label='Input'
                     )
        axes[1].plot(sig[:,2],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        axes[2].plot(sig[:,3],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

def main():
    nexp = 3  # Here you can specify the number of plot, 1 to 3 

    ox = np.zeros(nexp,dtype=bool)
    oxanox = np.zeros(nexp,dtype=bool)
    labs = np.zeros(nexp,dtype=bool)
    turbo2 = np.zeros(nexp,dtype=bool)
    nobio = np.zeros(nexp,dtype=bool)

    ox[:]=True
    oxanox[:]=True
    if nexp>1:nobio[0]=True
    if nexp>2:turbo2[2]=True
    
    # name below are used for figure
    outname = 'dis_exp_reading' 
    
    # specify on what axis signals should be plotted
    pltstyle = 'diagdep'  # plotting against diagnosed depth without tracking model time
    # pltstyle = 'diagdep_time' # plotting against diagnosed depth with tracking model time as a proxy 
    pltstyle = 'time'  # plotting against model time when tracked 
    
    outname += '_'+pltstyle
    
    # specigy code used, ('fortran', 'python' or 'matlab')
    # simulation name and filename 
    # in lists code, simname, and filename respectively
    # following are three sets of examples 
    # when matlab and python are used 
    
    # python example
    code = [
        ['python']*nexp
        ]*3
    
    simname = [
        ['test_reading_time_dis3.5']*nexp  # control 
        ,['test_reading_time_dis4.5']*nexp # dis exp. #1
        ,['test_reading_time_dis5.0']*nexp # dis exp. #2
        ]    
    
    filename = [
        ['cc-1.2e-05_rr-7.0e-01_dep-3.5e+00']*nexp # subfolder name which is created under simname directory
        ,['cc-1.2e-05_rr-7.0e-01_dep-3.5e+00']*nexp
        ,['cc-1.2e-05_rr-7.0e-01_dep-3.5e+00']*nexp
        ]
    
    # matlab example
    code = [
        ['matlab']*nexp
        ]*3
    
    simname = [
        ['test_reading_time_dis3.5']*nexp
        ,['test_reading_time_dis4.5']*nexp
        ,['test_reading_time_dis5.0']*nexp
        ]    
    
    filename = [
        ['cc-1.2e-05_rr-0.7_dep-3.5']*nexp
        ,['cc-1.2e-05_rr-0.7_dep-3.5']*nexp
        ,['cc-1.2e-05_rr-0.7_dep-3.5']*nexp
        ]
    
    if 'fortran' in np.array(code): outname += '_fortran'
    if 'python' in np.array(code): outname += '_python'
    if 'matlab' in np.array(code): outname += '_matlab'
    
    if pltstyle =='diagdep' or pltstyle=='diagdep_time': dep = True
    else: dep = False
    
    fs=12

    nx = 3
    ny =3
    if pltstyle=='diagdep_time': nx = 4
    tx = 1.15
    ty = 0.5
    
    off = 0
    if pltstyle=='diagdep_time': fig = plt.figure(figsize=(8,6*3/2.)) # long
    else: fig = plt.figure(figsize=(8*3/4.,6*3/2.)) # long
    for j in range(3):
        axes = [plt.subplot2grid((ny,nx), (j,i)) for i in range(nx)]
        for i in range(nexp):
            sigplot(code[j][i],ox[i],oxanox[i]
                    ,labs[i],turbo2[i],nobio[i],simname[j][i],filename[j][i],i,axes,pltstyle)

        if j==0: text = 'Control'
        else: text = 'Diss. exp.' +str(j)
        
        if pltstyle=='diagdep_time': 
            axes[3].text(tx, ty
                 ,text
                 ,horizontalalignment='center',verticalalignment='center'\
                 , transform=axes[3].transAxes
                 ,rotation=90
                 )
        else:
            axes[2].text(tx, ty
                 ,text
                 ,horizontalalignment='center',verticalalignment='center'\
                 , transform=axes[2].transAxes
                 ,rotation=90
                 )

        if j==0:
            axes[0].legend(facecolor='None',edgecolor='None'
                ,loc='center left'
                , bbox_to_anchor=(-0.4, 1.2)
                ,ncol=2
                ,handlelength=1.7
                ,handletextpad = 0.2
                )
        
        axes[0].set_xlim(-1.3,2.3)
        if not dep: axes[0].set_ylim(-40,90)
        if dep:axes[0].set_ylim(30+off,75+off)
        axes[0].set_xticks([-1,0,1,2])
        if j!=2:axes[0].set_xticklabels([])
        if j==2:axes[0].set_xlabel(r'$\mathregular{\delta^{13}}$'+'C ('+u'$‰$'+')')
        if j==1 and dep:axes[0].set_ylabel(r'$\mathregular{\it{z}_{\rm{diag}}}$'+' (cm)')
        if j==1 and not dep:axes[0].set_ylabel('Time (kyr)')
        if dep:axes[0].invert_yaxis()
        axes[0].yaxis.set_ticks_position('both')
        axes[0].xaxis.set_ticks_position('both')
        axes[0].xaxis.set_minor_locator(MultipleLocator(0.5))
        if dep:axes[0].yaxis.set_minor_locator(MultipleLocator(5))
        if not dep:axes[0].yaxis.set_minor_locator(MultipleLocator(10))

        axes[1].set_xlim(-1.2,1.2)
        if not dep: axes[1].set_ylim(-40,90)
        axes[1].set_xticks([-1,0,1])
        if dep:axes[1].set_ylim(30+off,75+off)
        if j!=2:axes[1].set_xticklabels([])
        if j==2:axes[1].set_xlabel(r'$\mathregular{\delta^{18}}$'+'O ('+u'$‰$'+')')
        if dep:axes[1].invert_yaxis()
        axes[1].set_yticklabels([])
        axes[1].yaxis.set_ticks_position('both')
        axes[1].xaxis.set_ticks_position('both')
        axes[1].xaxis.set_minor_locator(MultipleLocator(0.5))
        if dep:axes[1].yaxis.set_minor_locator(MultipleLocator(5))
        if not dep:axes[1].yaxis.set_minor_locator(MultipleLocator(10))
        
        if pltstyle=='diagdep_time': icarbonate = 3
        else: icarbonate = 2
        
        axes[icarbonate].set_xlim(-5,100)
        if not dep: axes[icarbonate].set_ylim(-40,90)
        axes[icarbonate].set_xticks([0,50,100])
        if dep:axes[icarbonate].set_ylim(30+off,75+off)
        if j!=2:axes[icarbonate].set_xticklabels([])
        if j==2:axes[icarbonate].set_xlabel('CaCO'+r'$\mathregular{_3}$'+' wt%')
        if dep:axes[icarbonate].invert_yaxis()
        axes[icarbonate].set_yticklabels([])
        axes[icarbonate].yaxis.set_ticks_position('both')
        axes[icarbonate].xaxis.set_ticks_position('both')
        axes[icarbonate].xaxis.set_minor_locator(MultipleLocator(25))
        if dep:axes[icarbonate].yaxis.set_minor_locator(MultipleLocator(5))
        if not dep:axes[icarbonate].yaxis.set_minor_locator(MultipleLocator(10))
        
        if pltstyle=='diagdep_time':        
            axes[2].set_xlim(-60,60)
            axes[2].set_ylim(30+off,75+off)
            if j!=2:axes[2].set_xticklabels([])
            if j==2:axes[2].set_xlabel('Time (kyr)')
            axes[2].invert_yaxis()
            axes[2].set_yticklabels([])
            axes[2].yaxis.set_ticks_position('both')
            axes[2].xaxis.set_ticks_position('both')
            axes[2].xaxis.set_minor_locator(MultipleLocator(25))
            axes[2].yaxis.set_minor_locator(MultipleLocator(5))
            

    fig.subplots_adjust(left=0.15,bottom=0.1,wspace=0.06,hspace=0.06)
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
