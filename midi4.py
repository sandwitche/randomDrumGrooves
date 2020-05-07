import sys
from midiutil.MidiFile import MIDIFile
import random
from random import choice
from random import randrange
import argparse


#get values from arguments
parser = argparse.ArgumentParser(description='generate random grooves')
parser.add_argument('-m', metavar='NUMBER', default=8, type=int, help="number of measures to generate(default:8)")
parser.add_argument('-swing', metavar='NUMBER', default=0, type=int, help="swing pattern or not(0=False, 1=True, default:0)")
parser.add_argument('-sk', metavar='NUMBER', default=0, choices=[0, 1], type=int, help="is it allowed to have a snare drum and a kick drumon the same beat(0=False, 1=True, default:1)")
parser.add_argument('-c', metavar='STRING', default="R", choices=['R', 'HH'], type=str, help="cymbal tye(HH=Hi-Hat, R=ride, default:ride")
parser.add_argument('-kick', metavar='NUMBER', default=2, choices=range(0,16), type=int, help="number of kick drum hits to generate per measure(default:2)")
parser.add_argument('-snare', metavar='NUMBER', default=2, choices=range(0,16), type=int, help="number of snare drum hits to generate per measure(default:2)")
args=parser.parse_args()


if args.swing==1 and 1==2 and args.kick >= 12 or args.snare >= 12:
    sys.exit("ERROR\nIf you use swing, you can enter a maximum of 12 notes per measure, please use a numbe lower than 12")
if args.swing==1 and args.sk==0 and args.kick+args.snare>12:
    sys.exit("ERROR\nIf you use swing and don't want to have snare and kick collide, you need to have less than 12 notes.")



cymbal=args.c
measures=args.m
nkick=args.kick
nsnare=args.snare
sk=args.sk

#variable declaration stuff
track = 0   # the only track
time = 0    # start at the beginning
channel = 9
volume = 100
kick=35;snare=38
if cymbal=="R":
    cymbal=51
if cymbal=="HH":
    cymbal=42

nn=0;

# create your MIDI object
mf = MIDIFile(1)     # only 1 track
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)




#cymbal swing pattern
if args.swing:
    for s in range(0, measures):
        mf.addNote(track, channel, cymbal, 0+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 1+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 5/3+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 2+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 3+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 11/3+4*s, 1, volume)
else:
    for s in range(0, measures):
        mf.addNote(track, channel, cymbal, 0+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 1/2+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 2/2+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 3/2+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 4/2+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 5/2+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 6/2+4*s, 1, volume)
        mf.addNote(track, channel, cymbal, 7/2+4*s, 1, volume)
    


if args.swing:
    un=[0/3,1/3,2/3,3/3,4/3,5/3,6/3,7/3,8/3,9/3,10/3,11/3]
else:
    un=[0/2,1/2,2/2,3/2,4/2,5/2,6/2,7/2]


kn=[None]*measures
sn=[None]*measures
uc=[None]*measures


import time
start=time.time()

#snare and drum pattern
for c in range (0, measures):
        while True:
            #guess a combination
            kn = random.sample(un, nkick)
            sn = random.sample(un, nsnare)

            kn.sort()
            
            #check pattern doesn't already exist
            repeat=False
            for i  in range(0, c):
                if set(kn) in uc:
                    #print(i)
                    repeat=True
            if repeat:
                continue


            #check if snare and kick collide
            if not sk:
                if set(kn)&set(sn):
                    continue

            
            #enter midi notes
            for i in range(0, nkick):
                mf.addNote(track, channel, kick, kn[i]+4*c, 1/3, volume)
            for i in range(0, nsnare):
                mf.addNote(track, channel, snare, sn[i]+4*c, 1/3, volume)
                
            uc[c]=set(kn)
            uc[-c]=set(sn)
            
            #print(c)
            break;




end=time.time()
print("time taken for generation:")
print(end-start)




# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
print("\nmidi exported to output.mid\n")



'''
#example
pitch = 64           # C4 (middle C)
time = 0             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)
'''
