# randomDrumGrooves
This small piece of software generates midi files with random drum grooves

to use it , you need python3 including these libraries:
- midiutil
- argparse
- tkinter

to run it, just use the command: <code>python3 midiGUI.py</code>
to use it only in the comman line, use the midi4.py file.<br>
In cli:<br>
  <code>-m</code>: number of measures (an integer)<br>
  <code>-swing</code>: do you want a swing pattern on the cymbal (1 or 0)<br>
  <code>-kick</code>: how many bass drum per measure do you want (max 8 or 12 in swing)<br>
  <code>-snare</code>: how many snares per measure you want (same as kick)<br>
  <code>-sk</code>: are anre and kick drum allowed to collide/hit on the same beat (1 or 0)<br>
  <code>-c</code>: which cymbal (HH or R)
