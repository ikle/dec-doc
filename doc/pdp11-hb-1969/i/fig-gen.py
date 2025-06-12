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

# fig-014-1

surface, c = create (8, 32, 4, 11)

ticks (c, 0, 2, 'llllll..l.......l')
bfls  (c, 0, 2, [1, 'C', 1, 'V', 1, 'Z', 1, 'N', 1, 'T', 3, 'Priority', 8, 'Unused'])

ctext (c, 16, 0.32, 'Central Processor Status Register (PS)')

write (surface, '014-1')

# fig-019-1

surface, c = create (8, 32, 4, 11)

ticks (c, 0, 2, 'l..l..l.........l')
bfls  (c, 0, 2, [3, 'Register', 3, 'Mode', 10, None])

ctext (c, 16, 0.32, 'Instruction Word')

write (surface, '019-1')

# fig-019-2

surface, c = create (8, 32, 5.2, 11)

ticks (c, 10, 3.2, 'l..l..l')
bfls  (c, 10, 3.2, [3, 'R', 3, 0])

ctext (c, 16, 1.52, 'Address Field — General Register Mode')
ctext (c, 16, 0.32, '(mode is indicated as an octal digit)')

write (surface, '019-2')

# Address Fields

def amode (mode, reg, path, desc):
	surface, c = create (8, 32, 4, 11)

	ticks (c, 10, 2, 'l..l..l')
	bfls  (c, 10, 2, [3, reg, 3, mode])

	ctext (c, 16, 0.32, desc)

	write (surface, path)

amode (1, 'R', '019-3',  'Address Field — Deferred Register Mode')
amode (6, 'R', '020-1a', 'Address Field — Indexed Mode')
amode (7, 'R', '020-2',  'Address Field — Deferred Indexed Mode')
amode (2, 'R', '020-3',  'Address Field — Autoincrement')
amode (3, 'R', '020-4',  'Address Field — Autoincrement Deferred Mode')
amode (4, 'R', '021-1',  'Address Field — Autodecrement')
amode (5, 'R', '021-2',  'Address Field — Autodecrement Deferred Mode')

amode (2, 7, '021-3', 'Address Field — Immediate Mode')
amode (3, 7, '022-1', 'Address Field — Absolute Mode')
amode (6, 7, '022-2', 'Address Field — Relative Mode')
amode (7, 7, '022-4', 'Address Field — Deferred Relative Mode')

# fig-020-1b

surface, c = create (8, 32, 4, 11)

ticks (c, 0, 2, 'l...............l')
bfls  (c, 0, 2, [16, 'X'])

ctext (c, 16, 0.32, 'Indexed Addressing — Index Word')

write (surface, '020-1b')

# fig-022-3

surface, c = create (8, 32, 2, 11)

ticks (c, 0, 0, 'l               l')
bfls  (c, 0, 0, [16, 'A - address of this word - 2'])

write (surface, '022-3')

# fig-022-5

surface, c = create (8, 32, 4, 11)

ticks (c, 0, 2, 'l.....l.....l...l')
bfls  (c, 0, 2, [6, 'Destination Address Field', 6, 'Source Address Field', 4, 'Op Field'])

ctext (c, 16, 0.32, 'Instruction Word — Double Operand Instructions')

write (surface, '022-5')

# double operand ops

