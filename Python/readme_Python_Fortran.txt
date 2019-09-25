Memo for IMP f2py ver.  

This is another way to run the model with Python
    by creating a python module from Fortran codes via f2py* and just importing and using the module.
* You need numpy.  

1. Create caco3mod.dll
    (a) Move to Fortran directory. 
        Compile caco3_therm.f90 and caco3_test_mod_v5_6.f90 as in readme file for Fortran (see readme_Fortran.txt).
    (b) Type 'python -m numpy.f2py -c -m caco3mod caco3_python.f90 caco3_test_mod_v5_6.o caco3_therm.o -lopenblas'  
        [or 'python -m numpy.f2py -c -m caco3mod caco3_python.f90 caco3_test_mod_v5_6.o caco3_therm.o umf4_f77wrapper.o
            -lumfpack -lamd -lcholmod -lcolamd -lsuitesparseconfig -llapack -lopenblas' 
            if you choose to use sparse matrix solver  
        or 'python -m numpy.f2py -c -m caco3mod caco3_python.f90 caco3_test_mod_v5_6.o caco3_therm.o call_mocsy.o 
            -lopenblas -lmocsy -L/path/to/mocsy/directory'  
            if you choose to use mocsy (see memo_mocsy_Fortran.txt)
        ]
    (c) Copy caco3mod.dll to Python directory: type 'cp caco3mod.dll ../Python'.
2. Import and use the module
    (a) Change the variables in caco3_fortran.py (rain flux of caco3, om/caco3 rain ratio, file name etc.)
        (you can change other variables in define.h before compiling fortran codes) 
    (b) Type 'python caco3_fortran.py'  

*** Note that this is just running compiled Fortran codes via Python, 
    so the results are stored in a directory for Fortran ver. 