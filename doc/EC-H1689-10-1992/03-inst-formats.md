# Chapter 3 · Instruction Formats

## Alpha Registers

Each Alpha processor has a set of registers that hold the current processor
state. If an Alpha system contains multiple Alpha processors, there are
multiple per-processor sets of these registers.

### Program Counter

The Program Counter (PC) is a special register that addresses the instruction
stream. As each instruction is decoded, the PC is advanced to the next
sequential instruction. This is referred to as the _updated_ PC. Any
instruction that uses the value of the PC will use the updated PC. The PC
includes only bits <63:2> with bits <1:0> treated as RAZ/IGN. This quantity
is a longword-aligned byte address. The PC is an implied operand on
conditional branch and subroutine jump instructions. The PC is not accessible
as an integer register.

### Integer Registers

There are 32 integer registers (R0 through R31), each 64 bits wide.

Register R31 is assigned special meaning by the Alpha architecture:

When R31 is specified as a register source operand, a zero-valued operand is supplied.

For all cases except the Unconditional Branch and Jump instructions, results
of an instruction that specifies R31 as a destination operand are discarded.
Also, it is UNPREDICTABLE whether the other destination operands (implicit
and explicit) are changed by the instruction. It is implementation dependent
to what extent the instruction is actually executed once it has been fetched.
It is also UNPREDICTABLE whether exceptions are signaled during the execution
of such an instruction. Note, however, that exceptions associated with the
instruction fetch of such an instruction are always signaled.

There are some interesting cases involving R31 as a destination:

- STx_C R31,disp(Rb)

  Although this might seem like a good way to zero out a shared location and
  reset the lock_flag, this instruction causes the lock_flag and virtual
  location {Rbv + SEXT(disp)} to become UNPREDICTABLE.

- LDx_L R31,disp(Rb)

  This instruction produces no useful result since it causes both lock_flag
  and locked_physicaLaddress to become UNPREDICTABLE.

  Unconditional Branch (BR and BSR) and Jump (JMP, JSR, RET, and
  JSR_COROUTINE) instructions, when R31 is specified as the Ra operand,
  execute normally and update the PC with the target virtual address. Of
  course, no PC value can be saved in R31.

### Floating-Point Registers

There are 32 floating-point registers (F0 through F31), each 64 bits wide.

When F31 is specified as a register source operand, a true zero-valued
operand is supplied. See _Definitions_ in Chapter 4 for a definition of true
zero.

Results of an instruction that specifies F31 as a destination operand are
discarded and it is UNPREDICTABLE whether the other destination operands
(implicit and explicit) are changed by the instruction. In this case, it is
implementation-dependent to what extent the instruction is actually executed
once it has been fetched. It is also UNPREDICTABLE whether exceptions are
signaled during the execution of such an instruction. Note, however, that
exceptions associated with the instruction fetch of such an instruction are
always signaled.

A floating-point instruction that operates on single-precision data reads all
bits <63 :0> of the source floating-point register. A floating-point
instruction that produces a single-precision result writes all bits <63:0> of
the destination floating-point register.

### Lock Registers

There are two per-processor registers associated with the LDx_L and STx_C
instructions, the lock_flag and the locked_physicaLaddress register. The use
of these registers is described in _Memory Integer Load/Store Instructions_
in Chapter 4.

### Optional Registers

Some Alpha implementations may include optional memory prefetch or VAX
compatibility processor registers.

#### Memory Pre/etch Registers

If the prefetch instructions FETCH and FETCH_M are implemented, an
implementation will include two sets of state prefetch registers used by
those instructions. The use of these registers is described in _Miscellaneous
Instructions_ in Chapter 4. These registers are not directly accessible by
software and are listed for completeness.

#### VAX Compatibility Register

The VAX compatibility instructions RC and RS include the intr_flag register,
as described in VAX _Compatibility Instructions_ in Chapter 4.

## Notation

The notation used to describe the operation of each instruction is given as a
sequence of control and assignment statements in an ALGOL-like syntax.

### Operand Notation

Tables Table 3-1, 3-2, and 3-3 list the notation for the operands, the operand values, and the
other expression operands.

_Table 3-1 · Operand Notation_

