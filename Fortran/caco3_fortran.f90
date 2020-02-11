program caco3_fort
implicit none 
! contains 
real(kind=8)::ccflxi,om2cc,dtinput,dep,ztot,detflxi,tempi,o2i,alki,dici,co3sati,sali,aomflxin,zsrin
character*555::runname,biotmode,co2chem,runmode
logical::oxonly

call getinput_v2(ccflxi,om2cc,dtinput,runname,dep,oxonly,biotmode,detflxi,tempi,o2i,alki,dici,co3sati,sali,aomflxin,zsrin)
call caco3(ccflxi,om2cc,dep,dtinput,runname,oxonly,biotmode,detflxi,tempi,o2i,dici,alki,co3sati,sali,aomflxin,zsrin) 

endprogram 
