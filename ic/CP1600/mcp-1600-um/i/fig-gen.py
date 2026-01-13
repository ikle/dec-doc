#!/usr/bin/python3
#
# Figure Generator for MCP1600 User's Manual 1977
#
# Copyright (c) 2021-2026 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import cairo

fonts = ["Liberation Sans", "Cantarell", "Fontin Sans CR", "Latin Modern Sans"]

def font_size (c, size, right = True):
	xx = size
	yy = -size if right else size

	c.set_font_matrix (cairo.Matrix (xx, 0, 0, yy, 0, 0))

def create (M, W, H, S = 20, step = 1, grid = False, right = True):
	SW, SH = round (W * S), round (H * S)
	IW, IH = SW + M * 2 + 1, SH + M * 2 + 1

	surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, IW, IH)
	# surface = cairo.SVGSurface ("cairo.svg", W, H)

	c = cairo.Context (surface)

	if right:
		# use right-handed Cartesian coordinate system
		c.scale (1.0, -1.0)
		c.translate (0, -IH)

	# white background
	c.set_source_rgb (1.0, 1.0, 1.0)
	c.rectangle (0, 0, IW, IH)
	c.fill ()

	# clip out margins
	c.rectangle (M, M, SW + 1, SH + 1)
	c.clip ()

	# coordinates in center of pixels in user area
	c.translate (M + 0.5, M + 0.5)

	c.set_source_rgb (0.0, 0.0, 0.0)
	c.set_line_width (1.0)

	c.set_line_cap  (1)  # cairo.LineCap.ROUND
	c.set_line_join (1)  # cairo.LineJoin.ROUND

	if grid:
		c.set_dash ([0, 4])

		for i in range (0, SW + 1, S):
			c.move_to (i,  0)
			c.line_to (i, SH)
			c.stroke ()

		for j in range (0, SH + 1, S):
			c.move_to (0,  j)
			c.line_to (SW, j)
			c.stroke ()

		c.set_dash ([])

	# scale to user coordinates
	c.scale (S / step, S / step)
	c.set_line_width (0.0625 * step)
	font_size (c, 0.5 * step)

	c.select_font_face (fonts[3])

	return surface, c

def write (surface, path):
	surface.write_to_png ('fig-' + path + '.png')

def line (c, x0, y0, x1, y1):
	c.move_to (x0, y0)
	c.line_to (x1, y1)

def hline (c, x0, y0, dx):
	line (c, x0, y0, x0 + dx, y0)

def vline (c, x0, y0, dy):
	line (c, x0, y0, x0, y0 + dy)

def text (c, x, y, label, align = 0.0):
	label = str (label)
	e = c.text_extents (label)
	c.move_to (x - e.width * align, y)
	c.show_text (label)

def ctext (c, x, y, label):
	text (c, x - 0.1, y, label, 0.5)

# Common Definitions

H = 2		# word format diagram height

def tick_len (tick):
	if tick == 'l':  return H
	if tick == 'o':  return H / 2.5
	if tick == '.':  return H / 5

	return 0

def ticks (c, x, y, prog, nums = None):
	total = len (prog) - 1
	dx = total * H

	hline (c, x, y,     dx)
	hline (c, x, y + H, dx)

	X = x + dx

	for a in prog:
		h = tick_len (a)

		if h > 0:
			vline (c, X, y, h)

		X -= H

	c.stroke ()

	if nums != None:
		font_size (c, 0.75)
		X = x + dx - H / 2

		for i in range (0, total):
			if nums[i] == 'x':
				ctext (c, X, y - 1, i)

			X -= H

def bfl (c, x, y, total, start, size, label):	# bit field label
	font_size (c, 1)

	x += (total - start - size / 2) * H
	text (c, x, y + 0.64, label, 0.5)

def bfls (c, x, y, prog):
	cmds  = list (zip (prog[::2], prog[1::2]))
	total = 0
	start = 0

	for size, label in cmds:
		total += size

	for size, label in cmds:
		if label != None:
			bfl (c, x, y, total, start, size, label)

		start += size

def desc (c, x, y, name, syntax, time):
	font_size (c, 1)
	y += H + 0.5

	if name   != None:  text (c, x,          y, name)
	if syntax != None:  text (c, x + H *  8, y, syntax, 0.5)
	if time   != None:  text (c, x + H * 16, y, time,   1.0)

# fig-5-1

surface, c = create (8, 32, 4.64, 11)

ticks (c, 0, 2.64, 'l..........ll...l', 'x.........xxx..x')
bfls  (c, 0, 2.64, [11, 'Address', 1, 'R', 4, 'Opcode'])

ctext (c, 16, 0.32, 'Jump Format')

write (surface, '5-1-jmp')

# fig-5-2

surface, c = create (8, 32, 4.64, 11)

ticks (c, 0, 2.64, 'l.......l...l...l', 'x......xx..xx..x')
bfls  (c, 0, 2.64, [8, 'Address', 4, 'Cond', 4, 'Opcode'])

ctext (c, 16, 0.32, 'Conditional Jump Format')

write (surface, '5-2-jcc')

# fig-5-3

surface, c = create (8, 32, 4.64, 11)

ticks (c, 0, 2.64, 'l...l.......l...l', 'x..xx......xx..x')
bfls  (c, 0, 2.64, [4, 'a', 8, 'Literal', 4, 'Opcode'])

ctext (c, 16, 0.32, 'Literal Format')

write (surface, '5-3-lit')

# fig-5-4

surface, c = create (8, 32, 4.64, 11)

ticks (c, 0, 2.64, 'l...l...l.......l', 'x..xx..xx......x')
bfls  (c, 0, 2.64, [4, 'a', 4, 'b', 8, 'Opcode'])

ctext (c, 16, 0.32, 'Register Format')

write (surface, '5-4-reg')

