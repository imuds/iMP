# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import sys,os
if not os.getcwd() in sys.path: sys.path.append(os.getcwd())

"""
caco3 signal profiles 
"""

ox = False
oxanox = False
labs = False
turbo2 = False
nobio = False
size = False
isotrack = False

str_tmp = raw_input("What code did you use [1--fortran, 2--python, 3--matlab]?: \t")
if str_tmp == '1': code = 'fortran'
elif str_tmp == '2': code = 'python'
elif str_tmp == '3': code = 'matlab'
else: exit()
str_tmp = raw_input("What mode of OM degrdation [1--oxonly, 2--oxanox]?: \t")
if str_tmp == '1': ox = True
elif str_tmp == '2': oxanox = True
else: exit()
str_tmp = raw_input("What mode of bioturbation [1--fickian, 2--nobio, 3--turbo2, 4--labs]?: \t")
if str_tmp == '1': pass
elif str_tmp == '2': nobio = True
elif str_tmp == '3': turbo2 = True
elif str_tmp == '4': labs = True
else: exit()

folder = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
folder += '/imp_output/'
folder += code+'/'
simlist = os.listdir(folder)
intlist = [int(i+1) for i in range(len(simlist))]
simlist_show = [str(intlist[i])+'--'+simlist[i] for i in range(len(simlist))]
simlist_show_2=', '.join(simlist_show)
str_tmp = raw_input("What is your simulation ["+simlist_show_2+"]?: \t")
for i in intlist:
    if eval(str_tmp)== i: 
        simname = simlist[i-1]
        break
folder += simname+'/profiles/'
if labs:
    if oxanox:folder += 'oxanox_labs/'
    else:folder += 'ox_labs/'
    label = 'LABS mixing'
elif nobio:
    if oxanox:folder += 'oxanox_nobio/'
    else:folder += 'ox_nobio/'
    label = 'No bioturbation'
elif turbo2:
    if oxanox:folder += 'oxanox_turbo2/'
    else:folder += 'ox_turbo2/'
    label='Homogeneous mixing'
else: 
    if oxanox:folder += 'oxanox/'
    else: folder += 'ox/'
    label ='Fickian mixing'

filelist = os.listdir(folder)
intlist = [int(i+1) for i in range(len(filelist))]
filelist_show = [str(intlist[i])+'--'+filelist[i] for i in range(len(filelist))]
filelist_show_2=', '.join(filelist_show)
str_tmp = raw_input("What is your file ["+filelist_show_2+"]?: \t")
for i in intlist:
    if eval(str_tmp)== i: 
        filename = filelist[i-1]
        break
folder += filename
folder += '/'

str_tmp = raw_input("Did you track size or 14Cage+capD47 in addition to d13C and d18O [1--no, 2--yes]?: \t")
if str_tmp =='2':
    str_tmp2 = raw_input("Which [1--size, 2--14Cage+capD47]?: \t")
    if str_tmp2=='1': size = True
    if str_tmp2=='2': isotrack = True

str_tmp = raw_input("Against what should signals be plotted [1--diagdep, 2--diagdep_time, 3--time, 4--diagtime]?: \n"
    # +"\tdiagdep:\t plotting against diagnosed depth without tracking model time\n"
    # +"\tdiagdep_time:\t plotting against diagnosed depth with tracking model time as a proxy\n"
    # +"\ttime:\t plotting against model time when tracked\n"
    # +"\tdiagtime:\t plotting against diagnosed time\n"
    )
if str_tmp == '1': pltstyle = 'diagdep' # plotting against diagnosed depth without tracking model time
if str_tmp == '2': pltstyle = 'diagdep_time'
if str_tmp == '3': pltstyle = 'time'
if str_tmp == '4': pltstyle = 'diagtime'


    
if isotrack:
    
    nx = 3
    figsize = (8*3/4.,4)
    tx = 3.3
    ty = 0.5
    ny =2

    fig = plt.figure(figsize=figsize) # long
    if pltstyle=='diagdep_time': 
        ntot = nx*ny
    else: 
        ntot = nx*ny-1
    axes = [plt.subplot2grid((ny,nx), ((i-i%nx)/nx,i%nx)) for i in range(ntot)] 

    i = 0
    import caco3_signals_isotrack
    caco3_signals_isotrack.sigplot_wokie(code,ox,oxanox,labs,turbo2,nobio,simname,filename,i,axes,pltstyle)

    axes[0].set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{13}}$C'+' ('+u'$‰$'+')')
    axes[1].set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{18}}$O'+' ('+u'$‰$'+')')
    axes[2].set_xlabel('CaCO'+r'$\mathregular{_{3}}$'+' wt%')
    axes[3].set_xlabel(r'$\mathregular{^{14}}$'+'C age (kyr)')
    axes[4].set_xlabel(r'$\mathregular{\Delta}$$\mathregular{_{47}}$'+' ('+u'$‰$'+')')
    if pltstyle=='diagdep_time':axes[5].set_xlabel('Time (kyr)')
    for i in range(ntot):
        if i==0 or i == nx: 
            if pltstyle == 'diagdep' or pltstyle == 'diagdep_time':
                axes[i].set_ylabel(r'$\mathregular{\it{z}_{\rm{diag}}}$'+' (cm)')
            else:
                axes[i].set_ylabel('Time (kyr)')
        if pltstyle == 'diagdep' or pltstyle == 'diagdep_time':
            axes[i].invert_yaxis()
            
else:
    if pltstyle=='time' or pltstyle =='diagdep' or pltstyle == 'diagtime':
        nx = 3
        figsize = (8*3/4.,3.5)
        tx = 3.3
        ty = 0.5
    else :
        nx = 4
        figsize = (8,3.5)
        tx = 4.4
        ty = 0.5
    ny =1

    fig = plt.figure(figsize=figsize) # long
    axes = [plt.subplot2grid((ny,nx), (0,i)) for i in range(nx)] 

    i = 0
    if size: 
        import caco3_signals_size
        caco3_signals_size.sigplot_ex(code,ox,oxanox,labs,turbo2,nobio,filename,simname,i,axes,pltstyle)
        plt.legend()
    else: 
        import caco3_signals_biotest
        caco3_signals_biotest.sigplot(code,ox,oxanox,labs,turbo2,nobio,simname,filename,i,axes,pltstyle)

    axes[0].set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{13}}$C'+' ('+u'$‰$'+')')
    axes[1].set_xlabel(r'$\mathregular{\delta}$$\mathregular{^{18}}$O'+' ('+u'$‰$'+')')
    axes[nx-1].set_xlabel('CaCO'+r'$\mathregular{_{3}}$'+' wt%')
    if nx==4:axes[2].set_xlabel('Time (kyr)')
    for i in range(nx):
        if i==0: 
            if pltstyle == 'diagdep' or pltstyle == 'diagdep_time':
                axes[i].set_ylabel(r'$\mathregular{\it{z}_{\rm{diag}}}$'+' (cm)')
            else:
                axes[i].set_ylabel('Time (kyr)')
        if pltstyle == 'diagdep' or pltstyle == 'diagdep_time':
            axes[i].invert_yaxis()
            
fig.tight_layout()
    
plt.savefig(folder+'imp_signals_'+pltstyle+'.svg', transparent=True)
plt.savefig(folder+'imp_signals_'+pltstyle+'.pdf', transparent=True)
    
plt.show()
plt.clf()
plt.close()