| Notation | Meaning                                                               |
| -------- | --------------------------------------------------------------------- |
| Ra       | An integer register operand in the Ra field of the instruction.       |
| Rb       | An integer register operand in the Rb field of the instruction.       |
| #b       | An integer literal operand in the Rb field of the instruction.        |
| Rc       | An integer register operand in the Rc field of the instruction.       |
| Fa       | A floating-point register operand in the Ra field of the instruction. |
| Fb       | A floating-point register operand in the Rb field of the instruction. |
| Fc       | A floating-point register operand in the Rc field of the instruction. |

_Table 3-2 · Operand Value Notation_

| Notation | Meaning |
| -------- | ------- |
| Rav      | The value of the Ra operand. This is the contents of register Ra. |
| Rbv      | The value of the Rb operand. This could be the contents of register Rb, or a zero-extended 8-bit literal in the case of an Operate format instruction. |
| Fav      | The value of the floating point Fa operand. This is the contents of register Fa. |
| Fbv      | The value of the floating point Fb operand. This is the contents of register Fb. |

_Table 3-3 · Expression Operand Notation_

| Notation     | Meaning                                                 |
| ------------ | ------------------------------------------------------- |
| IPR_x        | Contents of Internal Processor Register x               |
| IPR_SP[mode] | Contents of the per-mode stack pointer selected by mode |
| PC           | Updated PC value                                        |
| Rn           | Contents of integer register n                          |
| Fn           | Contents of floating-point register n                   |
| X[m]         | Element m of array X                                    |

### Instruction Operand Notation

The notation used to describe instruction operands follows from the operand
specifier notation used in the VAX Architecture Standard. Instruction
operands are described as follows:

    <name>.<access type><data type>

#### \<name\>

Specifies the instruction field (Ra, Rb, Rc, or disp) and register type of
the operand (integer or floating). It can be one of the following:

| Name | Meaning                                                               |
| ---- | --------------------------------------------------------------------- |
| disp | The displacement field of the instruction.                            |
| fnc  | The PAL function field of the instruction.                            |
| Ra   | An integer register operand in the Ra field of the instruction.       |
| Rb   | An integer register operand in the Rb field of the instruction.       |
| #b   | An integer literal operand in the Rb field of the instruction.        |
| Rc   | An integer register operand in the Rc field of the instruction.       |
| Fa   | A floating-point register operand in the Ra field of the instruction. |
| Fb   | A floating-point register operand in the Rb field of the instruction. |
| Fc   | A floating-point register operand in the Rc field of the instruction. |

#### \<access type\>

Is a letter denoting the operand access type:

| Access Type | Meaning                                       |
| ----------- | --------------------------------------------- |
| a | <p> The operand is used in an address calculation to form an effective address. The data type code that follows indicates the units of addressability (or scale factor) applied to this operand when the instruction is decoded. <p> For example: <p> “.al” means scale by 4 (longwords) to get byte units (used in branch displacements); “.ab” means the operand is already in byte units (used in load/store instructions). |
| i | The operand is an immediate literal in the instruction. |
| r | The operand is read only.                               |
| m | The operand is both read and written.                   |
| w | The operand is write only.                              |

#### \<data type\>

Is a letter denoting the data type of the operand:

| Data Type | Meaning                                       |
| --------- | --------------------------------------------- |
| b         | Byte                                          |
| f         | F_floating                                    |
| g         | G_floating                                    |
| l         | Longword                                      |
| q         | Quadword                                      |
| s         | IEEE single floating (S_floating)             |
| t         | IEEE double floating (T_floating)             |
| w         | Word                                          |
| x         | The data type is specified by the instruction |

### Operators

The operators shown in Table 3-4 are used:

_Table 3-4 · Operators_

| Operator | Meaning                                                 |
| -------- | ------------------------------------------------------- |
| !        | Comment delimiter                                       |
| +        | Addition                                                |
| -        | Subtraction                                             |
| \*       | Signed multiplication                                   |
| \*U      | Unsigned multiplication                                 |
| \*\*     | Exponentiation (left argument raised to right argument) |
| /        | Division                                                |
| ←        | Replacement                                             |
| \|\|     | Bit concatenation                                       |
| {}       | Indicates explicit operator precedence                  |
| (x)      | Contents of memory location whose address is x          |
| x\<m:n\> | Contents of bit field of x defined by bits n through m  |
| x\<m\>   | M'th bit of x                                           |

_Table 3-4 · Operators (Continued)_

