# -*- coding: utf-8 -*-
import numpy as np
import subprocess
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

"""
caco3 profiles - simple ver.  
"""
# Workdir = "C:/cygwin64/home/YK/caco3/"  # where result files exist; figures are stored in the same file out of my laziness 
Workdir = "/home/domhu/Documents/GitHub/caco3/MATLAB/2106_changedt_high_rr_ccflx54/"  # where result files exist; figures are stored in the same file out of my laziness 

nt = 2  # total number of time iteration to be plotted
nz = 100 # grid number 
nsp = 1  # caco3 species number 
dt = 1000.  # time step [yr]

numstr = np.empty((nt),dtype='|S5')

for i in range(nt):
    numstr[i] = '{:03d}'.format(i+1)

pt = np.empty((nt,nz,6),dtype=np.float)  # clay data 
cc = np.empty((nt,nz,8),dtype=np.float)  # caco3 system data 

om = np.empty((nt,nz,3),dtype=np.float)  # om 
o2 = np.empty((nt,nz,5),dtype=np.float)  # o2

ccsp = np.empty((nt,nz,nsp+2),dtype=np.float)  # individual caco3 species 
sig = np.empty((nt,nz,4),dtype=np.float)  # proxy signal data (not used)


for i in range(nt):
    pt[i,:,:]=np.loadtxt(Workdir+'matlab_ptx-'+numstr[i]+".txt")
    cc[i,:,:]=np.loadtxt(Workdir+'matlab_ccx-'+numstr[i]+".txt")
    om[i,:,:]=np.loadtxt(Workdir+'matlab_omx-'+numstr[i]+".txt")
    o2[i,:,:]=np.loadtxt(Workdir+'matlab_o2x-'+numstr[i]+".txt")
    ccsp[i,:,:]=np.loadtxt(Workdir+'matlab_ccx_sp-'+numstr[i]+".txt")
    sig[i,:,:]=np.loadtxt(Workdir+'matlab_sig-'+numstr[i]+".txt")

print('end input')  # finished reading 

# plotting format 
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

# plt.rcParams['axes.labelpad'] = 8

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'

plt.tick_params(top=True)
plt.tick_params(right=True)


fs=12 # fontsize 

nx = 3  # column number of plot 
ny =5  # row number of plot 

tx = 0.5  # parameter for location of text within plot 
ty = 0.8  # the same as above 

color=cm.jet(np.linspace(0,1,nt))  # color according to time 
label = np.empty((nt),dtype='|S15')  # making labels according to time 
for i in range(nt):
    label[i]=str(i*dt/1e3)+' kyr'

##"""
##fig = plt.figure(figsize=(14,20)) # long
fig = plt.figure(figsize=(20,14)) #wide

ax1 = plt.subplot2grid((ny,nx), (0,0))


