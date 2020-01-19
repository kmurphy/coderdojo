#! /usr/bin/env python

import sys
import turtle

script = sys.argv[1]

exec(compile(source=open(script).read(), filename=script, mode='exec'))

canvas = turtle.Screen().getcanvas()
canvas.postscript(file="out.ps")

import subprocess
subprocess.call(['epstopdf', 'out.ps', script.replace(".py", ".pdf")])