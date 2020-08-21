# -*- coding: utf-8 -*-
import numpy as np
import os 
"""
attempt to create input file for imp: ver.2
"""
# use default input?
# if yes, choose simulation mode
# if dissolution is induced, a depth value is asked to which water depth is changed during event
# if no, ask about backgraound value
# and then the specified values
# finally plot time evolutions 

#--- List of input parameters
str_tmp = raw_input('Use default backgroud values for input parameters [y/n] ?:\t')
if str_tmp == 'y': default_ref = True
else: default_ref = False
str_tmp = raw_input('Use default temporal changes of input parameter values [y/n] ?:\t')
if str_tmp == 'y': 
    default_event = True
    simmode = raw_input('What kind of simulation ["biot", "diss", "size" or "iso"] ?: \t')
else: default_event = False
str_tmp = raw_input('Plot temporal changes of input parameter values [y/n] ?:\t')
if str_tmp == 'y': plt_timeline = True
else: plt_timeline = False

par_names = [
    'time'                  # time in yr 
    ,'temp'                 # temperature in Celcius 
    ,'sal'                  # salinity g/kg 
    ,'dep'                  # water depth in km 
    ,'dic'                  # DIC in uM
    ,'alk'                  # ALK in ueqM
    ,'o2'                   # O2 in uM
    ,'ccflx'                # CaCO3 rain flux in mol cm-2 yr-1
    ,'omflx'                # OM rain flux in mol cm-2 yr-1
    ,'detflx'               # Detrial rain flux in g cm-2 yr-1
    ,'flxfin'               # fraction of fine species (0-1; used only when two size species are simulated)
    ,'aomflx'               # AOM flux in mol cm-2 yr-1
    ,'zsr'                  # sulfate reduction depth in m
    ,'d13c'                 # delta-13C in ocean (you name different proxy if you want)
    ,'d18o'                 # delta-18O in ocean  (you name different proxy if you want)
    ,'capd47'               # Cap-Delta 47 in ocean (used only simulating clumped isotopes)
    ,'14cage'               # Radiocarbon (14C) age in ocean in year (used only simulating clumped isotopes)
    ,'dt'                   # time step in yr 
    ]
n_par = len(par_names)
#--- time step in yr
dt = 10.
#--- start and end time of simulation 
time_start = 0.
if default_event:
    if simmode == 'biot': 
        time_end = 100e3   # choose for biot exp 
        event_start = 40e3
        event_end = 45e3
    else : 
        time_end = 200e3   # choose for diss exp 
        event_start = 40e3
        event_end = 90e3
else:
    # default values
    time_end = 100e3   
    event_start = 40e3
    event_end = 45e3
    print 
    print '+++ simulation and event duration +++' 
    print 'Default time of end of simulation, start of event and end of event are respecitvely:\n','{:.2e} {:.2e} {:.2e}'.format(time_end, event_start, event_end)
    print '+++++++++++++++++++++++++++++++++++++'
    strlist = raw_input(
        'Enter the above three time values in single line \n'
        + '(e.g., enter "200e3 50e3 100e3"):\n\t'
        )  
    time_values = [np.float64(i) for i in strlist.split()]
    time_end, event_start, event_end = time_values
    print 
    
    
n_step = int((time_end-time_start)/dt) + 1

inputdata = np.zeros((n_step,n_par),dtype=np.float)
inputdata[:,par_names.index('time')]=np.linspace(time_start,time_end,n_step)
#--- Base parameter values which are used unless specified (see below)
val_ref = [
    0.
    ,2.
    ,35.
    ,3.5
    ,2211.
    ,2285.
    ,165.  #O2
    ,12e-6  
    ,12e-6*0.7  #OM
    ,12e-6*1./9.*100.  # detrital 
    ,0.5  # fraction fine
    ,0.0  # AOM 
    ,10.   # bottom of SRZ 
    ,0.    
    ,0.   
    ,0.   
    ,0.   
    ,dt
    ]
if not default_ref:
    print '=== background parameter values  ===' 
    print 'parameters you can change:\n'+' '.join(par_names)
    print 
    print 'the reference backgound values of the above parameters are :\n', val_ref
    print '===================================='
    strlist = raw_input(
        'Enter parameters which you want to change from the reference background values during events \n'
        + 'choose from the above paramter list and put in single line (e.g.,  enter "d13c d18o capd47";\n'
        + 'if you press enter without any input default values are assumed):\n\t'
        )  
    for par_name in strlist.split():
        print 
        par_ref_tmp = raw_input( 
            'Specify '+par_name+' background value '
            + '(e.g., enter "1.5"):\t'
            )
        val_ref[par_names.index(par_name)] = np.float64(par_ref_tmp)
