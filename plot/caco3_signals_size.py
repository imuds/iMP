# -*- coding: utf-8 -*-
import numpy as np
import subprocess
import os,sys
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

"""
caco3 signal profiles 
"""

def sigplot_ex(code,ox,oxanox,labs,turbo2,nobio,filename,simname
            ,i,axes,pltstyle):
    
    # the following part is used to specify the location of individual result data 
    # in consistent with how and where to record the results 
    Workdir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    Workdir += '/imp_output/'
    # Workdir = 'C:/cygwin64/home/YK/imp_output/'
    # Workdir = 'E:/imp_output/'
    Workdir += code+'/'
    Workdir += simname
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
    
    rectime = np.loadtxt(Workdir+'rectime.txt')
    sig = np.loadtxt(Workdir+'sigmly.txt',skiprows = 30)
    sigf = np.loadtxt(Workdir+'sigmlyd.txt',skiprows = 30)
    recz = np.loadtxt(Workdir+'recz.txt')

    ls = np.array([':','-','-','--'])
    dsp = [(1,3),(5,0),(5,5),[5,3,1,3]]
    cc = 'k'
    cf = 'royalblue'
    
    ls = ['-']*4
    dsp = [(5,0)]*4
    cls = ['hotpink','royalblue','limegreen','orange']
    refc = 'k'
    refls = ':'
    refds = (1,1)
    reflw = 2

    if pltstyle == 'diagdep':
        bound = np.loadtxt(Workdir+'bound.txt', skiprows=5)
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[1,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,15]*0.5*(sig[k+1,16]+sig[k+1,16])*(sig[k+1,17]-sig[k,17])  
        
        zrecf = np.zeros(sig[:,0].shape[0])
        zrecf[-1]=recz[0,2]
        for k in reversed(range(sigf[:,0].shape[0]-1)):
            zrecf[k] = zrecf[k+1]+sigf[k,15]*0.5*(sigf[k+1,16]+sigf[k+1,16])*(sigf[k+1,17]-sigf[k,17])  

        xp = sig[:,0]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)
        xp = sigf[:,0]
        yp = zrecf[:]
        zrecfb=np.interp(bound[:,0],xp,yp)
        
        lw = 2
        dspf = (1,1.5)
        
        axes[0].plot(sig[:,8],zrec,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        if i==0:axes[0].plot(sigf[:,5],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        else:axes[0].plot(sigf[:,5],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        axes[1].plot(sig[:,9],zrec,refls,c=cls[i], dashes=refds,lw = reflw
                 )
        if i!=0:axes[1].plot(sigf[:,6],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        else:axes[1].plot(sigf[:,6],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[2].plot(sig[:,10],zrec,refls,c=cls[i], dashes=refds,lw = reflw,label='coarse'
                     )
        if i!=0:axes[2].plot(sigf[:,7],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label='fine'
                     )
        else:axes[2].plot(sigf[:,7],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label='fine'
                     )

    elif pltstyle == 'diagdep_time':
        bound = np.loadtxt(Workdir+'bound.txt', skiprows=5)
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[1,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,15]*0.5*(sig[k+1,16]+sig[k+1,16])*(sig[k+1,17]-sig[k,17])  
        
        zrecf = np.zeros(sig[:,0].shape[0])
        zrecf[-1]=recz[0,2]
        for k in reversed(range(sigf[:,0].shape[0]-1)):
            zrecf[k] = zrecf[k+1]+sigf[k,15]*0.5*(sigf[k+1,16]+sigf[k+1,16])*(sigf[k+1,17]-sigf[k,17])  

        xp = sig[:,0]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)
        xp = sigf[:,0]
        yp = zrecf[:]
        zrecfb=np.interp(bound[:,0],xp,yp)
        
        lw = 2
        dspf = (1,1.5)
        
        axes[0].plot(sig[:,8],zrec,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        if i==0:axes[0].plot(sigf[:,5],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        else:axes[0].plot(sigf[:,5],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        axes[1].plot(sig[:,9],zrec,refls,c=cls[i], dashes=refds,lw = reflw
                 )
        if i!=0:axes[1].plot(sigf[:,6],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        else:axes[1].plot(sigf[:,6],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[2].plot((sig[:,13]-rectime[4])/1e3,zrec,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        if i!=0:axes[2].plot((sigf[:,12]-rectime[4])/1e3,zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        else:axes[2].plot((sigf[:,12]-rectime[4])/1e3,zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[3].plot(sig[:,10],zrec,refls,c=cls[i], dashes=refds,lw = reflw,label = 'coarse'
                     )
        if i!=0:axes[3].plot(sigf[:,7],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label='fine'
                     )
        else:axes[3].plot(sigf[:,7],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label='fine'
                     )

    elif pltstyle == 'time':
    
        axes[0].plot(sig[:,8],(sig[:,13]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        axes[0].plot(sigf[:,5],(sigf[:,12]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        axes[1].plot(sig[:,9],(sig[:,13]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                 )
        axes[1].plot(sigf[:,6],(sigf[:,12]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[2].plot(sig[:,10],(sig[:,13]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw,label = 'coarse'
                     )
        axes[2].plot(sigf[:,7],(sigf[:,12]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label='fine'
                     )
                     
    elif pltstyle == 'diagtime':

        axes[0].plot(sig[:,8],(sig[:,0]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        axes[0].plot(sigf[:,5],(sigf[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        axes[1].plot(sig[:,9],(sig[:,0]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                 )
        axes[1].plot(sigf[:,6],(sigf[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        axes[2].plot(sig[:,10],(sig[:,0]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw,label = 'coarse'
                     )
        axes[2].plot(sigf[:,7],(sigf[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label='fine'
                     )

def sigplot(code,ox,oxanox,labs,turbo2,nobio,filename,simname
            ,i,ax1,ax2,ax4,pltstyle):
    
    # the following part is used to specify the location of individual result data 
    # in consistent with how and where to record the results 
    Workdir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    Workdir += '/imp_output/'
    # Workdir = 'C:/cygwin64/home/YK/imp_output/'
    # Workdir = 'E:/imp_output/'
    Workdir += code+'/'
    Workdir += simname
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
    
    rectime = np.loadtxt(Workdir+'rectime.txt')
    sig = np.loadtxt(Workdir+'sigmly.txt',skiprows = 30)
    sigf = np.loadtxt(Workdir+'sigmlyd.txt',skiprows = 30)
    recz = np.loadtxt(Workdir+'recz.txt')

    print 'end input-',i

    ls = np.array([':','-','-','--'])
    dsp = [(1,3),(5,0),(5,5),[5,3,1,3]]
    cc = 'k'
    cf = 'royalblue'
    
    ls = ['-']*4
    dsp = [(5,0)]*4
    cls = ['hotpink','royalblue','limegreen','orange']
    refc = 'k'
    refls = ':'
    refds = (1,1)
    reflw = 2

    if pltstyle == 'diagdep':
        bound = np.loadtxt(Workdir+'bound.txt', skiprows=5)
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[1,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,15]*0.5*(sig[k+1,16]+sig[k+1,16])*(sig[k+1,17]-sig[k,17])  
        
        zrecf = np.zeros(sig[:,0].shape[0])
        zrecf[-1]=recz[0,2]
        for k in reversed(range(sigf[:,0].shape[0]-1)):
            zrecf[k] = zrecf[k+1]+sigf[k,15]*0.5*(sigf[k+1,16]+sigf[k+1,16])*(sigf[k+1,17]-sigf[k,17])  

        xp = sig[:,0]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)
        xp = sigf[:,0]
        yp = zrecf[:]
        zrecfb=np.interp(bound[:,0],xp,yp)
        
        lw = 2
        dspf = (1,1.5)
        
        ax1.plot(sig[:,8],zrec,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        if i==0:ax1.plot(sigf[:,5],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        else:ax1.plot(sigf[:,5],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        ax2.plot(sig[:,9],zrec,refls,c=cls[i], dashes=refds,lw = reflw
                 )
        if i!=0:ax2.plot(sigf[:,6],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        else:ax2.plot(sigf[:,6],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        ax4.plot(sig[:,10],zrec,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        if i!=0:ax4.plot(sigf[:,7],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        else:ax4.plot(sigf[:,7],zrecf,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

    elif pltstyle == 'time':
    
        ax1.plot(sig[:,8],(sig[:,13]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        ax1.plot(sigf[:,5],(sigf[:,12]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax2.plot(sig[:,9],(sig[:,13]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                 )
        ax2.plot(sigf[:,6],(sigf[:,12]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        ax4.plot(sig[:,10],(sig[:,13]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        ax4.plot(sigf[:,7],(sigf[:,12]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
    elif pltstyle == 'diagtime':

        ax1.plot(sig[:,8],(sig[:,0]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        ax1.plot(sigf[:,5],(sigf[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax2.plot(sig[:,9],(sig[:,0]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                 )
        ax2.plot(sigf[:,6],(sigf[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        
        ax4.plot(sig[:,10],(sig[:,0]-rectime[4])/1e3,refls,c=cls[i], dashes=refds,lw = reflw
                     )
        ax4.plot(sigf[:,7],(sigf[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

def main():
    if not os.getcwd() in sys.path: sys.path.append(os.getcwd())
    import plot_settings
    plot_settings.plot_settings()
    
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
    outname = 'size_reading'
    
    pltstyle = 'diagtime'   # plotting against diagnosed time  
    pltstyle = 'diagdep' # plotting against diagnosed depth without tracking model time
    pltstyle = 'time' # plotting against model time when tracked 
    
    # specigy code used, ('fortran', 'python' or 'matlab')
    # simulation name and filename 
    # in lists code, simname, and filename respectively
    # following are three sets of examples 
    # when matlab and python are used 
    
    # matlab example
    code = ['matlab']*3
    simname = ['test_reading_time_size']*3
    filename = ['cc-1.2e-05_rr-0.7_dep-3.5']*3
    
    # python example 
    # code = ['python']*3
    # simname = ['test_time_size']*3
    # filename = ['cc-1.2e-05_rr-7.0e-01_dep-3.5e+00']*3
    
    outname += '_'+pltstyle
    
    if 'fortran' in code: outname += '_fortran'
    if 'python' in code: outname += '_python'
    if 'matlab' in code: outname += '_matlab'

    fs=12
    
    dep = False
    if pltstyle=='diagdep':dep = True

    nx = 3
    ny =1
    fig = plt.figure(figsize=(7*3/4.,4)) # long
    for j in range(1):
        
        ax1 = plt.subplot2grid((ny,nx), (j,0))
        ax2 = plt.subplot2grid((ny,nx), (j,1))
        ax4 = plt.subplot2grid((ny,nx), (j,2))
        for i in range(nexp):
            sigplot(code[i],ox[i],oxanox[i]
                    ,labs[i],turbo2[i],nobio[i],filename[i],simname[i]
                    ,i,ax1,ax2,ax4,pltstyle)
        
        tx = 0.2
        ty = 1.15
        ax4.text(tx, ty
            ,'Solid: fine\nDotted: coarse'
            ,horizontalalignment='left',verticalalignment='center'
            , transform=ax4.transAxes
            # ,rotation=90
            )

        if j==0:
            ax1.legend(facecolor='None',edgecolor='None'
                ,loc='lower left'
                , bbox_to_anchor=(-0.5, 1.0)
                ,ncol=1
                )

        ax1.set_xlim(-1.3,2.3)
        if not dep:ax1.set_ylim(-40,90)
        if dep: ax1.set_ylim(30,80)
        if dep:ax1.invert_yaxis()
        ax1.set_xticks([-1,0,1,2])
        ax1.set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{13}}$C'+' ('+u'$‰$'+')')
        if dep: ax1.set_ylabel(r'$\mathregular{\it{z}_{\rm{diag}}}$'+' (cm)')
        if not dep: ax1.set_ylabel('Time (kyr)')
        ax1.yaxis.set_ticks_position('both')
        ax1.xaxis.set_ticks_position('both')
        ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
        if dep:ax1.yaxis.set_minor_locator(MultipleLocator(5))
        if not dep:ax1.yaxis.set_minor_locator(MultipleLocator(10))

        ax2.set_xlim(-1.2,1.2)
        if not dep:ax2.set_ylim(-40,90)
        if dep: ax2.set_ylim(30,80)
        if dep:ax2.invert_yaxis()
        ax2.set_xticks([-1,0,1])
        ax2.set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{18}}$O'+' ('+u'$‰$'+')')
        ax2.set_yticklabels([])
        ax2.yaxis.set_ticks_position('both')
        ax2.xaxis.set_ticks_position('both')
        ax2.xaxis.set_minor_locator(MultipleLocator(0.5))
        if dep:ax2.yaxis.set_minor_locator(MultipleLocator(5))
        if not dep:ax2.yaxis.set_minor_locator(MultipleLocator(10))

        ax4.set_xlim(-5,100)
        if not dep:ax4.set_ylim(-40,90)
        if dep: ax4.set_ylim(30,80)
        if dep:ax4.invert_yaxis()
        ax4.set_xticks([0,50,100])
        ax4.set_xlabel('CaCO'+r'$\mathregular{_{3}}$'+' wt%')
        ax4.set_yticklabels([])
        ax4.yaxis.set_ticks_position('both')
        ax4.xaxis.set_ticks_position('both')
        ax4.xaxis.set_minor_locator(MultipleLocator(25))
        if dep:ax4.yaxis.set_minor_locator(MultipleLocator(5))
        if not dep:ax4.yaxis.set_minor_locator(MultipleLocator(10))

    #fig.tight_layout()
    fig.subplots_adjust(left=0.15,bottom=0.2,wspace=0.06,hspace=0.06,top=0.7)
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
