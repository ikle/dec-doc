#!/usr/bin/python3
#
# Figure Generator for EC-H1689-10-1992
#
# Copyright (c) 2021-2024 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import cairo

fonts = ["Liberation Sans", "Cantarell", "Fontin Sans CR", "Latin Modern Sans"]

def font_size (c, size, right = True):
	xx = size
	yy = -size if right else size

	c.set_font_matrix (cairo.Matrix (xx, 0, 0, yy, 0, 0))

def create (M, W, H, S = 20, step = 1, right = True, grid = True):
	SW, SH = W * S, H * S
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

	c.select_font_face (fonts[1])

	return surface, c

def draw_line (c, x0, y0, x1, y1):
	c.move_to (x0, y0)
	c.line_to (x1, y1)

def draw_text (c, x, y, text):
	c.move_to (x, y)
	c.show_text (text)

# Fig 1-1

surface, c = create (8, 40, 9, 11, 1, True, False)

draw_line (c, 0,  0, 32, 0)
draw_line (c, 0,  2, 32, 2)
draw_line (c, 0,  4, 32, 4)
draw_line (c, 0,  6, 32, 6)
draw_line (c, 0,  8, 32, 8)

draw_line (c,  0, 0,  0, 8)
draw_line (c,  6, 0,  6, 8)
draw_line (c, 11, 0, 11, 6)
draw_line (c, 16, 0, 16, 4)
draw_line (c, 27, 0, 27, 2)
draw_line (c, 32, 0, 32, 8)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 8.25, "31")
draw_text (c,  5, 8.25, "26")
draw_text (c,  6, 8.25, "25")
draw_text (c, 10, 8.25, "21")
draw_text (c, 11, 8.25, "20")
draw_text (c, 15, 8.25, "16")
draw_text (c, 16, 8.25, "15")
draw_text (c, 26, 8.25, "  5")
draw_text (c, 27, 8.25, "  4")
draw_text (c, 31, 8.25, "  0")

font_size (c, 1)

draw_text (c,  1.1, 0.64, "Opcode")
draw_text (c,  1.1, 2.64, "Opcode")
draw_text (c,  1.1, 4.64, "Opcode")
draw_text (c,  1.1, 6.64, "Opcode")

draw_text (c,  7.8, 0.64, "RA")
draw_text (c,  7.8, 2.64, "RA")
draw_text (c,  7.8, 4.64, "RA")
draw_text (c, 17.0, 6.64, "Number")

draw_text (c, 12.8, 0.64, "RB")
draw_text (c, 12.8, 2.64, "RB")
draw_text (c, 20.4, 4.64, "Disp")

draw_text (c, 19.4, 0.64, "Function")
draw_text (c, 22.9, 2.64, "Disp")

draw_text (c, 28.8, 0.64, "RC")

draw_text (c, 32.5, 0.64, "Operate Format")
draw_text (c, 32.5, 2.64, "Memory Format")
draw_text (c, 32.5, 4.64, "Branch Format")
draw_text (c, 32.5, 6.64, "PALcode Format")

surface.write_to_png ("fig-1-1.png")

# Fig 2-1

surface, c = create (8, 10, 5, 11, 1, True, False)

draw_line (c, 0,  0,  8, 0)
draw_line (c, 0,  4,  8, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  8, 0,  8, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "7")
draw_text (c,  7, 4.25, "  0")

font_size (c, 1)

draw_text (c,  8.5, 1.64, ":A")

surface.write_to_png ("fig-2-1.png")

# Fig 2-2

surface, c = create (8, 18, 5, 11, 1, True, False)

draw_line (c, 0,  0, 16, 0)
draw_line (c, 0,  4, 16, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c, 16, 0, 16, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "15")
draw_text (c, 15, 4.25, "  0")

font_size (c, 1)

draw_text (c,  16.5, 1.64, ":A")

surface.write_to_png ("fig-2-2.png")

