# 4 Programmable Translation Array

## 4.1 General

This section describes the operation of the MCP1600 Microprocessor set's most
unique feature, the Programmable Translation Array (PTA). The PTA serves to
generate new microinstruction fetch addresses as a function of several
parameters. These parameters are those which are normally considered during
the decode of a macroinstruction.

While the PTA was designed specifically to eliminate most of the over head of
macroinstruction translation, it is useful for other purposes. One could, for
instance, conceive of a data driven processor that would determine the next
operation to be performed on a data structure as a function of the present
data and the present operation. The uses of the PTA are limited only by the
system designer's imagination.

Briefly, the PTA consists of eight elements. They are:

* Location Counter
* Array 1
* Array 2
* Array 3
* Translation Register
* Array 4
* Translation State Register
* Return Register

![fig-4-1](i/fig-4-1.png "PTA Component Interconnections")

Fig 4-1. PTA Component Interconnections

These elements give the capability of calculating microinstruction addresses
other than sequentially, or as specified by a jump instruction. Figure 4-1
depicts their interconnection. The mapping (or new Location Counter (LC)
value) that the PTA generates, when invoked, is a function of the value of
the LC, the contents of the Translation Register (TR), the interrupts, and
the state of the RNI line.

## 4.2 PTA Components

This section will describe the components of the Programmable Translation
Array and their functions.

### 4.2.1 Location Counter

It is the function of the Location Counter (LC) to hold the address of the
next microinstruction. The LC is 11-bits wide and has outputs to MI10..MIB00
and to Array #1. It has inputs from the Master Control function, Array #4 and
the Return Register (RR). There is also an input to the LC from an
incrementer.

### 4.2.2 Array #1

Array #1 is an 88 element array of active low input AND gates with 23 inputs
There are 11 true inputs and 11 complemented inputs from the LC and the RNI
bit (MIB17). Figure 4-2 illustrates the organization of Array #1. Figure 4-3
illustrates the concept, as opposed to implementation of a typical gate, one
of 88, that make up Array #1. The outputs of these gates make up the bulk of
the inputs of Array #2.

![fig-4-2](i/fig-4-2.png "Array #1 Organiztion")

Fig 4-2. Array #1 Organiztion

![fig-4-3](i/fig-4-3.png "Typical Gate — Array #1")

Fig 4-3. Typical Gate — Array #1

The purpose of Array #1 is to perform a selection function. When the inputs
to Array #1 match one (or more) of the word values (addresses) the output
associated with that word is asserted. This array is programmed with 6
hexidecimal digits as shown in Figure 4-4. Transistors are placed in the
array for 1 bits in the data specification. To program a group of addresses
the bits of the address to be left out are specified as 0 bits for the true
and complement address inputs. This produces a ‘DON'T CARE’ effect for those
bits and the result will always be a match. This lets the user match on
modulo address.

![fig-4-4](i/fig-4-4.png "Array #1 Data Specification")

Fig 4-4. Array #1 Data Specification

The RNI Iine serves to inhibit the output of Array #1. The reason for this is
described later.

### 4.2.3 Array #2

Array #2 is an ORed array whose outputs are negated. The array has 89 inputs,
88 from Array #1 and one from MIB17, the RNI line. The seven outputs from
Array #2 represent a translation state code and become inputs into Array #3.

Figure 4-5 illustrates the orgainzation of Array #2. Figure 4-6 illustrates
in some detail, the conceptual structure of the gate and interconnect
structure of Array #2. The small circles present where the lines would
normally cross represent connections that can or cannot be made. It is via
the making or not making of the connections with transistors that this array
is programmed.

![fig-4-5](i/fig-4-5.png "Array #2 Organization")

Fig 4-5. Array #2 Organization

![fig-4-6](i/fig-4-6.png "Array #2 Gate and Interconnect Structure")

Fig 4-6. Array #2 Gate and Interconnect Structure

Array #2 is driven by the inputs from Array #1. When one or more outputs of
Array #1 are asserted, Array #2 will make the corresponding word available as
its outputs.

The purpose of Arrays #1 and #2 is to provide a mapping between the present
value of the Location Counter and a preselected set of translation state
codes.