par_values_base = val_ref
#--- specify parameter values when they are changed with time
#      Ex) if you want a given parameter to pass points 1 at year 5 and 4 at year 10, 
#      put a set of parameter-value and time lists [5,10],[1,4] 
event_list = [
    [[time_start,time_end],[par_values_base[i],par_values_base[i]]] for i in range(n_par)
    ]
if default_event:
    if simmode == 'biot':
        event_list[par_names.index('d13c')] = [[time_start,event_start,event_end,time_end],[2.,2.,-1.,-1.]]
        event_list[par_names.index('d18o')] = [[time_start,event_start,0.5*(event_start+event_end),event_end,time_end],[1.,1.,-1.,1.,1.]]
    else:
        event_list[par_names.index('d13c')] = [[time_start,40e3,45e3,85e3,90e3,time_end],[2.,2.,-1.,-1.,2.,2.]] 
        event_list[par_names.index('d18o')] = [[time_start,event_start,0.5*(event_start+event_end),event_end,time_end],[1.,1.,-1.,1.,1.]]
        event_list[par_names.index('capd47')] = [[time_start,event_start,0.5*(event_start+event_end),event_end,time_end],[0.6,0.6,0.5,0.6,0.6]]
        if simmode == 'size':
            event_list[par_names.index('flxfin')] = [[time_start,event_start,0.5*(event_start+event_end),event_end,time_end],[0.5,0.5,0.1,0.5,0.5]]
else: 
    print '--- parameter values during event ---' 
    print 'parameters you can change:\n'+' '.join(par_names)
    print '-------------------------------------'
    strlist = raw_input(
        'Enter parameters which you want to change from the background values during events \n'
        + 'choose from the above paramter list and put in single line (e.g.,  enter "d13c d18o capd47";\n'
        + 'if you press enter without any input parameter values are not changed from their default values):\n\t'
        )  
    for par_name in strlist.split():
        end_input = False
        time_list = []
        value_list = []
        print 
        while not end_input:
            par_event_tmp = raw_input( 
                'Specify time and '+par_name+' values'
                + '(e.g., enter "1e3 1.5"):\n\t'
                )
            time_list.append(np.float64(par_event_tmp.split()[0]))
            value_list.append(np.float64(par_event_tmp.split()[1]))
            end_tmp = raw_input( 
                'End to specify '+par_name +' [y/n]?: '
                )
            if end_tmp =='y': end_input = True
        event_list[par_names.index(par_name)] = [time_list, value_list]

par_values_spec = event_list

for par_name in par_names:
    par_index = par_names.index(par_name)
    time_index = par_names.index('time')
    if par_name == 'time':continue 
    if len(par_values_spec[par_index])==0:
        inputdata[:,par_index]=par_values_base[par_index]
    else:
        inputdata[:,par_index]=np.interp(inputdata[:,time_index],par_values_spec[par_index][0],par_values_spec[par_index][1]) 

saveplace = os.path.dirname(os.path.abspath(__file__))
filename = 'imp_input.in'
np.savetxt(saveplace+'/'+filename,inputdata)

#--- Specify recording time 
n_rec = 15
rectime = np.zeros(n_rec)
rectime[:5]= np.linspace(dt,event_start,5)
rectime[5:10]=np.linspace(event_start+dt,event_end,5)  # choose for diss. exp.
rectime[10:15]=np.linspace(event_end+dt,time_end,5)  # choos for diss exp. 
# rectime[5:10]=np.linspace(40e3+dt,45e3,5)  # choose for biot exp
# rectime[10:15]=np.linspace(45e3+dt,100e3,5)  # choose for biot exp


filename = 'rectime.in'
np.savetxt(saveplace+'/'+filename,rectime)

if plt_timeline:
    import matplotlib.pyplot as plt
    
    figsize = (10,5)
    fig = plt.figure(figsize=figsize)
    
    nx =3 
    ny =6 
    
    axes = [[plt.subplot2grid((ny,nx), (j,i)) for i in range(nx)] for j in range(ny)]
    
    for cnt in range(n_par):
        i = cnt%nx
        j = (cnt-i)/nx
        
        axes[j][i].plot(inputdata[:,0], inputdata[:,cnt])
        axes[j][i].set_ylabel(par_names[cnt])
        if j==ny-1:axes[j][i].set_xlabel(par_names[0]+' (yr)')
        axes[j][i].axvline(x=event_start,ls=':',c='0.6')
        axes[j][i].axvline(x=event_end,ls=':',c='0.6')
        
    fig.tight_layout()
    
    plt.savefig('imp_input.svg', transparent=True)
    plt.savefig('imp_input.pdf', transparent=True)
        
    plt.show()
    plt.clf()
    plt.close()
    