# Fig 2-3

surface, c = create (8, 34, 5, 11, 1, True, False)

draw_line (c, 0,  0, 32, 0)
draw_line (c, 0,  4, 32, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c, 32, 0, 32, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "31")
draw_text (c, 31, 4.25, "  0")

font_size (c, 1)

draw_text (c,  32.5, 1.64, ":A")

surface.write_to_png ("fig-2-3.png")

# Fig 2-4

surface, c = create (8, 66, 5, 11, 1, True, False)

draw_line (c, 0,  0, 64, 0)
draw_line (c, 0,  4, 64, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c, 64, 0, 64, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "63")
draw_text (c, 63, 4.25, "  0")

font_size (c, 1)

draw_text (c,  64.5, 1.64, ":A")

surface.write_to_png ("fig-2-4.png")

# Fig 2-5

surface, c = create (8, 19, 5, 11, 1, True, False)

draw_line (c, 0,  0, 16, 0)
draw_line (c, 0,  2, 16, 2)
draw_line (c, 0,  4, 16, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  1, 2,  1, 4)
draw_line (c,  9, 2,  9, 4)
draw_line (c, 16, 0, 16, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "15")
draw_text (c,  1, 4.25, "14")
draw_text (c,  8, 4.25, "  7")
draw_text (c,  9, 4.25, "6")
draw_text (c, 15, 4.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 2.64, "S")
draw_text (c,  4.1, 2.64, "Exp.")
draw_text (c, 10.8, 2.64, "Frac. Hi")
draw_text (c,  5.5, 0.64, "Fraction Lo")

draw_text (c,  16.5, 0.64, ":A+2")
draw_text (c,  16.5, 2.64, ":A")

surface.write_to_png ("fig-2-5.png")

# Fig 2-6

surface, c = create (8, 66, 5, 11, 1, True, False)

draw_line (c, 0,  0, 64, 0)
draw_line (c, 0,  4, 64, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  1, 0,  1, 4)
draw_line (c, 12, 0, 12, 4)
draw_line (c, 19, 0, 19, 4)
draw_line (c, 35, 0, 35, 4)
draw_line (c, 64, 0, 64, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "63")
draw_text (c,  1, 4.25, "62")
draw_text (c, 11, 4.25, "52")
draw_text (c, 12, 4.25, "51")
draw_text (c, 18, 4.25, "45")
draw_text (c, 19, 4.25, "44")
draw_text (c, 34, 4.25, "29")
draw_text (c, 35, 4.25, "28")
draw_text (c, 63, 4.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 1.64, "S")
draw_text (c,  5.7, 1.64, "Exp.")
draw_text (c, 13.8, 1.64, "Frac. Hi")
draw_text (c, 24.5, 1.64, "Fraction Lo")
draw_text (c, 48.8, 1.64, "0")

draw_text (c,  64.5, 1.64, ":Fx")

surface.write_to_png ("fig-2-6.png")

# Fig 2-7

surface, c = create (8, 19, 9, 11, 1, True, False)

draw_line (c, 0,  0, 16, 0)
draw_line (c, 0,  2, 16, 2)
draw_line (c, 0,  4, 16, 4)
draw_line (c, 0,  6, 16, 6)
draw_line (c, 0,  8, 16, 8)

draw_line (c,  0, 0,  0, 8)
draw_line (c,  1, 6,  1, 8)
draw_line (c, 12, 6, 12, 8)
draw_line (c, 16, 0, 16, 8)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 8.25, "15")
draw_text (c,  1, 8.25, "14")
draw_text (c, 11, 8.25, "  4")
draw_text (c, 12, 8.25, "3")
draw_text (c, 15, 8.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 6.64, "S")
draw_text (c,  5.6, 6.64, "Exp.")
draw_text (c, 12.3, 6.64, "Frac. Hi")
draw_text (c,  5.0, 4.64, "Fraction Midh")
draw_text (c,  5.1, 2.64, "Fraction Midl")
draw_text (c,  5.5, 0.64, "Fraction Lo")

