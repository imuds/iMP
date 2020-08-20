# -*- coding: utf-8 -*-
import numpy as np
import subprocess
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib import mathtext
mathtext.FontConstantsBase = mathtext.ComputerModernFontConstants

"""
caco3 signal profiles including clumped isotopes
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

def sigplot(code,code_kie,ox,oxanox,labs,turbo2,nobio,simname
            ,filename,i,ax1,ax2,ax3,ax4,ax5,ax6
            ,simname_kie,filename_kie
            ,pltstyle
            ):
    
    # the following part is used to specify the location of individual result data 
    # in consistent with how and where to record the results 
    Workdir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    Workdir += '/imp_output/'
    # Workdir = 'C:/cygwin64/home/YK/imp_output/'
    Workdir += code+'/'+simname+'/'
    Workdir += 'profiles/'
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
    
    Workdir += filename
    Workdir += '/'

    Workdir_kie = 'C:/cygwin64/home/YK/imp_output/'
    Workdir_kie += code_kie+'/'+simname_kie+'/'
    Workdir_kie += 'profiles/'
    if labs:
        if oxanox:Workdir_kie += 'oxanox_labs/'
        else:Workdir_kie += 'ox_labs/'
    elif nobio:
        if oxanox:Workdir_kie += 'oxanox_nobio/'
        else:Workdir_kie += 'ox_nobio/'
        label = 'No bioturbation'
    elif turbo2:
        if oxanox:Workdir_kie += 'oxanox_turbo2/'
        else:Workdir_kie += 'ox_turbo2/'
        label='Homogeneous mixing'
    else: 
        if oxanox:Workdir_kie += 'oxanox/'
        else: Workdir_kie += 'ox/'
        label ='Fickian mixing'
    
    Workdir_kie += filename_kie
    Workdir_kie += '/'
    
    rectime = np.loadtxt(Workdir+'rectime.txt')
    sig = np.loadtxt(Workdir+'sigmly.txt',skiprows=40)
    bound = np.loadtxt(Workdir+'bound.txt')
    
    rectime_kie = np.loadtxt(Workdir_kie+'rectime.txt')
    sig_kie = np.loadtxt(Workdir_kie+'sigmly.txt',skiprows=40)
    bound_kie = np.loadtxt(Workdir_kie+'bound.txt')
    recz = np.loadtxt(Workdir+'recz.txt')

    print 'end input-',i

    ckie = 'g'


    ls = np.array([':','--','-'])
    dsp = [(1,2),(5,2),[5,2,1,2]]
    
    ls = ['-']*4
    dsp = [(5,0)]*4
    # cls = ['b','r','g','m']
    cls = ['hotpink','royalblue','limegreen','orange']
    refc = 'k'
    refls = ':'
    refds = (1,1)
    reflw = 2
    

    if pltstyle== 'diagdep':
        zrec = np.zeros(sig[:,0].shape[0])
        zrec[-1]=recz[0,2]
        for k in reversed(range(sig[:,0].shape[0]-1)):
            zrec[k] = zrec[k+1]+sig[k,9]*0.5*(sig[k+1,10]+sig[k+1,10])*(sig[k+1,11]-sig[k,11]) 

        xp = sig[:,0]
        yp = zrec[:]
        zrecb=np.interp(bound[:,0],xp,yp)

        ax1.plot(sig[:,1],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )

        ax2.plot(sig[:,2],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        ax3.plot(sig[:,3],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax4.plot(sig[:,5]/1e3,zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax5.plot(sig[:,6],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax6.plot(sig[:,6],zrec,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        ax6.plot(sig_kie[:,6],zrec
                 ,refls,c=cls[i], dashes=refds,lw = reflw
                 ,label=label
                     )
    elif pltstyle == 'time':

        ax1.plot(sig[:,1],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax1.plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,refls,c=refc, dashes=refds,lw = reflw
                         ,label='Input'
                     )

        ax2.plot(sig[:,2],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax2.plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,refls,c=refc, dashes=refds,lw = reflw
                         ,label='Input'
                     )
        ax3.plot(sig[:,3],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax4.plot(sig[:,5]/1e3,(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax5.plot(sig[:,6],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax5.plot(bound[:,3],(bound[:,0]-rectime[4])/1e3,refls,c=refc, dashes=refds,lw = reflw
                         ,label='Input'
                     )
                     
        ax6.plot(sig[:,6],(sig[:,7]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        ax6.plot(sig_kie[:,6],(sig_kie[:,7]-rectime_kie[4])/1e3
                 ,refls,c=cls[i], dashes=refds,lw = reflw
                 ,label=label
                     )
        if i==0:ax6.plot(bound[:,3],(bound[:,0]-rectime[4])/1e3,refls,c=refc, dashes=refds,lw = reflw
                         ,label='Input'
                     )

    elif pltstyle == 'diagtime':

        ax1.plot(sig[:,1],(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax1.plot(bound[:,1],(bound[:,0]-rectime[4])/1e3,refls,c=refc, dashes=refds,lw = reflw
                         ,label='Input'
                     )

        ax2.plot(sig[:,2],(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax2.plot(bound[:,2],(bound[:,0]-rectime[4])/1e3,refls,c=refc, dashes=refds,lw = reflw
                         ,label='Input'
                     )
        ax3.plot(sig[:,3],(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax4.plot(sig[:,5]/1e3,(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
                     
        ax5.plot(sig[:,6],(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        if i==0:ax5.plot(bound[:,3],(bound[:,0]-rectime[4])/1e3,refls,c=refc, dashes=refds,lw = reflw
                         ,label='Input'
                     )
                     
        ax6.plot(sig[:,6],(sig[:,0]-rectime[4])/1e3,ls[i],c=cls[i], dashes=dsp[i]
                 ,label=label
                     )
        ax6.plot(sig_kie[:,6],(sig_kie[:,0]-rectime_kie[4])/1e3
                 ,refls,c=cls[i], dashes=refds,lw = reflw
                 ,label=label
                     )
        if i==0:ax6.plot(bound[:,3],(bound[:,0]-rectime[4])/1e3,refls,c=refc, dashes=refds,lw = reflw
                         ,label='Input'
                     )

def main():
    nexp = 3  # Here you can specify the number of plot, 1 to 3 

    ox = np.zeros(nexp,dtype=bool)
    oxanox = np.zeros(nexp,dtype=bool)
    labs = np.zeros(nexp,dtype=bool)
    turbo2 = np.zeros(nexp,dtype=bool)
    nobio = np.zeros(nexp,dtype=bool)
        
    # specigy code used, ('fortran', 'python' or 'matlab')
    # simulation name and filename 
    # in lists code, simname, and filename respectively
    # in this plotting script, you also need simulation results with enabling kie
    # so two sets of experimental info are needed
    # following are three sets of examples 
    # when fortran, matlab and python are used 
    
    # fortran example 
    code = ['fortran']*nexp
    code_kie = ['fortran']*nexp
    simname=[
        'chk_iso_org'
        ]*nexp
    simname_kie=[
        'chk_iso_kie_org'
        ]*nexp
    filename=[
        'cc-0.12E-4_rr-0.70E+0_dep-0.50E+1'
        ]*nexp
    filename_kie=[
        'cc-0.12E-4_rr-0.70E+0_dep-0.50E+1'
        ]*nexp
    
    # matlab example
    code = ['matlab']*nexp
    code_kie = ['matlab']*nexp
    simname=[
        'test_reading_time_iso'
        ]*nexp
    simname_kie=[
        'test_reading_time_iso_kie'
        ]*nexp
    filename=[
        'cc-1.2e-05_rr-0.7_dep-3.5'
        ]*nexp
    filename_kie=[
        'cc-1.2e-05_rr-0.7_dep-3.5'
        ]*nexp
    
    # python example 
    # code = ['python']*nexp
    # code_kie = ['python']*nexp
    # simname=[
        # 'test_time_iso'
        # ]*nexp
    # simname_kie=[
        # 'test_time_iso_kie'
        # ]*nexp
    # filename=[
        # 'cc-1.2e-05_rr-7.0e-01_dep-5.0e+00'
        # ]*nexp
    # filename_kie=[
        # 'cc-1.2e-05_rr-7.0e-01_dep-5.0e+00'
        # ]*nexp
    
    
    # plot styke is chosen here 
    # pltstyle = 'diagtime'  # plotting against diagnosed time  
    pltstyle = 'diagdep' # plotting against diagnosed depth without tracking model time
    # pltstyle = 'time' # plotting against model time when tracked 

    ox[:]=True
    oxanox[:]=True
    if nexp>1:nobio[0]=True
    if nexp>2:turbo2[2]=True
        
        
    # name below are used for figure
    outname = 'reading_iso_kie'
    
    outname += '_'+pltstyle
    
    if 'fortran' in code: outname += '_fortran'
    if 'python' in code: outname += '_python'
    if 'matlab' in code: outname += '_matlab'
    
    if 'fortran' in code_kie: outname += '_fortran'
    if 'python' in code_kie: outname += '_python'
    if 'matlab' in code_kie: outname += '_matlab'

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
        sigplot(code[i],code_kie[i],ox[i],oxanox[i]
                ,labs[i],turbo2[i],nobio[i],simname[i],filename[i]
                ,i,ax1,ax2,ax3,ax4,ax5,ax6
                ,simname_kie[i]
                ,filename_kie[i]
                ,pltstyle
                )

    ax1.set_xlim(-1.3,2.3)
    if pltstyle=='diagdep':
        ax1.set_ylim(30,60)
        ax1.invert_yaxis()
        ax1.set_ylabel(r'$\mathregular{\it{z}_{\rm{diag}}}$'+' (cm)')
    else:
        ax1.set_ylim(-40,90)
        ax1.set_ylabel('Time (kyr)')
    ax1.set_xticks([-1,0,1,2])
    ax1.set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{13}}$C'+' ('+u'$‰$'+')')
    ax1.yaxis.set_ticks_position('both')
    ax1.xaxis.set_ticks_position('both')
    ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax1.yaxis.set_minor_locator(MultipleLocator(10))

    ax2.set_xlim(-1.2,1.2)
    if pltstyle=='diagdep':
        ax2.set_ylim(30,60)
        ax2.invert_yaxis()
    else: ax2.set_ylim(-40,90)
    ax2.set_xticks([-1,0,1])
    ax2.set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{18}}$O'+' ('+u'$‰$'+')')
    ax2.set_yticklabels([])
    ax2.yaxis.set_ticks_position('both')
    ax2.xaxis.set_ticks_position('both')
    ax2.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax2.yaxis.set_minor_locator(MultipleLocator(10))

    ax3.set_xlim(-5,100)
    if pltstyle=='diagdep':
        ax3.set_ylim(30,60)
        ax3.invert_yaxis()
    else: ax3.set_ylim(-40,90)
    ax3.set_xticks([0,50,100])
    ax3.set_xlabel('CaCO'+r'$\mathregular{_{3}}$'+' wt%')
    ax3.set_yticklabels([])
    ax3.yaxis.set_ticks_position('both')
    ax3.xaxis.set_ticks_position('both')
    ax3.xaxis.set_minor_locator(MultipleLocator(25))
    ax3.yaxis.set_minor_locator(MultipleLocator(10))

    ax4.set_xlim(-3,60)
    if pltstyle=='diagdep':
        ax4.set_ylim(30,60)
        ax4.invert_yaxis()
        ax4.set_ylabel(r'$\mathregular{\it{z}_{\rm{diag}}}$'+' (cm)')
    else: 
        ax4.set_ylim(-40,90)
        ax4.set_ylabel('Time (kyr)')
    ax4.set_xticks([0,50])
    ax4.set_xlabel(r'$\mathregular{^{14}}$'+'C age (kyr)%')
    ax4.yaxis.set_ticks_position('both')
    ax4.xaxis.set_ticks_position('both')
    ax4.xaxis.set_minor_locator(MultipleLocator(10))
    ax4.yaxis.set_minor_locator(MultipleLocator(10))

    ax5.set_xlim(0.49,0.61)
    if pltstyle=='diagdep':
        ax5.set_ylim(30,60)
        ax5.invert_yaxis()
    else: ax5.set_ylim(-40,90)
    ax5.set_xticks([0.5,0.6])
    ax5.set_xlabel(r'$\mathregular{\Delta}$$\mathregular{_{47}}$'+' ('+u'$‰$'+')')
    ax5.set_yticklabels([])
    ax5.yaxis.set_ticks_position('both')
    ax5.xaxis.set_ticks_position('both')
    ax5.xaxis.set_minor_locator(MultipleLocator(0.025))
    ax5.yaxis.set_minor_locator(MultipleLocator(10))

    ax6.set_xlim(0.4,1.1)
    if pltstyle=='diagdep':
        ax6.set_ylim(30,60)
        ax6.invert_yaxis()
    else: ax6.set_ylim(-40,90)
    ax6.set_xticks([0.5,1.0])
    ax6.set_xlabel(r'$\mathregular{\Delta}$$\mathregular{_{47}}$'+' ('+u'$‰$'+')')
    ax6.set_yticklabels([])
    ax6.yaxis.set_ticks_position('both')
    ax6.xaxis.set_ticks_position('both')
    ax6.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax6.yaxis.set_minor_locator(MultipleLocator(10))
    
    
    tx = 0.35
    ty = 0.73
    
    ax6.text(tx, ty
         ,'Dotted: KIE\n('+r'$\mathregular{-5\times10^{-5}}$'+')'
         ,horizontalalignment='left',verticalalignment='center'\
         , transform=ax6.transAxes
         ,rotation=0
         )

    ax1.legend(facecolor='None',edgecolor='None'
        ,loc='center left'
        , bbox_to_anchor=(-0.1, 1.15)
        ,ncol=2
        ,handlelength=1.7
        ,handletextpad = 0.2
        )
        
    fig.subplots_adjust(left=0.15,bottom=0.1,wspace=0.06,hspace=0.3,right = 0.95)
    # You can specify the directory where output is made 
    Workdir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    Workdir += '/imp_output/'
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
