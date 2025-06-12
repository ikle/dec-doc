#!/usr/bin/python3
#
# Figure Generator for PDP-11 Habdbook 1969
#
# Copyright (c) 2021-2025 Alexei A. Smekalkine <ikle@ikle.ru>
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
h = H / 5	# word format diagram bit separator height

def bfl (c, y, total, start, size, label):	# bit field label
	font_size (c, 1)

	x = (total - start - size / 2) * 2
	text (c, x, y + 0.64, label, 0.5)

# fig-014-1

surface, c = create (8, 32, 4, 11)

hline (c,  0, 2,     32)
hline (c,  0, 2 + H, 32)

vline (c,  0, 2, H)
for x in range (1, 8):  vline (c, x * 2, 2, h)
vline (c, 16, 2, H)
for x in range ( 9, 11):  vline (c, x * 2, 2, h)
for x in range (11, 17):  vline (c, x * 2, 2, H)

c.stroke ()

bfl (c, 2, 16, 8, 8, 'Unused')
bfl (c, 2, 16, 5, 3, 'Prority')
bfl (c, 2, 16, 4, 1, 'T')
bfl (c, 2, 16, 3, 1, 'N')
bfl (c, 2, 16, 2, 1, 'Z')
bfl (c, 2, 16, 1, 1, 'V')
bfl (c, 2, 16, 0, 1, 'C')

ctext (c, 16, 0.32, 'Central Processor Status Register (PS)')

surface.write_to_png ('fig-014-1.png')

# fig-019-1

def afe (c, y):					# address field example
	hline (c,  0, y,     32)
	hline (c,  0, y + H, 32)

	vline (c,  0, y, H)
	for x in range ( 1, 10):  vline (c, x * 2, y, h)
	vline (c, 20, y, H)
	for x in range (11, 13):  vline (c, x * 2, y, h)
	vline (c, 26, y, H)
	for x in range (14, 16):  vline (c, x * 2, y, h)
	vline (c, 32, y, H)

	c.stroke ()

surface, c = create (8, 32, 4, 11)

afe (c, 2)

bfl (c, 2, 16, 3, 3, 'Mode')
bfl (c, 2, 16, 0, 3, 'Register')

ctext (c, 16, 0.32, 'Instruction Word')

surface.write_to_png ('fig-019-1.png')

# fig-019-2

def afs (c, y):					# address field skeleton
	hline (c, 10, y,     12)
	hline (c, 10, y + H, 12)

	vline (c, 10, y, H)
	vline (c, 12, y, h)
	vline (c, 14, y, h)
	vline (c, 16, y, H)
	vline (c, 18, y, h)
	vline (c, 20, y, h)
	vline (c, 22, y, H)

	c.stroke ()

surface, c = create (8, 32, 5.2, 11)

afs (c, 3.2)

bfl (c, 3.2, 6 + 5, 3, 3, 0)
bfl (c, 3.2, 6 + 5, 0, 3, 'R')

ctext (c, 16, 1.52, 'Address Field — General Register Mode')
ctext (c, 16, 0.32, '(mode is indicated as an octal digit)')

surface.write_to_png ('fig-019-2.png')

# Address Fields

def amode (mode, reg, path, desc):
	surface, c = create (8, 32, 4, 11)

	afs (c, 2)

	bfl (c, 2, 6 + 5, 3, 3, mode)
	bfl (c, 2, 6 + 5, 0, 3, reg)

	ctext (c, 16, 0.32, desc)

	surface.write_to_png (path + '.png')

amode (1, 'R', 'fig-019-3', 'Address Field — Deferred Register Mode')
amode (7, 'R', 'fig-020-2', 'Address Field — Deferred Indexed Mode')
amode (2, 'R', 'fig-020-3', 'Address Field — Autoincrement')
amode (3, 'R', 'fig-020-4', 'Address Field — Autoincrement Deferred Mode')
amode (4, 'R', 'fig-021-1', 'Address Field — Autodecrement')
amode (5, 'R', 'fig-021-2', 'Address Field — Autodecrement Deferred Mode')

