# Chapter 2 · Basic Architecture

## Addressing

The basic addressable unit in Alpha is the 8-bit byte. Virtual addresses are
64 bits long. An implementation may support a smaller virtual address space.
The minimum virtual address size is 43 bits.

Virtual addresses as seen by the program are translated into physical memory
addresses by the memory management mechanism.

## Data Types

Following are descriptions of the Alpha architecture data types.

### Byte

A byte is 8 contiguous bits starting on an addressable byte boundary. The
bits are numbered from right to left, 0 through 7, as shown in Figure 2-1.

_Figure 2-1 • Byte Format_

A byte is specified by its address A. A byte is an 8-bit value. The byte is
only supported in Alpha by the extract, mask, insert, and zap instructions.

### Word

A word is 2 contiguous bytes starting on an arbitrary byte boundary. The bits
are numbered from right to left, 0 through 15, as shown in Figure 2-2.

_Figure 2-2 • Word Format_

A word is specified by its address, the address of the byte containing bit 0.

A word is a 16-bit value. The word is only supported in Alpha by the extract,
mask, and insert instructions.

### Longword

A longword is 4 contiguous bytes starting on an arbitrary byte boundary. The
bits are numbered from right to left, 0 through 31, as shown in Figure 2-3.

_Figure 2-3 • Longword Format_

A longword is specified by its address A, the address of the byte containing
bit 0. A longword is a 32-bit value.

When interpreted arithmetically, a longword is a two's-complement integer
with bits of increasing significance from 0 through 30. Bit 31 is the sign
bit. The longword is only supported in Alpha by sign-extended load and store
instructions and by longword arithmetic instructions.

> #### Note
>
> Alpha implementations will impose a significant performance penalty when
> accessing longword operands that are not naturally aligned. (A naturally
> aligned longword has zero as the low-order two bits of its address.)

### Quadword

A quadword is 8 contiguous bytes starting on an arbitrary byte boundary. The
bits are numbered from right to left, 0 through 63, as shown in Figure 2-4.

_Figure 2-4 • Quadword Format_

A quadword is specified by its address A, the address of the byte containing
bit 0. A quadword is a 64-bit value. When interpreted arithmetically, a
quadword is either a two's-complement integer with bits of increasing
significance from 0 through 62 and bit 63 as the sign bit, or an unsigned
integer with bits of increasing significance from 0 through 63.

> #### Note
>
> Alpha implementations will impose a significant performance penalty when
> accessing quadword operands that are not naturally aligned. (A naturally
> aligned quadword has zero as the low-order three bits of its address.)

### VAX Floating-Point Formats

VAX floating-point numbers are stored in one set of formats in memory and in
a second set of formats in registers. The floating-point load and store
instructions convert between these formats purely by rearranging bits; no
rounding or range-checking is done by the load and store instructions.

#### F-floating

An F_floating datum is 4 contiguous bytes in memory starting on an arbitrary
byte boundary. The bits are labeled from right to left, 0 through 31, as
shown in Figure 2-5.

_Figure 2-5 • F_floating Datum_

An F_floating operand occupies 64 bits in a floating register, left-justified
in the 64-bit register, as shown in Figure 2-6.

_Figure 2-6 • F_floating Register Format_

The F_floating load instruction reorders bits on the way in from memory,
expands the exponent from 8 to 11 bits, and sets the low-order fraction bits
to zero. This produces in the register an equivalent G_floating number
suitable for either F_floating or G_floating operations. The mapping from
8-bit memory-format exponents to 11-bit register-format exponents is shown in
Table 2-1.

_Table 2·1 • F_floating Load Exponent Mapping_

