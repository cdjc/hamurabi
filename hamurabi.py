#!/usr/bin/python3
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# Translation of HAMURABI.BS by CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY

from random import random
from goto import goto

def get_number(prompt):
    while True:
        number_string = input(prompt + " ")
        try:
            return int(number_string)
        except:
            print("THAT WAS NOT A NUMBER. PLEASE TRY AGAIN.")

@goto
def main():

    def sub710():
        print("HAMURABI:  THINK AGAIN.  YOU HAVE ONLY")
        print(S, "BUSHELS OF GRAIN.  NOW THEN,")

    def sub720():
        print("HAMURABI:  THINK AGAIN.  YOU OWN ONLY", A, "ACRES.  NOW THEN,")

    def sub800():
        nonlocal C
        C=int(random()*5)+1

    print(31*' ', "HAMURABI")
    print(14*' ', "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print(17*' ', "Bart Massey <bart.massey@gmail.com>")
    print("\n\n")
    print("TRY YOUR HAND AT GOVERNING ANCIENT SUMERIA")
    print("FOR A TEN-YEAR TERM OF OFFICE.")
    print()
    D1=0
    P1=0
    Z=0
    P=95
    S=2800
    H=3000
    E=H-S
    Y=3
    A=H//Y
    I=5
    Q=1
    label .line210
    D=0
    label .line215
    print("\n\n")
    print("HAMURABI:  I BEG TO REPORT TO YOU,")
    Z=Z+1
    print("IN YEAR", str(Z) + ",", \
          D, "PEOPLE STARVED,", I, "CAME TO THE CITY,")
    P=P+I
    if Q>0:
        goto .line230
    P=P//2
    print("A HORRIBLE PLAGUE STRUCK!  HALF THE PEOPLE DIED.")
    label .line230
    print("POPULATION IS NOW", P)
    print("THE CITY NOW OWNS", A, "ACRES.")
    print("YOU HARVESTED", Y, "BUSHELS PER ACRE.")
    print("THE RATS ATE", E, "BUSHELS.")
    print("YOU NOW HAVE", S, "BUSHELS IN STORE.")
    print()
    if Z==11:
        goto .line860
    C=int(10*random())
    Y=C+17
    print("LAND IS TRADING AT", Y, "BUSHELS PER ACRE.")
    label .line320
    Q=get_number("HOW MANY ACRES DO YOU WISH TO BUY")
    if Q<0:
        goto .line850
    if Y*Q<=S:
        goto .line330
    sub710()
    goto .line320
    label .line330
    if Q==0:
        goto .line340
    A=A+Q
    S=S-Y*Q
    C=0
    goto .line400
    label .line340
    Q=get_number("HOW MANY ACRES DO YOU WISH TO SELL")
    if Q<0:
        goto .line850
    if Q<A:
        goto .line350
    sub720()
    goto .line340
    label .line350
    A=A-Q
    S=S+Y*Q
    C=0
    label .line400
    print()
    label .line410
    Q=get_number("HOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE")
    if Q<0:
        goto .line850
    # *** TRYING TO USE MORE GRAIN THAN IS IN SILOS?
    if Q<=S:
        goto .line430
    sub710()
    goto .line410
    label .line430
    S=S-Q
    C=1
    print()
    label .line440
    D=get_number("HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED")
    if D==0:
        goto .line511
    if D<0:
        goto .line850
    # *** TRYING TO PLANT MORE ACRES THAN YOU OWN?
    if D<=A:
        goto .line450
    sub720()
    goto .line440
    # *** ENOUGH GRAIN FOR SEED?
    label .line450
    if D//2<=S:
        goto .line455
    sub710()
    goto .line440
    # *** ENOUGH PEOPLE TO TEND THE CROPS?
    label .line455
    if D<=10*P:
        goto .line510
    print("BUT YOU HAVE ONLY", P, "PEOPLE TO TEND THE FIELDS!  NOW THEN,")
    goto .line440
    label .line510
    S=S-D//2
    label .line511
    sub800()
    # *** A BOUNTIFUL HARVEST!
    Y=C
    H=D*Y
    E=0
    sub800()
    if C % 2 == 1:
        goto .line530
    # *** RATS ARE RUNNING WILD!!
    E=S//C
    label .line530
    S=S-E+H
    sub800()
    # *** LET'S HAVE SOME BABIES
    I=int(C*(20*A+S)/P/100+1)
    # *** HOW MANY PEOPLE HAD FULL TUMMIES?
    C=Q//20
    # *** HORROS, A 15% CHANCE OF PLAGUE
    Q=int(10*(2*random()-.3))
    if P<C:
        goto .line210
    # *** STARVE ENOUGH FOR IMPEACHMENT?
    D=P-C
    if D>.45*P:
        goto .line560
    P1=((Z-1)*P1+D*100/P)/Z
    P=C
    D1=D1+D
    goto .line215
    label .line560
    print()
    print("YOU STARVED", D, "PEOPLE IN ONE YEAR!!!")
    label .line565
    print("DUE TO THIS EXTREME MISMANAGEMENT YOU HAVE NOT ONLY")
    print("BEEN IMPEACHED AND THROWN OUT OF OFFICE BUT YOU HAVE")
    print("ALSO BEEN DECLARED NATIONAL FINK!!!!")
    goto .line990
    label .line850
    print()
    print("HAMURABI:  I CANNOT DO WHAT YOU WISH.")
    print("GET YOURSELF ANOTHER STEWARD!!!!!")
    goto .line990
    label .line860
    print("IN YOUR 10-YEAR TERM OF OFFICE,", P1, "PERCENT OF THE")
    print("POPULATION STARVED PER YEAR ON THE AVERAGE, I.E. A TOTAL OF")
    print(D1, "PEOPLE DIED!!")
    L=A/P
    print("YOU STARTED WITH 10 ACRES PER PERSON AND ENDED WITH")
    print(L, "ACRES PER PERSON.")
    print()
    if P1>33:
        goto .line565
    if L<7:
        goto .line565
    if P1>10:
        goto .line940
    if L<9:
        goto .line940
    if P1>3:
        goto .line960
    if L<10:
        goto .line960
    print("A FANTASTIC PERFORMANCE!!!  CHARLEMANGE, DISRAELI, AND")
    print("JEFFERSON COMBINED COULD NOT HAVE DONE BETTER!")
    goto .line990
    label .line940
    print("YOUR HEAVY-HANDED PERFORMANCE SMACKS OF NERO AND IVAN IV.")
    print("THE PEOPLE (REMIANING) FIND YOU AN UNPLEASANT RULER, AND,")
    print("FRANKLY, HATE YOUR GUTS!!")
    goto .line990
    label .line960
    print("YOUR PERFORMANCE COULD HAVE BEEN SOMEWHAT BETTER, BUT")
    print("REALLY WASN'T TOO BAD AT ALL. ", int(P*.8*random()), "PEOPLE")
    print("WOULD DEARLY LIKE TO SEE YOU ASSASSINATED BUT WE ALL HAVE OUR")
    print("TRIVIAL PROBLEMS.")
    label .line990
    print()
    print(chr(7)*10 + "SO LONG FOR NOW.")
    print()

main()
