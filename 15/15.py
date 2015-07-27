#!/usr/bin/env python
import pdb
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
def o0OO00 ( dic ) :
 oo = " "
 for i1iII1IiiIiI1 in dic :
  oo += str ( dic [ i1iII1IiiIiI1 ] ) + " "
 #print oo
 if 40 - 40: ooOoO0O00 * IIiIiII11i
def o0oOOo0O0Ooo ( thisLvlNodes , currentLvl , numOfLvls ) :
 max = 1
 o0OO00 ( thisLvlNodes )
 while ( currentLvl <= numOfLvls ) :
  currentLvl += 1
  I1ii11iIi11i = { }
  I1IiI = currentLvl
  for o0OOO in xrange ( 0 , I1IiI ) :
   if ( o0OOO == 0 ) :
    I1ii11iIi11i [ o0OOO ] = thisLvlNodes [ 0 ]
   elif ( o0OOO == I1IiI - 1 ) :
    I1ii11iIi11i [ o0OOO ] = thisLvlNodes [ o0OOO - 1 ]
   else :
    I1ii11iIi11i [ o0OOO ] = thisLvlNodes [ o0OOO - 1 ] + thisLvlNodes [ o0OOO ]
   if ( max < I1ii11iIi11i [ o0OOO ] ) :
    max = I1ii11iIi11i [ o0OOO ]
  thisLvlNodes = I1ii11iIi11i
  I1ii11iIi11i = { }
  o0OO00 ( thisLvlNodes )
  if 13 - 13: ooOo + Oo
 print max
 if 67 - 67: O00ooOO . I1iII1iiII
def iI1Ii11111iIi ( ) :
 i1i1II = { 0 : 1 }
 O0oo0OO0 = 40
 I1i1iiI1 = 1
 o0oOOo0O0Ooo ( i1i1II , I1i1iiI1 , O0oo0OO0 )
 if 24 - 24: oOOOO0o0o
 if 40 - 40: II / oo00 * i1I1Ii1iI1ii * o0oOoO00o . i1
iI1Ii11111iIi ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
