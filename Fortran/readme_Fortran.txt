Memo for IMP Fortran ver. 

caco3_therm.f90: CaCO3 thermodynamic subroutines & functions   
caco3_test_mod_v5_6.f90: Main subroutines 
caco3_fortran.f90: Just to call main subroutines  

---- Prerequisites: BLAS (& UMFPACK if you choose to use sparse matrix solver) libraries -----

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
(0) Modify /input/defines.h file depending on the simulation you want 
(1) Compile: 
        a) gfortran -c caco3_therm.f90
        b) gfortran -c -cpp -I/path/to/iMP/input caco3_test_mod_v5_6.f90
    [if you choose not to use sparse matrix solver in defines.h (default)] 
        c) gfortran caco3_fortran.f90 caco3_test_mod_v5_6.o caco3_therm.o -lopenblas -g -fcheck=all
    [if you choose to use sparse matrix solver in defines.h]
        c) gfortran caco3_fortran.f90 caco3_test_mod_v5_6.o caco3_therm.o umf4_f77wrapper.o 
            -lumfpack -lamd -lcholmod -lcolamd -lsuitesparseconfig -lopenblas -g -fcheck=all
(2) Run compiled code
    [if you choose to use input file to give boundary conditions in defines.h (default)]
    Type './a.exe biot X ox Y fl Z'
        where 
        X is bioturbation mode (enter fickian, turbo2, labs, or nobio, for Fickian-, homogeneous-, LABS- or No-mixing, respectively)
        Y is OM degradation scheme (enter false or ture, with true allowing only oxic degradation)
        Z is the file name you would like to give to result directory
            E.g.) Typing './a.exe biot fickian ox false fl test_simu' will simulate 
                CaCO3 multiple particles diagenesis with Fickian mixing and oxic+anoxic OM degradation, 
                with saving results in ../../imp_output/fortran/test_simu directory 
    [if you choose not to use input file to give boundary conditions in defines.h]
    Type './a.exe cc A rr B dep C dt D biot X ox Y fl Z'
        where 
        A is caco3_rainflux_value [mol cm-2 yr-1]
        B is OM/caco3 rain ratio 
        C is value to which water depth changes during signal change event [km]        
        D is the time step, which is used only when you run a steady state simulation [yr] 
            E.g.) Typing './a.exe cc 12e-6 rr 0.7 dep 4.5 biot fickian ox false fl test_simu' will simulate 
                CaCO3 multiple particle diagenesis with Fickian mixing and oxic+anoxic OM degradation 
                assuming 12 umol cm-2 yr-1 CaCO3 rain flux with 0.7 OM/CaCO3 rain flux ratio
                and water depth change to 4.5 km during signal change event, 
                with saving results in ../../imp_output/fortran/test_simu directory 
(3) Plot results        
    (a-1) Time evolution of signals and solid and aqueous phases are stored in a directory within /imp_output/.../profiles/ directory. 
        There, the directory name changes with OM degradation scheme and bioturbation mode as well as the file name you specified (Z in above)
            E.g.) when you run a simulation by typing './a.exe biot turbo2 ox true fl demo' then 
                the directory is '../../imp_output/fortran/demo/ox_burbo2/profiles'. 
    (a-2) You can use python script to plot results. 
        E.g.) You can plot evolutions of signals using caco3_signals.py. There you must change the name of result directory to read data correctly. 

    (b-1) Steady-state or final state of CaCO3 concentration and burial flux are stored in a directory within /imp_output/.../res/ directory.
        There again the directory name changes with OM degradation scheme and bioturbation mode. See (a-1) above. 
    (b-2) You can use python script (e.g., /plot/caco3_lys.py) to plot results. 

-------------------- * -------- * -------------------- 

EXAMPLES 

1. Lysocline (Section 3.1)
    a. Switch on 'sense' in defines.h 
    b. Complile the code with specifying executable file name as 'sense'. 
    c. Create shell script 'pruns.sh' to run 'sense.exe' in parallel using caco3_shell.py. 
    d. Run the shell script, i.e., type './pruns.sh' 
        (See memo_shell_Fortran.txt for more details.)
    e. You can plot lysocline with /plot/caco3_lys.py script.
    
