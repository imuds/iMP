! using 'test' directory 
#define test 

! reading input data
#define reading 

! testing 5kyr signal change event 
! #define biotest

! testting two size caco3 simulation 
! #define size 

! without signal tracking 
! #define sense

! using method2 to track signals (default 42 species)
! #define track2 

! time tracking 
! #define timetrack

! specify the background depth (default 3.5 km)
! #define depiinput 4.0

! specify the number of caco3 species (if not, nspccinput=4)
! #define nspccinput 22

! specify the grid number (if not, nzinput=100)
! #define nzinput 100

! not showing results on display 
! #define nondisp

! not recording profiles 
! #define nonrec

! shwoing every iteration 
! #define showiter

! using sparse matrix solve (you need UMFPACK) 
! #define sparse

! all turbo2 mixing 
! #define allturbo2 

! all labs mixing 
! #define alllabs 

! no bioturbation 
! #define allnobio 

! enabling only oxic degradation of om 
! #define oxonly

! recording the grid to be used for making transition matrix in LABS 
!#define recgrid

! specify ref om decomp rate const (default 0.06 [yr-1])
! #define komi_input 0.06

! specify ref cc dissolution rate const (default 365.25 [yr-1])
! #define kcci_input 365.25

! if assuming linear rate law for CaCO3 dissolution
! #define linear

! if assuming no om decomposition 
! #define nodecomp

! if assuming no caco3 dissolution 
! #define nodissolve

! direct isotope tracking 
#define isotrack

! kinetic isotope effect
! #define kie

! isotope tracking also for dic
#define aqiso

! allow precipitation 
#define precip

! no 14c radio-decay 
! #define noradio

! consider diffusion boundary layer 
! #define DBL

! consider DIC and ALK fluxes from hydrate model
! #define methane 

! stepwise warm up (first reaching steady state) (better to use when allowing precipitation?)
#define stepwarm

! direct isotope tracking with including 17O 
! #define fullclump

! using mocsy for caco3 thermodynamics 
! #define mocsy

! digit used for mocsy
! #define USE_PRECISION=2

! monitor display mocsy results
! #define display