draw_text (c,  16.5, 6.64, ":A")
draw_text (c,  16.5, 4.64, ":A+2")
draw_text (c,  16.5, 2.64, ":A+4")
draw_text (c,  16.5, 0.64, ":A+6")

surface.write_to_png ("fig-2-7.png")

# Fig 2-8

surface, c = create (8, 66, 5, 11, 1, True, False)

draw_line (c, 0,  0, 64, 0)
draw_line (c, 0,  4, 64, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  1, 0,  1, 4)
draw_line (c, 12, 0, 12, 4)
draw_line (c, 16, 0, 16, 4)
draw_line (c, 32, 0, 32, 4)
draw_line (c, 48, 0, 48, 4)
draw_line (c, 64, 0, 64, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "63")
draw_text (c,  1, 4.25, "62")
draw_text (c, 11, 4.25, "52")
draw_text (c, 12, 4.25, "51")
draw_text (c, 15, 4.25, "48")
draw_text (c, 16, 4.25, "47")
draw_text (c, 31, 4.25, "32")
draw_text (c, 32, 4.25, "31")
draw_text (c, 47, 4.25, "16")
draw_text (c, 48, 4.25, "15")
draw_text (c, 63, 4.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 1.64, "S")
draw_text (c,  5.7, 1.64, "Exp.")
draw_text (c, 12.3, 1.64, "Frac. Hi")
draw_text (c, 21.0, 1.64, "Fraction Midh")
draw_text (c, 37.1, 1.64, "Fraction Midl")
draw_text (c, 53.5, 1.64, "Fraction Lo")

draw_text (c,  64.5, 1.64, ":Fx")

surface.write_to_png ("fig-2-8.png")

# Fig 2-9

surface, c = create (8, 19, 9, 11, 1, True, False)

draw_line (c, 0,  0, 16, 0)
draw_line (c, 0,  2, 16, 2)
draw_line (c, 0,  4, 16, 4)
draw_line (c, 0,  6, 16, 6)
draw_line (c, 0,  8, 16, 8)

draw_line (c,  0, 0,  0, 8)
draw_line (c,  1, 6,  1, 8)
draw_line (c,  9, 6,  9, 8)
draw_line (c, 16, 0, 16, 8)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 8.25, "15")
draw_text (c,  1, 8.25, "14")
draw_text (c,  8, 8.25, "  7")
draw_text (c,  9, 8.25, "6")
draw_text (c, 15, 8.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 6.64, "S")
draw_text (c,  4.1, 6.64, "Exp.")
draw_text (c, 10.8, 6.64, "Frac. Hi")
draw_text (c,  5.0, 4.64, "Fraction Midh")
draw_text (c,  5.1, 2.64, "Fraction Midl")
draw_text (c,  5.5, 0.64, "Fraction Lo")

draw_text (c,  16.5, 6.64, ":A")
draw_text (c,  16.5, 4.64, ":A+2")
draw_text (c,  16.5, 2.64, ":A+4")
draw_text (c,  16.5, 0.64, ":A+6")

surface.write_to_png ("fig-2-9.png")

# Fig 2-10

surface, c = create (8, 66, 5, 11, 1, True, False)