def dop (path, v, op, name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	ticks (c, 0, 1, 'l.....l.....l..ol', 'x....xx....xx..x')
	bfls  (c, 0, 1, [6, 'dst', 6, 'src', 3, op, 1, v])
	desc  (c, 0, 1, name, syntax, str (time) + ' us')

	write (surface, path)

dop ('026-1-mov', 0, 1, 'MOVe',		'MOV src,dst', 2.3)
dop ('026-2-add', 0, 6, 'ADD',		'ADD src,dst', 2.3)
dop ('027-1-sub', 1, 6, 'SUB',		'SUB src,dst', 2.3)
dop ('028-1-cmp', 0, 2, 'CoMPare',	'CMP src,dst', 2.3)
dop ('028-2-bis', 0, 5, 'BIt Set',	'BIS src,dst', 2.3)
dop ('028-3-bic', 0, 4, 'BIt Clear',	'BIC src,dst', 2.9)
dop ('029-1-bit', 0, 3, 'BIt Test',	'BIT src,dst', 2.9)

# branch ops

def bxx (path, name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	ticks (c, 0, 1, 'l..o..o.lo..o..ol', 'x......xx......x')
	bfls  (c, 0, 1, [8, 'offset', 8, 'operation code'])
	desc  (c, 0, 1, name, syntax, time)

	write (surface, path)

def bop (path, v, p, q, r, name, syntax, tf, tt):
	time = f'{tt} us' if tf is None else f'{tf} us, {tt} us'

	surface, c = create (8, 32, 4.3, 11)

	ticks (c, 0, 1, 'l..o..o.lo..o..ol', 'x......xx......x')
	bfls  (c, 0, 1, [8, 'offset', 1, r, 3, q, 3, p, 1, v])
	desc  (c, 0, 1, name, syntax, time)

	write (surface, path)

def top (path, v, p, q, r, name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	ticks (c, 0, 1, 'l..o..o.lo..o..ol', 'x......xx......x')
	bfls  (c, 0, 1, [8, 'xxx', 1, r, 3, q, 3, p, 1, v])
	desc  (c, 0, 1, name, syntax, time)

	write (surface, path)

bxx ('029-2-bxx', 'Operation', 'Bxx loc', 'Instruction Time')

bop ('029-3-br',   0, 0, 0, 4, 'BRanch (Uncoditional)',		'BR loc', None, 2.6)

bop ('030-1-beq',  0, 0, 1, 4, 'Branch on EQual (Zero)',	'BEQ loc', 1.5, 2.6)
bop ('030-2-bne',  0, 0, 1, 0, 'Branch on Not Equal (Zero)',	'BNE loc', 1.5, 2.6)
bop ('030-3-bmi',  1, 0, 0, 4, 'Branch on MInus',		'BMI loc', 1.5, 2.6)
bop ('030-4-bpl',  1, 0, 0, 0, 'Branch on PLus',		'BPL loc', 1.5, 2.6)

bop ('031-1-bcs',  1, 0, 3, 4, 'Branch on Carry Set',		'BCS loc', 1.5, 2.6)
bop ('031-2-bcc',  1, 0, 3, 0, 'Branch on Carry Clear',		'BCC loc', 1.5, 2.6)
bop ('031-3-bvs',  1, 0, 2, 4, 'Branch on oVerflow Set',	'BVS loc', 1.5, 2.6)
bop ('031-4-bvc',  1, 0, 2, 0, 'Branch on oVerflow Clear',	'BVC loc', 1.5, 2.6)

bop ('032-3-blt',  0, 0, 2, 4, 'Branch on Less Than (Zero)',	'BLT loc', 1.5, 2.6)
bop ('032-4-bge',  0, 0, 2, 0, 'Branch on Greater or Equal',	'BGE loc', 1.5, 2.6)

bop ('033-1-ble',  0, 0, 3, 4, 'Branch on Less or Equal',	'BLE loc', 1.5, 2.6)
bop ('033-2-bgt',  0, 0, 3, 0, 'Branch on Greater Than',	'BGT loc', 1.5, 2.6)
bop ('033-3-bhi',  1, 0, 1, 0, 'Branch on HIgher',		'BHI loc', 1.5, 2.6)
bop ('033-4-blos', 1, 0, 1, 4, 'Branch on Lower or Same',	'BLOS loc', 1.5, 2.6)
bop ('033-5-bhis', 1, 0, 3, 0, 'Branch on Higher or Same',	'BHIS loc', 1.5, 2.6)
bop ('034-1-blo',  1, 0, 3, 4, 'Branch on LOwer',		'BLO loc', 1.5, 2.6)

# single operand ops

def sop (path, v, p, q, r, name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	ticks (c, 0, 1, 'l..o..l..o..o..ol', 'x....xx........x')
	bfls  (c, 0, 1, [6, 'dst', 3, r, 3, q, 3, p, 1, v])
	desc  (c, 0, 1, name, syntax, f'{time} us')

	write (surface, path)

sop ('034-2-jmp', 0, 0, 0, 1, 'JuMP', 'JMP dst', 1.2)

# register double operand ops

def rdop (path, v, p, q, name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	ticks (c, 0, 1, 'l..o..l..l..o..ol', 'x....xx.xx.....x')
	bfls  (c, 0, 1, [6, 'dst', 3, 'reg', 3, q, 3, p, 1, v])
	desc  (c, 0, 1, name, syntax, f'{time} us')

	write (surface, path)

rdop ('035-1-jsr', 0, 0, 4, 'Jump to SubRoutine', 'JSR reg,dst', 4.2)

# register single operand ops

def rsop (path, v, p, q, r, s, name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	ticks (c, 0, 1, 'l..l..o..o..o..ol', 'x.xx...........x')
	bfls  (c, 0, 1, [3, 'reg', 3, s, 3, r, 3, q, 3, p, 1, v])
	desc  (c, 0, 1, name, syntax, f'{time} us')

	write (surface, path)

rsop ('036-1-rts', 0, 0, 0, 2, 0, 'ReTurn from Subroutine', 'RTS reg', 3.5)

# fig-039-1-sop

surface, c = create (8, 32, 4.3, 11)

ticks (c, 0, 1, 'l..o..l..o..o..ol', 'x....xx........x')
bfls  (c, 0, 1, [6, 'dst', 10, 'operation code'])
desc  (c, 0, 1, 'OPeRation', 'OPR dst', 'Instruction Time')

write (surface, '039-1-sop')

sop ('039-2-clr', 0, 0, 5, 0, 'CLeaR',			'CLR dst', 2.3)
sop ('039-3-inc', 0, 0, 5, 2, 'INCrement',		'INC dst', 2.3)

sop ('040-1-dec', 0, 0, 5, 3, 'DECrement',		'DEC dst', 2.3)
sop ('040-2-neg', 0, 0, 5, 4, 'NEGate',			'NEG dst', 2.3)
sop ('040-3-tst', 0, 0, 5, 7, 'TeST',			'TST dst', 2.3)
sop ('040-4-com', 0, 0, 5, 1, 'COMplement',		'COM dst', 2.3)

sop ('041-1-adc', 0, 0, 5, 5, 'ADd Carry',		'ADC dst', 2.3)
sop ('041-2-sbc', 0, 0, 5, 6, 'SuBstract Carry',	'SBC dst', 2.3)

sop ('042-2-ror',  0, 0, 6, 0, 'ROtate Right',		'ROR dst', 2.3)
sop ('042-3-rol',  0, 0, 6, 1, 'ROtate Left',		'ROL dst', 2.3)
sop ('042-4-swab', 0, 0, 0, 3, 'SWAp Bytes',		'SWAB dst', 2.3)

sop ('043-1-asr', 0, 0, 6, 2, 'Arithmetic Shift Right',	'ASR dst', 2.3)
sop ('043-2-asl', 0, 0, 6, 3, 'Arithmetic Shift Left',	'ASL dst', 2.3)

dop ('044-1-movb', 1, 1, 'MOVe Byte',		'MOVB src,dst', 2.3)
dop ('045-1-cmpb', 1, 2, 'CoMPare Byte',	'CMPB src,dst', 2.3)
dop ('045-2-bisb', 1, 5, 'BIt Set Byte',	'BISB src,dst', 2.3)
dop ('045-3-bicb', 1, 4, 'BIt Clear Byte',	'BICB src,dst', 2.3)
dop ('045-4-bitb', 1, 3, 'BIt Test Byte',	'BITB src,dst', 2.3)

sop ('046-1-clrb', 1, 0, 5, 0, 'CLeaR Byte',			'CLRB dst', 2.3)
sop ('046-2-incb', 1, 0, 5, 2, 'INCrement Byte',		'INCB dst', 2.3)
sop ('046-3-decb', 1, 0, 5, 3, 'DECrement Byte',		'DECB dst', 2.3)
sop ('047-1-negb', 1, 0, 5, 4, 'NEGate Byte',			'NEGB dst', 2.3)
sop ('047-2-tstb', 1, 0, 5, 7, 'TeST Byte',			'TSTB dst', 2.3)
sop ('047-3-comb', 1, 0, 5, 1, 'COMplement Byte',		'COMB dst', 2.3)
sop ('047-4-adcb', 1, 0, 5, 5, 'ADd Carry Byte',		'ADCB dst', 2.3)
sop ('047-5-sbcb', 1, 0, 5, 6, 'SuBstract Carry Byte',		'SBCB dst', 2.3)
sop ('047-6-rorb', 1, 0, 6, 0, 'ROtate Right Byte',		'RORB dst', 2.3)
sop ('048-1-rolb', 1, 0, 6, 1, 'ROtate Left Byte',		'ROLB dst', 2.3)
sop ('048-2-asrb', 1, 0, 6, 2, 'Arithmetic Shift Right Byte',	'ASRB dst', 2.3)
sop ('048-3-aslb', 1, 0, 6, 3, 'Arithmetic Shift Left Byte',	'ASLB dst', 2.3)

# fig-048-4-ccop

surface, c = create (8, 32, 4.3, 11)

ticks (c, 0, 1, 'lllllll..o..o..ol', 'xxxxxxx........x')
bfls  (c, 0, 1, [1, 'C', 1, 'V', 1, 'Z', 1, 'N', 1, 'S/C', 1, 4, 3, 2, 3, 0, 3, 0, 1, 0])
desc  (c, 0, 1, 'Condition Code Operators', None, '1.5 us')

write (surface, '048-4-ccop')

# Misc Control Instructions

def mop (path, v, p, q, r, s, t, name, syntax, time):
	surface, c = create (8, 32, 4.3, 11)

	ticks (c, 0, 1, 'l..o..o..o..o..ol', 'x..............x')
	bfls  (c, 0, 1, [3, t, 3, s, 3, r, 3, q, 3, p, 1, v])
	desc  (c, 0, 1, name, syntax, f'{time} us')

	write (surface, path)

mop ('049-1-reset', 0, 0, 0, 0, 0, 5, 'RESet ExTernal bus',	'RESET',    20)
mop ('049-2-wait',  0, 0, 0, 0, 0, 1, 'WAit for InterrupT',	'WAIT',     1.8)
mop ('049-3-halt',  0, 0, 0, 0, 0, 0, 'HALT',			'HALT',     1.8)

top ('050-1-emt',   1, 0, 4, 0, 'EMulator Trap',		'EMT xxx',  8.9)
top ('050-2-trap',  1, 0, 4, 4, 'TRAP',				'TRAP xxx', 8.9)

mop ('050-3-iot',   0, 0, 0, 0, 0, 4, 'I/O Trap',		'IOT',      8.9)
mop ('050-4-bpt',   0, 0, 0, 0, 0, 3, 'No defined mnemonic',	'000003',   8.9)
mop ('051-1-rti',   0, 0, 0, 0, 0, 2, 'ReTurn from Interrupt',	'RTI',      4.8)

