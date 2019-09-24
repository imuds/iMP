Memo for IMP Fortran ver. 

caco3_therm.f90: CaCO3 thermodynamic subroutines & functions   
caco3_test_mod_v5_6.f90: Main subroutines 
caco3_fortran.f90: Just to call main subroutines  

---- Prerequisites: BLAS (& UMFPACK if you choose to use sparce matrix solver) libraries -----

>>> BLAS (OpenBLAS) install 
(Google yourself or)
1. download: http://www.openblas.net/ -> TAR
2. tar zxvf OpenBLAS-0.2.20.tar.gz
3. cd OpenBLAS-0.2.20
4. make BINARY=64 CC="gcc -m64" FC="gfortran -m64"
5. su
6. make PREFIX=/usr/local install

If you get the error 'libopenblas.so.0: cannot open shared object file: No such file or directory' then type
1. sudo apt-get install libopenblas-base
2. export LD_LIBRARY_PATH=/usr/lib/openblas-base/

>>> UMFPACK install 
(Google yourself or)
See https://github.com/PetterS/SuiteSparse/tree/master/UMFPACK for 
(*** Note that UMFPACK is usually not necessary) 

-------------------- * -------- * -------------------- 

Simulation can be run by following steps:
(0) Modify input/defines.h file depending on the simulation you want 
(1) Compile: 
        a) gfortran -c caco3_therm.f90
        b) gfortran -c -cpp -I/path/to/iMP/input caco3_test_mod_v5_6.f90
    [if you choose not to use sparce matrix solver in defines.h (default)] 
        c) gfortran caco3_fortran.f90 caco3_test_mod_v5_6.o caco3_therm.o -lopenblas -g -fcheck=all
    [if you choose to use sparce matrix solver in defines.h]
        c) gfortran caco3_fortran.f90 caco3_test_mod_v5_6.o caco3_therm.o umf4_f77wrapper.o 
            -lumfpack -lamd -lcholmod -lcolamd -lsuitesparseconfig -lopenblas -g -fcheck=all
(2) Run compiled code
    [if you choose to use input file to give boundary conditions in defines.h (default)]
    Type './a.exe biot X ox Y fl Z'
        where 
        X is bioturbation mode (enter fickian, turbo2, labs, or nobio, for Fickian-, homogeneous-, LABS- or No-mixing, respectively)
        Y is OM degradation scheme (enter false or ture, with true allows only oxic degradation)
        Z is the file name you would like to give to result directory
            E.g.) Typing './a.exe biot fickian ox false fl test_simu' will simulate 
                CaCO3 multip particle diagenesis with Fickian mixing and oxic+anoxic OM degradation 
                saving results in output/profiles/oxanox/test_simu directory 
    [if you choose not to use input file to give boundary conditions in defines.h]
    Type './a.exe cc A rr B dep C dt D biot X ox Y fl Z'
        where 
        A is caco3_rainflux_value [mol cm2 yr-1]
        B is OM/caco3 rain ratio 
        C is value to which water depth changes during signal change event [km]        
        D is the time step, which is used only you run steady state simulation [yr] 
            E.g.) Typing './a.exe cc 12e-6 rr 0.7 dep 4.5 biot fickian ox false fl test_simu' will simulate 
                CaCO3 multiple particle diagenesis with Fickian mixing and oxic+anoxic OM degradation 
                assuming 12 umol cm2 yr-1 CaCO3 rain flux with 0.7 OM/CaCO3 rain flux ratio
                and water depth change to 4.5 km during signal change event 
                saving results in output/profiles/oxanox/test_simu directory 
(3) Plot results        
    (a-1) Time evolution of signals and solid and aqueous phases are stored in a directory within output/profiles/ directory. 
        There, the directory name changes with OM degradation scheme and bioturbation mode as well as the file name you specified (Z in above)
            E.g.) when you run a simulation by typing './a.exe biot turbo2 ox true fl demo' then 
                the directory is 'output/profiles/ox_turbo2/demo'. 
    (a-2) You can use python script to plot results. 
        E.g.) You can plot evolutions of signals using caco3_signals.py. There you must change the name of result directory to read data correctly. 

    (b-1) Steady-state or final state of CaCO3 concentration and burial flux are stored in a directory within output/res/ directory.
        There again the directory name changes with OM degradation scheme and bioturbation mode. See (a-1) above. 
    (b-2) You can use python script (e.g., plot/caco3_lys_oxanox_sum.py) to plot results. 
        