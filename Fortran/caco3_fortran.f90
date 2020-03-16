program caco3_fort
implicit none 
! contains 
real(kind=8)::ccflxi,om2cc,dtinput,dep,ztot,detflxi,tempi,o2i,alki,dici,co3sati,sali,aomflxin,zsrin  &
    ,d13c_ocn_in,d13c_caco3_in,d13c_poc_in
character*555::runname,biotmode,co2chem,runmode
character*7::locin
logical::oxonly

call getinput_v2(  &
    ccflxi,om2cc,dtinput,runname,dep,oxonly,biotmode,detflxi  &
    ,tempi,o2i,alki,dici,co3sati,sali,aomflxin,zsrin,locin  &
    ,d13c_ocn_in,d13c_caco3_in,d13c_poc_in  &
    )
call caco3(  &
    ccflxi,om2cc,dep,dtinput,runname,oxonly,biotmode,detflxi  &
    ,tempi,o2i,dici,alki,co3sati,sali,aomflxin,zsrin,locin  &
    ,d13c_ocn_in,d13c_caco3_in,d13c_poc_in  &
    ) 

endprogram 