for i in range(nt):
    ax1.plot(pt[i,:,3],pt[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
          ,'(a) '+r"$\mathregular{\rho}$" \
         +' (g cm'+ r"$\mathregular{^{-3}}$"+')'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.set_ylabel ('depth (cm)')
ax1.invert_yaxis()
ax1.set_yscale('log')
# ax1.set_xlim(2.45,2.70)

ax1 = plt.subplot2grid((ny,nx), (3,2))

for i in range(nt):
    ax1.plot(pt[i,:,3],pt[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
# ax1.legend(facecolor='None',edgecolor='None',fontsize=12,ncol=2,loc='center')
ax1.legend(fontsize=12,ncol=2,loc='center')

ax1.tick_params(labelbottom="off",bottom="off")
ax1.tick_params(labelleft="off",left="off")
ax1.set_xticklabels([])
ax1.set_yticklabels([])
ax1.spines["right"].set_color("none")  
ax1.spines["left"].set_color("none")   
ax1.spines["top"].set_color("none")    
ax1.spines["bottom"].set_color("none") 
ax1.set_xlim(-6,-2)


ax1 = plt.subplot2grid((ny,nx), (0,1))
for i in range(nt):
    ax1.plot(pt[i,:,5]*1e3,pt[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(b) w (cm kyr'+r"$\mathregular{^{-1}}$" + ')'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
ax1.set_yticklabels([])


ax1 = plt.subplot2grid((ny,nx), (1,2))
for i in range(nt):
    ax1.plot(pt[i,:,2],pt[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(f) clay (wt%)'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
ax1.set_yticklabels([])


ax1 = plt.subplot2grid((ny,nx), (0,2))
for i in range(nt):
    ax1.plot(pt[i,:,4],pt[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(c) total fraction'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
# ax1.set_xlim(0.95,1.01)
ax1.set_yticklabels([])


ax1 = plt.subplot2grid((ny,nx), (1,0))
for i in range(nt):
    ax1.plot(cc[i,:,2],cc[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(d) CaCO' +r"$\mathregular{_3}$"+ ' (wt%)'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.set_ylabel ('depth (cm)')
ax1.invert_yaxis()
ax1.set_yscale('log')



ax1 = plt.subplot2grid((ny,nx), (3,1))
for i in range(nt):
    ax1.plot(cc[i,:,7],cc[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(k) pH'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
ax1.set_yticklabels([])



ax1 = plt.subplot2grid((ny,nx), (2,0))
for i in range(nt):
    ax1.plot(cc[i,:,3]*1e3,cc[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(g) DIC (mM)'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.set_ylabel ('depth (cm)')
ax1.invert_yaxis()
ax1.set_yscale('log')


ax1 = plt.subplot2grid((ny,nx), (2,1))
for i in range(nt):
    ax1.plot(cc[i,:,4]*1e3,cc[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(h) ALK (mM)'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
ax1.set_yticklabels([])


ax1 = plt.subplot2grid((ny,nx), (2,2))
for i in range(nt):
    ax1.plot(cc[i,:,5]*1e3,cc[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(i) '+r"$\mathregular{\Delta}$"+"CO"+r"$\mathregular{_3}$"+' (mM)'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
ax1.set_yticklabels([])


ax1 = plt.subplot2grid((ny,nx), (1,1))
for i in range(nt):
    plt.plot(om[i,:,2],om[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(e) OM (wt%)'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
ax1.set_yticklabels([])


ax1 = plt.subplot2grid((ny,nx), (3,0))

for i in range(nt):
    ax1.plot(o2[i,:,2]*1e3,o2[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(j) O'+r"$\mathregular{_2}$"+' (mM)'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.set_ylabel ('depth (cm)')
ax1.invert_yaxis()
ax1.set_yscale('log')



ax1 = plt.subplot2grid((ny,nx), (4,1))

for i in range(nt):
    plt.plot(o2[i,:,3]*1e3,o2[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(m) Aero. OM dec. (mol cm'+r"$\mathregular{^{-3}}$"\
         +' kyr'+r"$\mathregular{^{-1}}$"+')'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
ax1.set_yticklabels([])



ax1 = plt.subplot2grid((ny,nx), (4,2))

for i in range(nt):
    plt.plot(o2[i,:,4]*1e3,o2[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(n) Anaero. OM dec. (mol cm'+r"$\mathregular{^{-3}}$"\
         +' kyr'+r"$\mathregular{^{-1}}$"+')'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.invert_yaxis()
ax1.set_yscale('log')
ax1.set_yticklabels([])



ax1 = plt.subplot2grid((ny,nx), (4,0))

for i in range(nt):
    plt.plot(cc[i,:,6]*1e3,cc[i,:,0],'-x',c=color[i]\
             ,label=label[i]\
             )
ax1.text(tx, ty\
         ,'(l) CaCO'+r"$\mathregular{_3}$"+' dissol. (mol cm'\
         +r"$\mathregular{^{-3}}$"\
         +' kyr'+r"$\mathregular{^{-1}}$"+')'\
         ,horizontalalignment='center',verticalalignment='center'\
         , transform=ax1.transAxes\
         ,fontsize=fs\
         )
ax1.set_ylabel ('depth (cm)')
ax1.invert_yaxis()
ax1.set_yscale('log')




##fig.tight_layout()
fig.subplots_adjust(left=0.1,bottom=0.1,wspace=0.06,hspace=0.2)
outfilename = Workdir+"2106_matlab_caco3_changedt_highccrr.svg" # you can modify the fig name and location 
plt.savefig(outfilename, transparent=True)
# if you do not have inkscape comment out the following three lines 
# subprocess.call('"C:\Program Files\Inkscape\inkscape.exe" -z -f ' \
#                + outfilename + ' --export-emf '+outfilename+\
#                '.emf',shell=True)
# subprocess.call(['/usr/bin/inkscape', Workdir+"caco3_model_sum_multi.svg", "./0_file1.pdf"])
# p = subprocess('/usr/bin/inkspace','caco3_model_sum.svg','0_file1.pdf')
plt.show()
plt.clf()
plt.close()
##"""

if 3<2:
	"""
	Only for multiple spicies simulations with different 13C and 18O signatures
	"""

	##fig = plt.figure(figsize=(14,20)) # long
	fig = plt.figure(figsize=(20,14)) #wide

	nfig = nsp + 1 #+ 2

	nx = 3
	ny = int(math.ceil(nfig/float(nx))) 

	tit=[chr(i) for i in range(97,97+nfig)]
	if nfig>26:tit=[str(i) for i in range(1,1+nfig)]
	spstr = np.empty((nsp),dtype='|S5')
	for i in range(nsp):
	    spstr[i] = '{:03d}'.format(i+1)

	for j in range(nsp):
	    ax1 = plt.subplot2grid((ny,nx), (int(math.floor(j/float(nx))),j%nx))

	    for i in range(nt):
		ax1.plot(ccsp[i,:,j+2],ccsp[i,:,0],'-x',c=color[i]\
		         ,label=label[i]\
		         )
	    ax1.text(tx, ty\
		     ,'('+tit[j]+')'+' CaCO' +r"$\mathregular{_3}$"+'_SP:'\
		     +spstr[j] \
		     ,horizontalalignment='center',verticalalignment='center'\
		     , transform=ax1.transAxes\
		     ,fontsize=fs\
		     )
	    if j%nx==0: ax1.set_ylabel ('depth (cm)')
	    ax1.invert_yaxis()
	    ax1.set_yscale('log')
	    if j%nx!=0: ax1.set_yticklabels([])


	# j=nsp+1
	# ax1 = plt.subplot2grid((ny,nx), (int(math.floor(j/float(nx))),j%nx))

	# for i in range(nt):
	    # ax1.plot(sig[i,:,2],sig[i,:,0],'-x',c=color[i]\
		     # ,label=label[i]\
		     # )
	# ax1.text(tx, ty\
		 # ,'('+tit[j-1]+')'+' ' +r"$\mathregular{\delta}$" \
		 # +r"$\mathregular{^{13}}$"+'C'+ ' ('\
		 # +u'\u2030'+')'\
		 # ,horizontalalignment='center',verticalalignment='center'\
		 # , transform=ax1.transAxes\
		 # ,fontsize=fs\
		 # )
	# if j%nx==0: ax1.set_ylabel ('depth (cm)')
	# ax1.invert_yaxis()
	# ax1.set_yscale('log')
	# if j%nx!=0: ax1.set_yticklabels([])


	# j=nsp+2
	# ax1 = plt.subplot2grid((ny,nx), (int(math.floor(j/float(nx))),j%nx))

	# for i in range(nt):
	    # ax1.plot(sig[i,:,3],sig[i,:,0],'-x',c=color[i]\
		     # ,label=label[i]\
		     # )
	# ax1.text(tx, ty\
		 # ,'('+tit[j-1]+')'+' ' +r"$\mathregular{\delta}$" \
		 # +r"$\mathregular{^{18}}$"+'O'+ ' ('\
		 # +u'\u2030'+')'\
		 # ,horizontalalignment='center',verticalalignment='center'\
		 # , transform=ax1.transAxes\
		 # ,fontsize=fs\
		 # )
	# if j%nx==0: ax1.set_ylabel ('depth (cm)')
	# ax1.invert_yaxis()
	# ax1.set_yscale('log')
	# if j%nx!=0: ax1.set_yticklabels([])

	j=nsp
	ax1 = plt.subplot2grid((ny,nx), (int(math.floor(j/float(nx))),j%nx))

	for i in range(nt):
	    ax1.plot(pt[i,:,3],pt[i,:,0],'-x',c=color[i]\
		     ,label=label[i]\
		     )
	# ax1.legend(facecolor='None',edgecolor='None',fontsize=12,ncol=3,loc='center')
	ax1.legend(fontsize=12,ncol=3,loc='center')

	ax1.tick_params(labelbottom="off",bottom="off")
	ax1.tick_params(labelleft="off",left="off")
	ax1.set_xticklabels([])
	ax1.set_yticklabels([])
	ax1.spines["right"].set_color("none")  
	ax1.spines["left"].set_color("none")   
	ax1.spines["top"].set_color("none")    
	ax1.spines["bottom"].set_color("none") 
	ax1.set_xlim(-6,-2)


	##fig.tight_layout()
	fig.subplots_adjust(left=0.1,bottom=0.1,wspace=0.06,hspace=0.2)
	outfilename = Workdir+"2006_matlab_caco3_multi_NOchangedt.svg"
	plt.savefig(outfilename, transparent=True)
	# if you do not have inkscape comment out the following three lines 
	# subprocess.call('"C:\Program Files\Inkscape\inkscape.exe" -z -f ' \
	#                + outfilename + ' --export-emf '+outfilename+\
	#                '.emf',shell=True)
	# subprocess.call(['/usr/bin/inkscape', 'caco3_model_sum_multi.svg', '0_file2.pdf'])
	# p = subprocess('/usr/bin/inkspace','caco3_model_sum_multi.svg','0_file2.pdf')
	plt.show()
	plt.clf()
	plt.close()
