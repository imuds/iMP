! using 'test' directory 
#define test 

! testing 5kyr signal change event 
! #define biotest

! testting two size caco3 simulation 
!#define size 

! without signal tracking 
! #define sense

! using method2 to track signals (default 42 species)
#define track2 

! specify the number of caco3 species (if not, nspccinput=4)
#define nspccinput 22

! specify the grid number (if not, nzinput=100)
! #define nzinput 100

! not showing results on display 
! #define nondisp

! not recording profiles 
! #define nonrec

! shwoing every iteration 
! #define showiter

! using sparse matrix solve (you need UMFPACK) 
#define sparse

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

! if assuming no caco3 dissolution 
! #define nodissolve

! direct isotope tracking 
! #define isotrack

! direct isotope tracking with including 17O 
! #define fullclump

! using mocsy for caco3 thermodynamics 
! #define mocsy

! digit used for mocsy
! #define USE_PRECISION=2

! monitor display mocsy results
! #define display