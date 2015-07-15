#!/usr/bin/env python
if 64 - 64: i11iIiiIii
class OO0o :
 def __init__ ( self , val , parentL , parentR ) :
  self . r = parentR
  self . i = parentL
  self . val = val
  if 81 - 81: Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o
import pdb
if 4 - 4: IiII1IiiIiI1 / iIiiiI1IiI1I1
def o0OoOoOO00 ( pyramid , selfRow , selfIndex ) :
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
 o0OOO = 0
 if ( selfIndex == 0 ) :
  o0OOO = int ( pyramid [ selfRow - 1 ] [ selfIndex ] ) + int ( pyramid [ selfRow ] [ selfIndex ] )
 elif ( selfIndex == selfRow ) :
  o0OOO = int ( pyramid [ selfRow - 1 ] [ selfIndex - 1 ] ) + int ( pyramid [ selfRow ] [ selfIndex ] )
 else :
  iIiiiI = int ( pyramid [ selfRow - 1 ] [ selfIndex ] ) + int ( pyramid [ selfRow ] [ selfIndex ] )
  Iii1ii1II11i = int ( pyramid [ selfRow - 1 ] [ selfIndex - 1 ] ) + int ( pyramid [ selfRow ] [ selfIndex ] )
  if ( iIiiiI > Iii1ii1II11i ) :
   o0OOO = iIiiiI
  else :
   o0OOO = Iii1ii1II11i
   if 10 - 10: I1iII1iiII + I1Ii111 / OOo
 return o0OOO
 if 41 - 41: I1II1
def Ooo0OO0oOO ( pyramid ) :
 oooO0oo0oOOOO = len ( pyramid . keys ( ) )
 for O0oO in xrange ( 1 , oooO0oo0oOOOO ) :
  for o0oO0 in range ( 0 , O0oO + 1 ) :
   pyramid [ O0oO ] [ o0oO0 ] = o0OoOoOO00 ( pyramid , O0oO , o0oO0 )
 oo00 = 0
 for o00 in pyramid [ oooO0oo0oOOOO - 1 ] :
  if ( o00 >= oo00 ) :
   oo00 = o00
 print oo00
 if 62 - 62: II1ii - o0oOoO00o . iIi1IIii11I + oo0 * o0oOoO00o % o0oOoO00o
def i11 ( fname ) :
 I11 = { }
 Oo0o0000o0o0 = open ( fname , "r" )
 oOo0oooo00o = 0
 for oO0o0o0ooO0oO in Oo0o0000o0o0 :
  I11 [ oOo0oooo00o ] = oO0o0o0ooO0oO [ : - 1 ] . split ( " " )
  oOo0oooo00o += 1
 Oo0o0000o0o0 . close ( )
 return I11
 if 52 - 52: ooO0OO000o - i11iIiiIii % iIi1IIii11I
def O0OoOoo00o ( ) :
 iiiI11 = i11 ( "ntxt" )
 Ooo0OO0oOO ( iiiI11 )
 if 91 - 91: Ooo00oOo00o / ooO0OO000o . I1IiI + I1Ii111
 if 47 - 47: Oo / I1II1 * iiiii
O0OoOoo00o ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