draw_line (c, 0,  0, 64, 0)
draw_line (c, 0,  4, 64, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  1, 0,  1, 4)
draw_line (c,  9, 0,  9, 4)
draw_line (c, 16, 0, 16, 4)
draw_line (c, 32, 0, 32, 4)
draw_line (c, 48, 0, 48, 4)
draw_line (c, 64, 0, 64, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "63")
draw_text (c,  1, 4.25, "62")
draw_text (c,  8, 4.25, "55")
draw_text (c,  9, 4.25, "54")
draw_text (c, 15, 4.25, "48")
draw_text (c, 16, 4.25, "47")
draw_text (c, 31, 4.25, "32")
draw_text (c, 32, 4.25, "31")
draw_text (c, 47, 4.25, "16")
draw_text (c, 48, 4.25, "15")
draw_text (c, 63, 4.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 1.64, "S")
draw_text (c,  4.1, 1.64, "Exp.")
draw_text (c, 10.8, 1.64, "Frac. Hi")
draw_text (c, 21.0, 1.64, "Fraction Midh")
draw_text (c, 37.1, 1.64, "Fraction Midl")
draw_text (c, 53.5, 1.64, "Fraction Lo")

draw_text (c,  64.5, 1.64, ":Fx")

surface.write_to_png ("fig-2-10.png")

# Fig 2-11

surface, c = create (8, 19, 5, 11, 1, True, False)

draw_line (c, 0,  0, 16, 0)
draw_line (c, 0,  2, 16, 2)
draw_line (c, 0,  4, 16, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  1, 0,  1, 2)
draw_line (c,  9, 0,  9, 2)
draw_line (c, 16, 0, 16, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "15")
draw_text (c,  1, 4.25, "14")
draw_text (c,  8, 4.25, "  7")
draw_text (c,  9, 4.25, "6")
draw_text (c, 15, 4.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 0.64, "S")
draw_text (c,  4.1, 0.64, "Exp.")
draw_text (c, 10.8, 0.64, "Frac. Hi")
draw_text (c,  5.5, 2.64, "Fraction Lo")

draw_text (c,  16.5, 0.64, ":A+2")
draw_text (c,  16.5, 2.64, ":A")

surface.write_to_png ("fig-2-11.png")

# Fig 2-12 same as fig 2-6

# Fig 2-13

surface, c = create (8, 19, 9, 11, 1, True, False)

draw_line (c, 0,  0, 16, 0)
draw_line (c, 0,  2, 16, 2)
draw_line (c, 0,  4, 16, 4)
draw_line (c, 0,  6, 16, 6)
draw_line (c, 0,  8, 16, 8)

draw_line (c,  0, 0,  0, 8)
draw_line (c,  1, 0,  1, 2)
draw_line (c, 12, 0, 12, 2)
draw_line (c, 16, 0, 16, 8)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 8.25, "15")
draw_text (c,  1, 8.25, "14")
draw_text (c, 11, 8.25, "  4")
draw_text (c, 12, 8.25, "3")
draw_text (c, 15, 8.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 0.64, "S")
draw_text (c,  5.6, 0.64, "Exp.")
draw_text (c, 12.3, 0.64, "Frac. Hi")
draw_text (c,  5.0, 2.64, "Fraction Midh")
draw_text (c,  5.1, 4.64, "Fraction Midl")
draw_text (c,  5.5, 6.64, "Fraction Lo")

draw_text (c,  16.5, 6.64, ":A")
draw_text (c,  16.5, 4.64, ":A+2")
draw_text (c,  16.5, 2.64, ":A+4")
draw_text (c,  16.5, 0.64, ":A+6")

surface.write_to_png ("fig-2-13.png")

# Fig 2-14 same as fig 2-8

# Fig 2-15

surface, c = create (8, 19, 5, 11, 1, True, False)

draw_line (c, 0,  0, 16, 0)
draw_line (c, 0,  2, 16, 2)
draw_line (c, 0,  4, 16, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  1, 0,  1, 2)
draw_line (c, 16, 0, 16, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "15")
draw_text (c,  1, 4.25, "14")
draw_text (c, 15, 4.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 0.64, "S")
draw_text (c,  6.3, 0.64, "Integer Hi")
draw_text (c,  5.8, 2.64, "Integer Lo")

draw_text (c,  16.5, 0.64, ":A+2")
draw_text (c,  16.5, 2.64, ":A")

surface.write_to_png ("fig-2-15.png")

# Fig 2-16