<table>
<tr><th>Operator</th><th>Meaning</th></tr>
<tr><td>ACCESS(x,y)</td><td>
Accessibility of the location whose address is x using the access mode y.
Returns a Boolean value TRUE if the address is accessible, else
FALSE.</td></tr>
<tr><td>AND</td><td>Logical product</td></tr>
<tr><td>ARITH_RIGHT_SHIFT(x,y)</td><td>
Arithmetic right shift of first operand by the second operand. Y is an
unsigned shift value. Bit 63, the sign bit, is copied into vacated bit
positions and shifted out bits are discarded.</td></tr>
<tr><td>BYTE_ZAP(x,y)</td><td>
X is a quadword, y is an 8-bit vector in which each bit corresponds to a byte
of the result. The y bit to x byte correspondence is y\<n\> ↔ x<8n+7:8n>.
This correspondence also exists between y and the result.

For each bit of y from n = 0 to 7, if y \<n\> is 0 then byte \<n\> of x is
copied to byte \<n\> of result, and if y \<n\> is 1 then byte \<n\> of result
is forced to all zeros.</td></tr>
<tr><td>CASE</td><td>
The CASE construct selects one of several actions based on the value of its
argument. The form of a case is:

    CASE argument OF
        argvalue1: action_1
        argvalue2: action_2
        argvaluen: action_n
        [otherwise: default_action]
    ENDCASE

If the value of argument is argvalue1 then action_1 is executed; if argument
= argvalue2, then action_2 is executed, and so forth.

Once a single action is executed, the code stream breaks to the ENDCASE
(there is an implicit break as in Pascal). Each action may nonetheless be a
sequence of pseudocode operations, one operation per line.

Optionally, the last argvalue may be the atom ‘otherwise’. The associated
default action will be taken if none of the other argvalues match the
argument.</td></tr>
<tr><td>DIV</td><td>Integer division (truncates)</td></tr>
<tr><td>LEFT_SHIFT(x,y)</td><td>
Logical left shift of first operand by the second operand. Y is an unsigned
shift value. Zeros are moved into the vacated bit positions, and shifted out
bits are discarded.</td></tr>
</table>

_Table 3-4 · Operators (Continued)_

<table>
<tr><th>Operator</th><th>Meaning</th></tr>
<tr><td>NOT</td><td>Logical (ones) complement</td></tr>
<tr><td>OR</td><td>Logical sum</td></tr>
<tr><td>x MOD y</td><td>x modulo y</td></tr>
<tr><td>Relational Operators</td><td>
<table>
<tr><th>Operator</th><th>Meaning</th></tr>
<tr><td>LT</td><td>Less than signed</td></tr>
<tr><td>LTU</td><td>Less than unsigned</td></tr>
<tr><td>LE</td><td>Less or equal signed</td></tr>
<tr><td>LEU</td><td>Less or equal unsigned</td></tr>
<tr><td>EQ</td><td>Equal signed and unsigned</td></tr>
<tr><td>NE</td><td>Not equal signed and unsigned</td></tr>
<tr><td>GE</td><td>Greater or equal signed</td></tr>
<tr><td>GEU</td><td>Greater or equal unsigned</td></tr>
<tr><td>GT</td><td>Greater signed</td></tr>
<tr><td>GTU</td><td>Greater unsigned</td></tr>
<tr><td>LBC</td><td>Low bit clear</td></tr>
<tr><td>LBS</td><td>Low bit set</td></tr>
</table>
</td></tr>
<tr><td>MINU(x,y)</td><td>
Returns the smaller of x and y, with x and y interpreted as unsigned
integers</td></tr>
<tr><td>PHYSICAL_ADDRESS</td><td>Translation of a virtual address</td></tr>
<tr><td>PRIORITY_ENCODE</td><td>
Returns the bit position of most significant set bit, interpreting its
argument as a positive integer (= int(lg(x))).

For example:

    priority_encode (255) = 7

</td></tr>
<tr><td>RIGHT_SHIFT(x,y)</td><td>
Logical right shift of first operand by the second operand. Y is an unsigned
shift value. Zeros are moved into vacated bit positions, and shifted out bits
are discarded.</td></tr>
<tr><td>SEXT(x)</td><td>X is sign-extended to the required size.</td></tr>
<tr><td>TEST(x,cond)</td><td>
The contents of register x are tested for branch condition (cond) true. TEST
returns a Boolean value TRUE if x bears the specified relation to 0, else
FALSE is returned. Integer and floating test conditions are drawn from the
preceding list of relational operators.</td></tr>
<tr><td>XOR</td><td>Logical difference</td></tr>
<tr><td>ZEXT(x)</td><td>X is zero-extended to the required size.</td></tr>
</table>

