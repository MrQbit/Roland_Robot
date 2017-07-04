#! /usr/bin/python

import wheels
import sys
import sonar
import configure

usage = '''
robot

Tell the robot what to do.

Commands 

Actions
-------
forward
backward
left
right
stop
shake

Test Wheels
-----------
wheel1
wheel2
wheel3
wheel4

Test Sonar
----------
leftdist
rightdist
centerdist 
'''

print sys.argv

if (len(sys.argv) == 1):
	print usage
	exit(1)

cmd = sys.argv[1]
	
if (cmd == 'forward'):
	wheels.forward(200, 1)

elif (cmd == 'backward'):
	wheels.backward(150, 1)

elif (cmd == 'left'):
	wheels.left(-150, 0.3)

elif (cmd == 'right'):
	wheels.right(-150, .3)

elif (cmd == 'wheel1'):
	wheels.spinMotor(1, 50, 1)

elif (cmd == 'wheel2'):
	wheels.spinMotor(2, 50, 1)

elif (cmd == 'wheel3'):
	wheels.spinMotor(3, 50, 1)

elif (cmd == 'wheel4'):
	wheels.spinMotor(4, 50, 1)

elif (cmd == 'shake'):
	wheels.left(50, 0.2)
	wheels.right(50, 0.2)

elif (cmd == 'leftdist'):
	print sonar.ldist()
elif (cmd == 'rightdist'):
	print sonar.rdist()
elif (cmd == 'centerdist'):
	print sonar.cdist()

else:
	print usage



	