Due to electrical considerations, there are restrictions placed on the
configuration of Array #2. Normally this array is programmed in a 4 of 7 code
(4 of 7 outputs may be selected to be high, the other 3 must be low), or more
ideally, to reduce capacitive loading, a 5 of 7 code. The tables below
describe the various state code outputs available in both the 4 of 7 and the
5 of 7 schemes.

Table 4-1 Translation State Code Outputs — 4 of 7
```
0F 2D 3C 56 69
17 2E 47 59 6A
1B 33 4B 5A 6C
1D 35 4D 5C 71
1E 36 4E 63 72
27 39 53 65 74
2B 3A 55 66 78
```

Table 4-2 Translation State Code Outputs — 5 of 7
```
1F 3D 5B 6B 75
2F 3E 5D 6D 76
37 4F 5E 6E 79
3B 57 67 73 7A
            7C
```

The outputs of Array #2 represent some of the inputs to Array #3.

The RNI line (MIB17) deserves mention at th is point. It is the purpose of
the RNI line to force a particular user defined state code from the mapping
represented by Arrays #1 and #2. This state code will be independent of the
contents of the LC.

Accordingly, RNI inhibits the outputs of Array #1 and invokes that state code
selected by the user in Array #2 and makes it present at the output of Array
#2.

The programming of Array #2 is illustrated in Figure 4-7 below. Transistors
are put in the arrays for zero bits as per the data specifications.

![fig-4-7](i/fig-4-7.png "Data Specification")

Fig 4-7. Data Specification

### 4.2.4 Array #3

Array #3 consists of 100 active low input AND gates, and has 42 inputs. In
contrast to Arrays #1 and #2, the inputs come from a variety of sources. The
inputs to this array constitute a direct interface to the real world at the
macromachine level, as one of the inputs is the Translation Register (TR).
The inputs to Array #3 are:

* Seven from Array #2 (Translation Code).

* Sixteen from the TR. Eight are true data and eight are complemented data.

* Fourteen inputs from the interrupt latches. Again, both true and
  complemented data are present.

* Two from the translation state register. Again, both true and complemented
  data are used.

* One input, called the Q signal, not generally usable.

It is worth noting, that, while there are 42 inputs in Array #3, they are not
all present at the same time. The array is broken into two partitions. The
first partition consists of words 0 through 15, and has as its inputs, the 14
bits from the interrupt latches. The second partition of the array, words 16
through 99 have, in these same slots, the 16 bits of inputs from the
Translation Register.

The Figure 4-8 illustrates the structure of the first partition of the array.
Figure 4-9 illustrates the second partition of the array. Figure 4-10 shows a
conceptual picture of a typical gate in the array.

![fig-4-8](i/fig-4-8.png "Array #3 Interrupt Organization")

Fig 4-8. Array #3 Interrupt Organization

![fig-4-9](i/fig-4-9.png "Array #3 Translation Register Organization")

Fig 4-9. Array #3 Translation Register Organization

![fig-4-10](i/fig-4-10.png "Typical Gate of Array #3")

Fig 4-10. Typical Gate of Array #3

Array #3, being an ANDed array, will try to match the configuration of its
inputs against one of the words that make up the array. If it finds a match,
the output associated with that word will be asserted.

Array #3 is programmed with true data as eight hexadecimal digits. DON'T
CAREs, which always result in matches, are created by placing both true and
complemented bits to zero. Below is a data specification for the programming
of Array #3.

![fig-4-a](i/fig-4-a.png "Data Specification for the Programming of Array #3")

### 4.2.5 Array #4

Array #4 is a NORed array with 100 inputs which come from Array #3. The
outputs generated by Array #4 include address data to be fed into the LC,
data to be fed into the Translation State Register (TSR), and three control
lines. Two control lines determine whether the LC will be loaded from the
Return Register (RR) or the output of the translation array. The third
control line determines whether or not the value presented to the TSR will in
fact be loaded into the TSR. Figure 4-11 illustrates the orgainzation of this
array. Note that not all the outputs are complemented. The two control
signals LRA and LTA are true data.

![fig-4-11](i/fig-4-11.png "Array #4 Organization")

Fig 4-11. Array #4 Organization

Array #4 will determine if any of its inputs are active. If they are, the
word associated with the active input is placed on the output lines.