amode (2, 7, 'fig-021-3', 'Address Field — Immediate Mode')
amode (3, 7, 'fig-022-1', 'Address Field — Absolute Mode')
amode (6, 7, 'fig-022-2', 'Address Field — Relative Mode')
amode (7, 7, 'fig-022-4', 'Address Field — Deferred Relative Mode')

# fig-020-1

amode (6, 'R', 'fig-020-1a', 'Address Field — Indexed Mode')

surface, c = create (8, 32, 4, 11)

hline (c,  0, 2,     32)
hline (c,  0, 2 + H, 32)
vline (c,  0, 2, H)
for x in range (1,  16):  vline (c, x * 2, 2, h)
vline (c, 32, 2, H)
c.stroke ()

bfl (c, 2, 6 + 5, 0, 6, 'X')

ctext (c, 16, 0.32, 'Indexed Addressing — Index Word')

surface.write_to_png ('fig-020-1b.png')

# fig-022-3

surface, c = create (8, 32, 2, 11)

hline (c,  0, 0,     32)
hline (c,  0, 0 + H, 32)
vline (c,  0, 0, H)
vline (c, 32, 0, H)
c.stroke ()

bfl (c, 0, 6 + 5, 0, 6, 'A - address of this word - 2')

surface.write_to_png ('fig-022-3.png')

# fig-022-5

def dos (c, y):					# double operand skeleton
	hline (c,  0, y,     32)
	hline (c,  0, y + H, 32)

	vline (c,  0, y, H)
	for x in range ( 1,  4):  vline (c, x * 2, y, h)
	vline (c,  8, y, H)
	for x in range ( 5, 11):  vline (c, x * 2, y, h)
	vline (c, 20, y, H)
	for x in range (11, 16):  vline (c, x * 2, y, h)
	vline (c, 32, y, H)

	c.stroke ()

surface, c = create (8, 32, 4, 11)

dos (c, 2)

bfl (c, 2, 16, 12, 4, 'Op Field')
bfl (c, 2, 16,  6, 6, 'Source Address Field')
bfl (c, 2, 16,  0, 6, 'Destination Address Field')

ctext (c, 16, 0.32, 'Instruction Word — Double Operand Instructions')

surface.write_to_png ('fig-022-5.png')

# double operand ops