2. Bioturbation simulation (Section 3.2.1)
    a. Switch on 'reading' and 'timetrack' in defines.h 
    b. Use rectime_EXAMPLE-BIOT.in and imp_input_EXAMPLE-BIOT.in. I.e., type the following: 
        'cd ../input' 
        'cp EXAMPLES/rectime_EXAMPLE-BIOT.in rectime.in'
        'cp EXAMPLES/imp_input_EXAMPLE-BIOT.in imp_input.in'
    c. Complile and run the code (see above).
    d. You can plot signals with /plot/caco3_signals.py. 
        *** Note that if you want to compare different bioturbation effect, 
            you need to repeat c, run the code, with assuming different bioturbation mode. 
            (changing X in (2) above) 
        *** Note also that if you want to exclude CaCO3 dissolution, 
            you need to switch on 'nondissolve' in /input/defines.h and repeat the above procedure. 

3. Dissolution experiment (Section 3.2.2)
    a. Switch on 'reading' and 'timetrack' in defines.h 
    b. Use rectime_EXAMPLE-DIS.in and imp_input_EXAMPLE-DIS-xx.in. 
        xx can be CNTRL, 4.5 or 5.0, depending on the water depth change scinario you want to impose. 
        I.e., type the following: 
        'cd ../input' 
        'cp EXAMPLES/rectime_EXAMPLE-DIS.in rectime.in'
        'cp EXAMPLES/imp_input_EXAMPLE-DIS-xx.in imp_input.in'
    c. Complile and run the code (see above).
    d. You can plot signals with /plot/caco3_signals.py. 
        *** Note that if you want to compare different bioturbation effect, 
            you need to repeat c, run the code, with assuming different bioturbation mode. 
            (changing X in (2) above)
            
4. Two size fractions (Section 3.2.3)
    a. Switch on 'reading', 'timetrack' and 'size' in defines.h 
    b. Use rectime_EXAMPLE-SIZE.in and imp_input_EXAMPLE-SIZE.in. 
        I.e., type the following: 
        'cd ../input' 
        'cp EXAMPLES/rectime_EXAMPLE-SIZE.in rectime.in'
        'cp EXAMPLES/imp_input_EXAMPLE-SIZE.in imp_input.in'
    c. Complile and run the code (see above).
    d. You can plot signals with /plot/caco3_signals.py. 
        *** Note that if you want to compare different bioturbation effect, 
            you need to repeat c, run the code, with assuming different bioturbation mode. 
            (changing X in (2) above)
            
5. Time-stepping method (Section 4.1)
    a. Switch on 'track2' in defines.h 
    b. Complile and run the code. 
        Because input files are not used, you need to specify rain flux and rain ratio when running.
        I.e., type: 
        './a.exe cc 12e-6 rr 0.7 dep 5.0 biot fickian ox false fl test_time-stepping-method'
        './a.exe cc 12e-6 rr 0.7 dep 5.0 biot turbo2 ox false fl test_time-stepping-method'
        './a.exe cc 12e-6 rr 0.7 dep 5.0 biot nobio ox false fl test_time-stepping-method'
        Three simulations will yield results with time-stepping method 
            with 3 different bio-mixing styles (see above).
    c. You can plot signals with /plot/caco3_signals.py. 
            
6. Direct-tracking method (Section 4.2)
    a. Switch on 'reading', 'timetrack' and 'isotrack' in defines.h 
    b. Use rectime_EXAMPLE-ISO.in and imp_input_EXAMPLE-ISO.in. 
        I.e., type the following: 
        'cd ../input' 
        'cp EXAMPLES/rectime_EXAMPLE-ISO.in rectime.in'
        'cp EXAMPLES/imp_input_EXAMPLE-ISO.in imp_input.in'
    c. Complile and run the code (see above).
    d. You can plot signals with /plot/caco3_signals.py. 
        *** Note that if you want to compare different bioturbation effect, 
            you need to repeat c, run the code, with assuming different bioturbation mode. 
            (changing X in (2) above)
        *** Note also that if you want to test kinetic isotope effect, 
            you need to switch on 'kie' in /input/defines.h and repeat the above procedure. 

7. Lysocline with using mocsy (Section 4.3)
    a. Switch on 'sense', 'mocsy' and 'USE_PRECISION=2' in defines.h 
    b. Compile the code with specifying executable file name as 'sense' and using mocsy.
        (See memo_mocsy_Fortran.txt for details on how to use mocsy.)
    c. Create shell script 'pruns.sh' to run 'sense.exe' in parallel using caco3_shell.py. 
    d. Run the shell script, i.e., type './pruns.sh' 
        (See memo_shell_Fortran.txt for more details.)
    e. You can plot lysocline with /plot/caco3_lys.py script.