| Memory <14:7> | Register <62:52>                       |
| ------------- | -------------------------------------- |
| 1 1111111     | 1 000 1111111                          |
| 1 xxxxxxx     | 1 000 xxxxxxx    (xxxxxxx not all 1's) |
| 0 xxxxxxx     | 0 111 xxxxxxx    (xxxxxxx not all 0's) |
| 0 0000000     | 0 000 0000000                          |

This mapping preserves both normal values and exceptional values.

The F_floating store instruction reorders register bits on the way to memory
and does no checking of the low-order fraction bits. Register bits <61:59>
and <28:0> are ignored by the store instruction.

An F_floating datum is specified by its address A, the address of the byte
containing bit 0. The memory form of an F_floating datum is sign magnitude
with bit 15 the sign bit, bits <14:7> an excess-128 binary exponent, and bits
<6:0> and <31:16> a normalized 24-bit fraction with the redundant most
significant fraction bit not represented. Within the fraction, bits of
increasing significance are from 16 through 31 and 0 through 6. The 8-bit
exponent field encodes the values 0 through 255. An exponent value of 0,
together with a sign bit of 0, is taken to indicate that the F_floating datum
has a value of 0.

If the result of a VAX floating-point format instruction has a value of zero,
the instruction always produces a datum with a sign bit of 0, an exponent of
0, and all fraction bits of 0. Exponent values of 1..255 indicate true binary
exponents of -127..127. An exponent value of 0, together with a sign bit of
1, is taken as a reserved operand. Floating-point instructions processing a
reserved operand take an arithmetic exception. The value of an F_floating
datum is in the approximate range 0.29\*10\*\*-38..1.7\*10\*\*38. The
precision of an F_floating datum is approximately one part in 2\*\*23,
typically 7 decimal digits.

> #### Note
>
> Alpha implementations will impose a significant performance penalty when
> accessing F_floating operands that are not naturally aligned. (A naturally
> aligned F_floating datum has zero as the low-order two bits of its
> address.)

#### G_floating

A G_floating datum in memory is 8 contiguous bytes starting on an arbitrary
byte boundary. The bits are labeled from right to left, 0 through 63, as
shown in Figure 2-7.

_Figure 2-7 • G_floating Datum_

A G_floating operand occupies 64 bits in a floating register, arranged as
shown in Figure 2-8.

_Figure 2-8 • G_floating Format_

A G_floating datum is specified by its address A, the address of the byte
containing bit 0. The form of a G_floating datum is sign magnitude with bit
15 the sign bit, bits <14:4> an excess-1024 binary exponent, and bits <3:0>
and <63:16> a normalized 53-bit fraction with the redundant most significant
fraction bit not represented. Within the fraction, bits of increasing
significance are from 48 through 63, 32 through 47, 16 through 31, and 0
through 3. The 11-bit exponent field encodes the values 0 through 2047. An
exponent value of 0, together with a sign bit of 0, is taken to indicate that
the G_floating datum has a value of 0.

If the result of a floating-point instruction has a value of zero, the
instruction always produces a datum with a sign bit of 0, an exponent of 0,
and all fraction bits of 0. Exponent values of 1..2047 indicate true binary
exponents of -1023..1023. An exponent value of 0, together with a sign bit of
1, is taken as a reserved operand. Floating-point instructions processing a
reserved operand take a user-visible arithmetic exception. The value of a
G_floating datum is in the approximate range
0.56\*10\*\*-308..0.9\*10\*\*308. The precision of a G_floating datum is
approximately one part in 2\*\*52, typically 15 decimal digits.

> #### Note
>
> Alpha implementations will impose a significant performance penalty when
> accessing G_floating operands that are not naturally aligned. (A naturally
> aligned G_floating datum has zero as the low-order three bits of its
> address.)

#### D_floating

A D_floating datum in memory is 8 contiguous bytes starting on an arbitrary
byte boundary. The bits are labeled from right to left, 0 through 63, as
shown in Figure 2-9.

_Figure 2-9 • D_floating Datum_

A D_floating operand occupies 64 bits in a floating register, arranged as
shown in Figure 2-10.

_Figure 2-10 • D_floating Register Format_

The reordering of bits required for a D_floating load or store are identical
to those required for a G_floating load or store. The G_floating load and
store instructions are therefore used for loading or storing D_floating data.

A D_floating datum is specified by its address A, the address of the byte
containing bit 0. The memory form of a D_floating datum is identical to an
F_floating datum except for 32 additional low significance fraction bits.
Within the fraction, bits of increasing significance are from 48 through 63,
32 through 47, 16 through 31, and 0 through 6. The exponent conventions and
approximate range of values is the same for D_floating as F_floating. The
precision of a D_floating datum is approximately one part in 2\*\*55,
typically 16 decimal digits.

> #### Note
>
> D_floating is not a fully supported data type; no D_floating arithmetic
> operations are provided in the architecture. For backward compatibility,
> exact D_floating arithmetic may be provided via software emulation.
> D_floating “format compatibility” in which binary files of D_floating
> numbers may be processed, but without the last 3 bits of fraction
> precision, can be obtained via conversions to G_floating, G arithmetic
> operations, then conversion back to D_floating.

> #### Note
>
> Alpha implementations will impose a significant performance penalty on
> access to D_floating operands that are not naturally aligned. (A naturally
> aligned D_floating datum has zero as the low-order three bits of its
> address.)

### IEEE Floating-Point Formats

The IEEE standard for binary floating-point arithmetic, ANSI/IEEE 754-1985,
defines four floating-point formats in two groups, basic and extended, each
having two widths, single and double. The Alpha architecture supports the
basic single and double formats, with the basic double format serving as the
extended single format. The values representable within a format are
specified by using three integer parameters:

1. P — the number of fraction bits
2. Emax — the maximum exponent
3. Emin — the minimum exponent

Within each format, only the following entities are permitted:

1. Numbers of the form (-1)\*\*S × 2\*\*E × b(0).b(1)b(2)..b(P-1) where:
   1. S = 0 or 1
   2. E = any integer between Emin and Emax, inclusive
   3. b(n) = 0 or 1
2. Two infinities — positive and negative
3. At least one Signaling NaN
4. At least one Quiet NaN

NaN is an acronym for Not-a-Number. A NaN is an IEEE floating-point bit
pattern that represents something other than a number. NaNs come in two
forms: Signaling NaNs and Quiet NaNs. Signaling NaNs are used to provide
values for uninitialized variables and for arithmetic enhancements. Quiet
NaNs provide retrospective diagnostic information regarding previous invalid
or unavailable data and results. Signaling NaNs signal an invalid operation
when they are an operand to an arithmetic instruction, and may generate an
arithmetic exception. Quiet NaNs propagate through almost every operation
without generating an arithmetic exception.

Arithmetic with the infinities is handled as if the operands were of
arbitrarily large magnitude. Negative infinity is less than every finite
number; positive infinity is greater than every finite number.

#### S_Floating

An IEEE single-precision, or S_floating, datum occupies 4 contiguous bytes in
memory starting on an arbitrary byte boundary. The bits are labeled from
right to left, 0 through 31, as shown in Figure 2-11.

_Figure 2-11 • S_floating Datum_

An S_floating operand occupies 64 bits in a floating register, left-justified
in the 64-bit register, as shown in Figure 2-12.

_Figure 2-12 • S_floating Register Format_

The S_floating load instruction reorders bits on the way in from memory,
expanding the exponent from 8 to 11 bits, and sets the low-order fraction
bits to zero. This produces in the register an equivalent T_floating number,
suitable for either S_floating or T_floating operations. The mapping from
8-bit memory-format exponents to 11-bit register-format exponents is shown in
Table 2-2.

_Table 2-2 • S_floating Load Exponent Mapping_

| Memory <30:23> | Register <62:52>                       |
| -------------- | -------------------------------------- |
| 1 1111111      | 1 111 1111111                          |
| 1 xxxxxxx      | 1 000 xxxxxxx    (xxxxxxx not all 1's) |
| 0 xxxxxxx      | 0 111 xxxxxxx    (xxxxxxx not all 0's) |
| 0 0000000      | 0 000 0000000                          |

This mapping preserves both normal values and exceptional values. Note that
the mapping for all 1's differs from that of F_floating load, since for
S_floating all 1's is an exceptional value and for F_floating all 1's is a
normal value.

The S_floating store instruction reorders register bits on the way to memory
and does no checking of the low-order fraction bits. Register bits <61:59>
and <28:0> are ignored by the store instruction. The S_floating load
instruction does no checking of the input.

The S_floating store instruction does no checking of the data; the preceding
operation should have specified an S_floating result.

An S_floating datum is specified by its address A, the address of the byte
containing bit 0. The memory form of an S_floating datum is sign magnitude
with bit 31 the sign bit, bits <30:23> an excess-127 binary exponent, and
bits <22:0> a 23-bit fraction.

The value (V) of an S_floating number is inferred from its constituent sign
(S), exponent (E), and fraction (F) fields as follows:

1. If E=255 and F<>0, then V is NaN, regardless of S.
2. If E=255 and F=0, then V = (-l)\*\*S × Infinity.
3. If 0 < E < 255, then V = (-l)\*\*S × 2\*\*(E-127) × (1.F).
4. If E=0 and F<>0, then V = (-l)\*\*S × 2\*\*(-126) × (0.F).
5. If E=0 and F=0, then V = (-1)\*\*S × 0 (zero).

Floating-point operations on S_floating numbers may take an arithmetic
exception for a variety of reasons, including invalid operations, overflow,
underflow, division by zero, and inexact results.

> #### Note
>
> Alpha implementations will impose a significant performance penalty when
> accessing S_floating operands that are not naturally aligned. (A naturally
> aligned S_floating datum has zero as the low-order two bits of its
> address.)

#### T_floating

An IEEE double-precision, or T_floating, datum occupies 8 contiguous bytes in
memory starting on an arbitrary byte boundary. The bits are labeled from
right to left, 0 through 63, as shown in Figure 2-13.

_Figure 2-13 • T_floating Datum_

A T_floating operand occupies 64 bits in a floating register, arranged as
shown in Figure 2-14.

_Figure 2-14 • T_floating Register Format_

The T_floating load instruction performs no bit reordering on input, nor does
it perform checking of the input data.

The T_floating store instruction performs no bit reordering on output. This
instruction does no checking of the data; the preceding operation should have
specified a T_floating result.

A T_floating datum is specified by its address A, the address of the byte
containing bit 0. The form of a T_floating datum is sign magnitude with bit
63 the sign bit, bits <62:52> an excess-1023 binary exponent, and bits <51:0>
a 52-bit fraction.

The value (V) of a T_floating number is inferred from its constituent sign
(S), exponent (E), and fraction (F) fields as follows:

1. If E=2047 and F<>0, then V is NaN, regardless of S.
2. If E=2047 and F=0, then V = (-1)\*\*S × Infinity.
3. If 0 < E < 2047, then V = (-1)\*\* × 2\*\*(E-1023) × (1.F).
4. If E=0 and F<>0, then V = (-1)\*\*S × 2\*\*(-1022) × (0.F).
5. If E=0 and F=0, then V = (-1)\*\*S × 0 (zero).

Floating-point operations on T_floating numbers may take an arithmetic
exception for a variety of reasons, including invalid operations, overflow,
underflow, division by zero, and inexact results.

> #### Note
>
> Alpha implementations will impose a significant performance penalty when
> accessing T_floating operands that are not naturally aligned. (A naturally
> aligned T_floating datum has zero as the low-order three bits of its
> address.)

### Longword Integer Format in Floating-Point Unit

A longword integer operand occupies 32 bits in memory, arranged as shown in
Figure 2-15.

_Figure 2-15 • Longword Integer Datum_

A longword integer operand occupies 64 bits in a floating register, arranged
as shown in Figure 2-16.

_Figure 2-16 • Longword Integer Floating-Register Format_

There is no explicit longword load or store instruction; the S_floating
load/store instructions are used to move longword data into or out of the
floating registers. The register bits <61:59> are set by the S_floating load
exponent mapping. They are ignored by S_floating store. They are also ignored
in operands of a longword integer operate instruction, and they are set to
000 in the result of a longword operate instruction.

The register format bit <62>, “1”, in Figure 2-16 is part of the Integer Hi
field in Figure 2-15 and represents the high-order bit of that field. Bits
<58:45> of Figure 2-16 are the remaining bits of the Integer Hi field of
Figure 2-15.

> #### Note
>
> Alpha implementations will impose a significant performance penalty when
> accessing longwords that are not naturally aligned. (A naturally aligned
> longword datum has zero as the low-order two bits of its address.)

### Quadword Integer Format in Floating-Point Unit

A quadword integer operand occupies 64 bits in memory, arranged as shown in
Figure 2-17.

_Figure 2-17 • Quadword Integer Datum_

A quadword integer operand occupies 64 bits in a floating register, arranged
as shown in Figure 2-18.

_Figure 2-18 • Quadword Integer Floating-Register Format_

There is no explicit quadword load or store instruction; the T_floating
load/store instructions are used to move quadword data into or out of the
floating registers.

The T_floating load instruction performs no bit reordering on input. The
T_floating store instruction performs no bit reordering on output. This
instruction does no checking of the data; when used to store quadwords, the
preceding operation should have specified a quadword result.

> #### Note
>
> Alpha implementations will impose a significant performance penalty when
> accessing quadwords that are not naturally aligned. (A naturally aligned
> quadword datum has zero as the low-order three bits of its address.)

### Data Types with No Hardware Support

The following VAX data types are not directly supported in Alpha hardware.

- Octaword
- H_floating
- D_floating (except load/store and convert to/from G_floating)
- Variable-Length Bit Field
- Character String
- Trailing Numeric String
- Leading Separate Numeric String
- Packed Decimal String

