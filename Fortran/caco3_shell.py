import glob
import os
import numpy as np 
print ''
print '*** just press [enter] to choose default parameter ***'
print ''
process= raw_input('Enter paralellized process number [default= 4]: ') 
runtitle= raw_input('Enter simulation name [default= test_lys]: ') 
if len(process)==0:
    process=4
else:
    process= eval(process)
if len(runtitle)==0:
    runtitle = 'test_lys'
shellloc = os.path.dirname(os.path.abspath(__file__)) 
seriesname='prun'
filelist = glob.glob(shellloc+'/'+seriesname+'*.sh')
for i in range(len(filelist)):
    os.remove(filelist[i])
wholework=shellloc+'/'+seriesname+'s.sh'
line = '#!/bin/bash -e\n'\
       + 'a=1\n'\
       + 'while [ $a -lt ' +str(process+1) +' ]\n'\
       + 'do \n'\
       + '  echo $a\n'\
       + '  dos2unix '+seriesname+'_${a}.sh\n'\
       + '  chmod u+x "'+seriesname+'_${a}.sh"\n'\
       + '  nohup ./'+seriesname+'_${a}.sh' \
       + '> out${a}.log < /dev/null &\n' \
       + '  a=`expr $a + 1`\n' \
       + 'done\n'
f=open(wholework, 'w')
f.write(line)
f.close()

rrlist = np.array([0.0,0.5,0.6666,1.0,1.5])

cnt=0
nz = 25
for i in range(nz):
    for j in range(10):
        for k in range(5):
            for l in range(2):

##                if k!=4:continue
##                if k!=4:continue
##                if l!=1:continue

##                if j!=8:continue

                if l==0:exefile='true'  # exe. complied switching on 'oxonly'
                if l==1:exefile='false' # exe. complied without switching on 'oxonly'
                
                runfile = shellloc +'/'+ seriesname +'_'+str(cnt%process+1)+'.sh'
                f=open(runfile,'a')
                runplace = './'+'sense'  \
                           +' cc '+str(int((j+1)*6))+'e-6' \
                           +' rr '+str(rrlist[k])\
                           +' dep '+str((i+1.)*6.0/(1.0*nz))  \
                           +' dt 100000000.'  \
                           +' ox '+exefile  \
                           +' fl '+runtitle
                line = runplace \
                           +'\n'
                f.write(line)
                f.close()
                cnt+=1