surface, c = create (8, 66, 5, 11, 1, True, False)

draw_line (c, 0,  0, 64, 0)
draw_line (c, 0,  4, 64, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  1, 0,  1, 4)
draw_line (c,  2, 0,  2, 4)
draw_line (c,  5, 0,  5, 4)
draw_line (c, 19, 0, 19, 4)
draw_line (c, 35, 0, 35, 4)
draw_line (c, 64, 0, 64, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "63")
draw_text (c,  1, 4.25, "62")
draw_text (c,  2, 4.25, "61")
draw_text (c,  4, 4.25, "59")
draw_text (c,  5, 4.25, "58")
draw_text (c, 18, 4.25, "45")
draw_text (c, 19, 4.25, "44")
draw_text (c, 34, 4.25, "29")
draw_text (c, 35, 4.25, "28")
draw_text (c, 63, 4.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 1.64, "S")
draw_text (c,  1.4, 1.64, "I")
draw_text (c,  2.8, 1.64, "xxx")
draw_text (c,  9.8, 1.64, "Integer Hi")
draw_text (c, 24.8, 1.64, "Integer Lo")
draw_text (c, 48.8, 1.64, "0")

draw_text (c,  64.5, 1.64, ":Fx")

surface.write_to_png ("fig-2-16.png")

# Fig 2-17

surface, c = create (8, 19, 9, 11, 1, True, False)

draw_line (c, 0,  0, 16, 0)
draw_line (c, 0,  2, 16, 2)
draw_line (c, 0,  4, 16, 4)
draw_line (c, 0,  6, 16, 6)
draw_line (c, 0,  8, 16, 8)

draw_line (c,  0, 0,  0, 8)
draw_line (c,  1, 0,  1, 2)
draw_line (c, 16, 0, 16, 8)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 8.25, "15")
draw_text (c,  1, 8.25, "14")
draw_text (c, 15, 8.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 0.64, "S")
draw_text (c,  6.3, 0.64, "Integer Hi")
draw_text (c,  5.2, 2.64, "Integer Midh")
draw_text (c,  5.4, 4.64, "Integer Midl")
draw_text (c,  5.8, 6.64, "Integer Lo")

draw_text (c,  16.5, 6.64, ":A")
draw_text (c,  16.5, 4.64, ":A+2")
draw_text (c,  16.5, 2.64, ":A+4")
draw_text (c,  16.5, 0.64, ":A+6")

surface.write_to_png ("fig-2-17.png")

# Fig 2-18

surface, c = create (8, 66, 5, 11, 1, True, False)

draw_line (c, 0,  0, 64, 0)
draw_line (c, 0,  4, 64, 4)

draw_line (c,  0, 0,  0, 4)
draw_line (c,  1, 0,  1, 4)
draw_line (c, 16, 0, 16, 4)
draw_line (c, 32, 0, 32, 4)
draw_line (c, 48, 0, 48, 4)
draw_line (c, 64, 0, 64, 4)

c.stroke ()

font_size (c, 0.75)

draw_text (c,  0, 4.25, "63")
draw_text (c,  1, 4.25, "62")
draw_text (c, 15, 4.25, "48")
draw_text (c, 16, 4.25, "47")
draw_text (c, 31, 4.25, "32")
draw_text (c, 32, 4.25, "31")
draw_text (c, 47, 4.25, "16")
draw_text (c, 48, 4.25, "15")
draw_text (c, 63, 4.25, "  0")

font_size (c, 1)

draw_text (c,  0.2, 1.64, "S")
draw_text (c,  6.3, 1.64, "Integer Hi")
draw_text (c, 21.2, 1.64, "Integer Midh")
draw_text (c, 37.4, 1.64, "Integer Midl")
draw_text (c, 53.8, 1.64, "Integer Lo")

draw_text (c,  64.5, 1.64, ":Fx")

surface.write_to_png ("fig-2-18.png")

