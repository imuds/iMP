# -*- coding: utf-8 -*-
import numpy as np
import os 
"""
attempt to create input file for imp: ver.2
"""
#--- List of input parameters
par_names = [
    'time'                  # time in yr 
    ,'temp'                 # temperature in Celcius 
    ,'sal'                  # salinity g/kg 
    ,'dep'                  # water depth in km 
    ,'dic'                  # DIC in uM
    ,'alk'                  # ALK in ueqM
    ,'o2'                   # O2 in uM
    ,'ccflx'                # CaCO3 rain flux in umol cm-2 yr-1
    ,'omflx'                # OM rain flux in umol cm-2 yr-1
    ,'detflx'               # Detrial rain flux in ug cm-2 yr-1
    ,'flxfin'               # fraction of fine species (0-1; used only when two size species are simulated)
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
# time_end = 100e3 
time_end = 200e3 
n_step = int((time_end-time_start)/dt) + 1

inputdata = np.zeros((n_step,n_par),dtype=np.float)
inputdata[:,par_names.index('time')]=np.linspace(time_start,time_end,n_step)
#--- Base parameter values which are used unless specified (see below)
par_values_base = [
    0.
    ,2.
    ,35.
    ,3.5
    ,2211.
    ,2285.
    ,165.
    ,12e-6
    ,12e-6*0.7
    ,12e-6*1./9.*100.
    ,0.5
    ,0.  
    ,0.   
    ,0.   
    ,0.   
    ,dt
    ]
#--- specify parameter values when they are changed with time
#      Ex) if you want a given parameter to pass points 1 at year 5 and 4 at year 10, 
#      put a set of parameter-value and time lists [5,10],[1,4] 
par_values_spec = [
    []   # time
    ,[]  # temp
    ,[]  # sal
    # ,[[time_start,40e3,45e3,85e3,90e3,time_end],[3.5,3.5,4.5,4.5,3.5,3.5]]  #dep 
    # ,[[time_start,40e3,45e3,85e3,90e3,time_end],[3.5,3.5,5.0,5.0,3.5,3.5]]  #dep 
    ,[[time_start,time_end],[3.5,3.5]]  #dep 
    # ,[[time_start,time_end],[4.5,4.5]]  #dep 
    # ,[[time_start,time_end],[5.0,5.0]]  #dep 
    ,[]  # dic
    ,[]  # alk
    ,[]  # o2
    ,[]  # ccflx
    ,[]  # omflx 
    ,[]  # detflx
    # ,[[time_start,40e3,65e3,90e3,time_end],[0.5,0.5,0.1,0.5,0.5]]  # flxfin
    ,[]  # flxfin
    ,[[time_start,40e3,45e3,85e3,90e3,time_end],[2.,2.,-1.,-1.,2.,2.]]  # d13c
    # ,[[time_start,40e3,45e3,time_end],[2.,2.,-1.,-1.]]  # d13c
    ,[[time_start,40e3,65e3,90e3,time_end],[1.,1.,-1.,1.,1.]]  # d18o
    # ,[[time_start,40e3,42.5e3,45e3,time_end],[1.,1.,-1.,1.,1.]]  # d18o
    ,[[time_start,40e3,65e3,90e3,time_end],[0.6,0.6,0.5,0.6,0.6]]  # capd47
    # ,[]  # capd47
    # ,[]  # 14cage
    ,[[time_start,time_end],[1e3,1e3]]  #14cage
    # ,[[time_start,40e3,45e3,85e3,90e3,time_end],[10e3,10e3,5e3,5e3,10e3,10e3]]  # 14cage
    ,[]  # dt
    ]

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
rectime[:5]= np.linspace(dt,40e3,5)
rectime[5:10]=np.linspace(40e3+dt,90e3,5)
# rectime[5:10]=np.linspace(40e3+dt,45e3,5)
rectime[10:15]=np.linspace(90e3+dt,200e3,5)
# rectime[10:15]=np.linspace(45e3+dt,100e3,5)


filename = 'rectime.in'
np.savetxt(saveplace+'/'+filename,rectime)