def dop (path, v, op, name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	y = 1

	hline (c,  0, y,     32)
	hline (c,  0, y + H, 32)

	vline (c,  0, y, H)
	vline (c,  2, y, H / 2.5)
	for x in range ( 2,  4):  vline (c, x * 2, y, h)
	vline (c,  8, y, H)
	for x in range ( 5, 11):  vline (c, x * 2, y, h)
	vline (c, 20, y, H)
	for x in range (11, 16):  vline (c, x * 2, y, h)
	vline (c, 32, y, H)

	c.stroke ()

	bfl (c, y, 16, 15, 1, v)
	bfl (c, y, 16, 12, 3, op)
	bfl (c, y, 16,  6, 6, 'src')
	bfl (c, y, 16,  0, 6, 'dst')

	font_size (c, 1)

	text (c,  0, y + 2.5, name)
	text (c, 16, y + 2.5, syntax, 0.5)
	text (c, 32, y + 2.5, str (time) + ' us', 1.0)

	font_size (c, 0.75)

	ctext (c,  1, 0, 15)
	ctext (c,  7, 0, 12)
	ctext (c,  9, 0, 11)
	ctext (c, 19, 0,  6)
	ctext (c, 21, 0,  5)
	ctext (c, 31, 0,  0)

	surface.write_to_png (path + '.png')

dop ('fig-026-1-mov', 0, 1, 'MOVe',	'MOV src,dst', '2.3')
dop ('fig-026-2-add', 0, 6, 'ADD',	'ADD src,dst', '2.3')
dop ('fig-027-1-sub', 1, 6, 'SUB',	'SUB src,dst', '2.3')
dop ('fig-028-1-cmp', 0, 2, 'CoMPare',	'CMP src,dst', '2.3')
dop ('fig-028-2-bis', 0, 5, 'BIt Set',	'BIS src,dst', '2.3')
dop ('fig-028-3-bic', 0, 4, 'BIt Clear','BIC src,dst', '2.9')
dop ('fig-029-1-bit', 0, 3, 'BIt Test',	'BIT src,dst', '2.9')

# branch ops

def bfs (name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	y = 1
	font_size (c, 1)

	text (c,  0, y + 2.5, name)
	text (c, 16, y + 2.5, syntax, 0.5)
	text (c, 32, y + 2.5, time, 1.0)

	hline (c,  0, y,     32)
	hline (c,  0, y + H, 32)

	vline (c,  0, y, H)
	vline (c, 16, y, H)
	vline (c, 32, y, H)

	for i in range (0, 5):
		vline (c, 2 + 6 * i, y, H / 2.5)
		vline (c, 4 + 6 * i, y, h)
		vline (c, 6 + 6 * i, y, h)

	c.stroke ()

	bfl (c, y, 16,  0, 8, 'offset')

	font_size (c, 0.75)

	ctext (c,  1, 0, 15)
	ctext (c, 15, 0,  8)
	ctext (c, 17, 0,  7)
	ctext (c, 31, 0,  0)

	return surface, c, y

def bxx (path, name, syntax, time):
	surface, c, y = bfs (name, syntax, time)

	bfl (c, y, 16, 8, 8, 'operation code')

	surface.write_to_png (path + '.png')

def bop (path, v, p, q, r, name, syntax, tf, tt):
	time = f'{tt} us' if tf is None else f'{tf} us, {tt} us'

	surface, c, y = bfs (name, syntax, time)

	bfl (c, y, 16, 15, 1, v)
	bfl (c, y, 16, 12, 3, p)
	bfl (c, y, 16,  9, 3, q)
	bfl (c, y, 16,  8, 1, r)

	surface.write_to_png (path + '.png')

bxx ('fig-029-2-bxx', 'Operation', 'Bxx loc', 'Instruction Time')

bop ('fig-029-3-br',   0, 0, 0, 4, 'BRanch (Uncoditional)',	'BR loc', None, 2.6)

bop ('fig-030-1-beq',  0, 0, 1, 4, 'Branch on EQual (Zero)',	'BEQ loc', 1.5, 2.6)
bop ('fig-030-2-bne',  0, 0, 1, 0, 'Branch on Not Equal (Zero)','BNE loc', 1.5, 2.6)
bop ('fig-030-3-bmi',  1, 0, 0, 4, 'Branch on MInus',		'BMI loc', 1.5, 2.6)
bop ('fig-030-4-bpl',  1, 0, 0, 0, 'Branch on PLus',		'BPL loc', 1.5, 2.6)

bop ('fig-031-1-bcs',  1, 0, 3, 4, 'Branch on Carry Set',	'BCS loc', 1.5, 2.6)
bop ('fig-031-2-bcc',  1, 0, 3, 0, 'Branch on Carry Clear',	'BCC loc', 1.5, 2.6)
bop ('fig-031-3-bvs',  1, 0, 2, 4, 'Branch on oVerflow Set',	'BVS loc', 1.5, 2.6)
bop ('fig-031-4-bvc',  1, 0, 2, 0, 'Branch on oVerflow Clear',	'BVC loc', 1.5, 2.6)

bop ('fig-032-3-blt',  0, 0, 2, 4, 'Branch on Less Than (Zero)','BLT loc', 1.5, 2.6)
bop ('fig-032-4-bge',  0, 0, 2, 0, 'Branch on Greater or Equal','BGE loc', 1.5, 2.6)

bop ('fig-033-1-ble',  0, 0, 3, 4, 'Branch on Less or Equal',	'BLE loc', 1.5, 2.6)
bop ('fig-033-2-bgt',  0, 0, 3, 0, 'Branch on Greater Than',	'BGT loc', 1.5, 2.6)
bop ('fig-033-3-bhi',  1, 0, 1, 0, 'Branch on HIgher',		'BHI loc', 1.5, 2.6)
bop ('fig-033-4-blos', 1, 0, 1, 4, 'Branch on Lower or Same',	'BLOS loc', 1.5, 2.6)
bop ('fig-033-5-bhis', 1, 0, 3, 0, 'Branch on Higher or Same',	'BHIS loc', 1.5, 2.6)
bop ('fig-034-1-blo',  1, 0, 3, 4, 'Branch on LOwer',		'BLO loc', 1.5, 2.6)