The array is programmed into terms of true data. Five hexadecimal digits are
used to program each word. Transistors are placed in the array for 1 bits in
the data specification. More than one active AND gate in Array 3 causes the
outputs to OR.

![fig-4-b](i/fig-4-b.png "Data Specification for the Programming of Array #4")

### 4.2.6 Translation State Register

The Translation State Register (TSR) serves two functions. One is to
determine whether the Hi or the Lo order byte of the Translation Register
(TR) is to be selected for input to Array #3; The other is to provide a four
state feedback as an input of Array #3. The loading of the TSR is controlled
by an output (LTSR) of Array #4.

### 4.2.7 Translation Register

The Translation Register (TR) holds the data presently serving as input to
the PTA. It receives its inputs from the Micro Instruction Bus (MIB15..MIB00)
as a result of an LTR or IW instruction. Because of the fact that its output
destination is 8 bits wide, only half of the TR can be examined at anyone
time. The Translation State Register (TSR) controls which half of the TR is
gated into the input of Array #3, its destination. It serves as a feedback
term of information to the second half of the word.

Bit 2 of the TSR controls the selection of translation input from the TR.
When this bit is a zero the upper byte of the TR is selected; when it is a
one the lower byte is selected. TSR2 does not serve as an input to Array #3.

## 4.3 Programmable Translation Array Operations

This section describes the operation of the Programmable Translation Array.
The operation is based on the description of the components in the preceeding
section that make up the PTA. The PTA operates as a loop. The beginning and
end points of the loop can be considered as the Location Counter.

This loop is completed within one machine cycle. It is helpful to remember
that the main components of the loop are

* The Location Counter

* Arrays #1 and #2, which taken together perform a mapping of the Location
  Counter to a translation code.

* The translation register, which holds the macroinstruction undergoing the
  translation process.

* Arrays #3 and #4, which take the translation code and the macroinstruction
  presently undergoing translation and map them into an address.

This newly generated address can then point to the beginning of a
macroroutine to interpret the macroinstruction presently accessed.

The following description can be best followed by reference to the attached
diagrams which depict the flow of data in the Programmable Translation Array
as a function of phase time clocks.

The operation of the Programmable Translation Array begins at ∅1. During ∅1
the location counter is loaded with its new value. The new value can come
from anyone of four sources. They are:

* From Array #4 of the Programmable Translation Array
* From the MI register
* From the incrementer
* From the Return Register

Figure 4-12 assumes, for the purposes of instruction, that the LC is loaded
from the incrementer. Concurrently, with the loading of the Location Counter
at ∅1, the TR is also being loaded if either a LTR or an IW instruction was
executed.

![fig-4-12](i/fig-4-12.png "∅1 Data Flow")

Fig 4-12. ∅1 Data Flow

At the beginning of ∅2 (see Figure 4-13) the contents of the LC are clocked
out to the MIB bus (MIB10..00) and to Array #1. Both the true and
complemented forms of the LC are input to Array #1. Also input is the RNI
line. Array #1 takes the input data word and determines whether or not it has
a match. If it has a match, then the appropriate output is set at the end of
∅2. If there is no match, the translation proceeds no farther because no
outputs are set.

![fig-4-13](i/fig-4-13.png "∅2 Data Flow")

Fig 4-13. ∅2 Data Flow

At the beginning of ∅3 (see Figure 4-14), Array #2 samples the outputs from
Array #1 and determines whether any are active. If there is a match, then the
translation code is generated and fed to Array #3, also during ∅3.

![fig-4-14](i/fig-4-14.png "∅3 Data Flow")

Fig 4-14. ∅3 Data Flow

During ∅3, the contents of the selected byte of the TR are fed to Array #3
along with the contents of the interrupt register, the TSR, and the Q bit.
During the later portions of ∅3, Array #3 determines if there is a match and,
if a match is found, at the end of ∅3 an output is generated.

This output is fed into Array #4 at the beginning of ∅4 (see Figure 4-15).
During ∅4, Array #4 determines whether there is an active input to it. If
there is an active input, the contents of the word associated with the input
are sent out at the end of ∅4. The Array #4 word mayor may not cause the TSR
to be loaded, and mayor may not cause the LC to be loaded at the next
occurance of ∅1.

![fig-4-15](i/fig-4-15.png "∅4 Data Flow")

Fig 4-15. ∅4 Data Flow


