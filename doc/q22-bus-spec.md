# Q22-Bus Specification

## А.1 General Description

The Q22-Bus, also known as the extended LSI-11 Bus, is the low-end member of
Digital's bus family. All of Digital's microcomputers, such as the MicroVAX
I, MicroVAX II, and MicroPDP-11, use the Q22-Bus.

The Q22-Bus consists of 42 bidirectional and 2 unidirectional signal lines.
These form the lines along which the processor, memory, and I/O devices
communicate with each other.

Addresses, data, and control information are sent along these signal lines,
some of which contain time-multiplexed information. The lines are divided as
follows.

* Sixteen multiplexed data/address lines -- BDAL<15:00>
* Two multiplexed address/parity lines -- BDAL<17:16>
* Four extended address lines -- BDAL<21:18>
* Six data transfer control lines -- BBS7, BDIN, BDOUT, BRPLY, BSYNC, BWTBT
* Six system control lines -- BHALT, BREF, BEVNT, BINIT, BDCOK, BPOK
* Ten interrupt control and direct memory access control lines -- ВIАКО,
  BIAKI, BIRQ4, BIRQ5, BIRQ6, BIRQ7, BDMGO, BDMR, BSACK, BDMGI

In addition, a number of power, ground, and space lines are defined for the
bus. Refer to Table А-1 for a detailed description of these lines.

The discussion in this Appendix applies to the general 22-bit physical
address capability. All modules used with the KA630-A CPU module must use
22-bit addressing.

Most Q22-Bus signals are bidirectional and use terminations for a negated
(high) signal level. Devices connect to these lines via high-impedance bus
receivers and open collector drivers. The asserted state is produced when a
bus driver asserts the line low.

Although bidirectional lines are electrically bidirectional (any point along
the line can be driven or received), certain lines are functionally
unidirectional. These lines communicate to or from a bus master (or signal
source), but not both. Interrupt acknowledge (BIAK) and direct memory access
grant (BDMG) signals are physically unidirectional in a daisy-chain fashion.
These signals originate at the processor output signal pins. Each is received
on device input pins (BIAKI or BDMGI) and is conditionally retransmitted via
device output pins (BIAKO or BDMGO). These signals are received from
higher-priority devices and are retransmitted to lower-priority devices along
the bus, establishing the position-dependent priority scheme.

### A.1.1 Master/Slave Relationship

Communication between devices on the bus is asynchronous. А master/slave
relationship exists throughout each bus transaction. Only one device has
control of the bus at any one time. This controlling device is termed the bus
master, or arbiter. The master device controls the bus when communicating
with another device on the bus, termed the slave.

The bus master (typically the processor or a DMA device) initiates a bus
transaction. The slave device responds by acknowledging the transaction in
progress and by receiving data from, or transmitting data to, the bus master.
Q22-Bus control signals transmitted or received by the bus master or bus
slave device must complete the sequence according to bus protocol.

The processor controls bus arbitration, that is, which device becomes bus
master at any given time. A typical example of this relationship is a disk
drive, as master, transferring data to memory as slave. Communication on the
Q22-Bus is interlocked so that, for certain control signals issued by the
master device, there must be a response from the slave in order to complete
the transfer. It is the master/slave signal protocol that makes the Q22-Bus
asynchronous. The asynchronous operation precludes the need for synchronizing
with, and waiting for, clock pulses.

Since bus cycle completion by the bus master requires response from the slave
device, each bus master must include a timeout error circuit that aborts the
bus cycle if the slave does not respond to the bus transaction within 10 μs.
The actual time before a timeout error occurs must be longer than the reply
time of the slowest peripheral or memory device on the bus.

## А.2 Bus Signal Assignments

Table А-1 lists the signal assignments for the data/address, control,
power/ground, and spare functions of the Q22-Bus.

: Table A-1: Data and Address

| Name    | Pin Assignment | Name    | Pin Assignment |
| ------- | -------------- | ------- | -------------- |
| BDAL0   | AU2            | BDAL11  | BR2            |
| BDAL1   | AV2            | BDAL12  | BS2            |
| BDAL2   | BE2            | BDAL13  | BT2            |
| BDAL3   | BF2            | BDAL14  | BU2            |
| BDAL4   | BH2            | BDAL15  | BV2            |
| BDAL5   | BJ2            | BDAL16  | АС1            |
| BDAL6   | BK2            | ВDAL17  | AD1            |
| BDAL7   | BL2            | BDAL18  | BC1            |
| BDAL8   | BM2            | BDAL19  | BD1            |
| BDAL9   | BN2            | ВDAL20  | ВЕ1            |
| BDAL10  | BP2            | BDAL21  | ВF1            |

: Table A-1: Data Control

| Name    | Pin Assignment | Name    | Pin Assignment |
| ------- | -------------- | ------- | -------------- |
| BDOUT   | AE2            | BSYNC   | AJ2            |
| BRPLY   | AF2            | BWTBT   | AK2            |
| BDIN    | AH2            | BBS7    | AP2            |

: Table A-1: Interrupt Control

| Name    | Pin Assignment | Name    | Pin Assignment |
| ------- | -------------- | ------- | -------------- |
| BIRQ7   | ВР1            | BIRQ4   | AL2            |
| BIRQ6   | АВ1            | BIAKI   | AM2            |
| BIRQ5   | АА1            | BIAKO   | AN2            |

: Table A-1: DMA Control

| Name    | Pin Assignment | Name    | Pin Assignment |
| ------- | -------------- | ------- | -------------- |
| BDMR    | AN1            | BDMGI   | AR2            |
| BSACK   | BN1            | BDMGO   | AS2            |

: Table A-1: System Control

| Name    | Pin Assignment | Name    | Pin Assignment |
| ------- | -------------- | ------- | -------------- |
| BHALT   | АР1            | BDCOK   | ВА1            |
| BREF    | АR1            | ВРОК    | ВВ1            |
| BINIT   | AT2            | BEVMT   | ВR1            |

: Table A-1: Power and Ground

| Name    | Pin Assignment | Name    | Pin Assignment |
| ------- | -------------- | ------- | -------------- |
| +5      | AA2            | +5      | BA2            |
| -12     | AB2            | -12     | BB2            |
| GND     | AC2            | GND     | BC2            |
| +12     | AD2            | +12     | BD2            |
| GND     | AJ1            | GND     | BJ1            |
| GND     | AM1            | GND     | ВМ1            |
| +5B or +12B (battery) | AS1 | +12B    | BS1            |
| GND     | АТ1            | GND     | BT1            |
| +5B     | AV1            | +5      | BV1            |

: Table A-1: Spares

| Name    | Pin Assignment | Name    | Pin Assignment |
| ------- | -------------- | ------- | -------------- |
| SSpare1 | АЕ1            |         | ~~BE1~~        |
| SSpare2 | АF1            |         | ~~BF1~~        |
| SSpare3 | АН1            | SSраге8 | ВН1            |
| MSpareA | AK1            | MSpareB | BK1            |
| MSpareA | АL1            | MSpareB | BL1            |
| PSpare1 | AU1            | ASpare2 | BU1            |

1. SSpare BE1 now ВDAL20
2. SSpare ВF1 now BDAL21

## A.3 Data Transfer Bus Cycles

Data transfer bus cycles are listed and defined in Table A-2.

These bus cycles, executed by bus master devices, transfer 16-bit words or
8-bit bytes to or from slave devices. In block mode, multiple words may be
transferred to sequential word addresses, starting from a single bus address.
The bus signals listed in Table A-3 are used in the data transfer operations
described in Table A-2.

: Table A-2 Data Transfer Operations

| Mnemonic | Description                   | Function                  |
| -------- | ----------------------------- | ------------------------- |
| DATI     | Data word input               | Read                      |
| DATO     | Data word output              | Write                     |
| DATOB    | Data byte output              | Write byte                |
| DATIO    | Data word input/output        | Read-modify-write         |
| DATIOB   | Data word input/byte output   | Read-modify-write byte    |
| DATBI    | Data block input              | Read block                |
| DATBO    | Data block output             | Write block               |

* Mnemonic — Bus Cycle Mnemonic
* Function — with Respect to the Bus Master

: Table A-3 Bus Signals for Data Transfers

| Mnemonic | Description                   | Function                  |
| -------- | ----------------------------- | ------------------------- |
| BDAL<21:00> L | 22 Data/address lines    | BDAL<15:00> L are used for word and byte transfers. BDAL<17:16> L are used for extended addressing, memory parity error (16), and memory parity error enable (17), functions. BDAL<21:18> L are used for extended addressing beyond 256 Kbytes |
| BSYNC L  | Bus cycle control             | Indicates bus transaction in progress |
| BDIN L   | Data input indicator          | Strobe signals            |
| BDOUT L  | Data output indicator         | Strobe signals            |
| BRPLY L  | Slave's acknowledge of bus cycle | Strobe signals         |
| BWTBT L  | Write/byte control            | Control signals           |
| BBS7 L   | I/O device select             | Indicates address is in the I/O page |

Data transfer bus cycles can be reduced to five basic types: DATI, DATO(B),
DATIO(B), DATBI, and DATBO. These transactions occur between the bus master
and one slave device selected during the addressing portion of the bus cycle.

### A.3.1 Bus Cycle Protocol

Before initiating a bus cycle, the previous bus transaction must have been
completed (BSYNC L negated) and the device must become bus master. The bus
cycle can be divided into two parts: an addressing portion, and a data
transfer portion. During the addressing portion, the bus master outputs the
address for the desired slave device, memory location, or device register.
The selected slave device responds by latching the address bits and holding
this condition for the duration of the bus cycle until BSYNC L becomes
negated. During the data transfer portion, the actual data transfer occurs.

### A.3.2 Device Addressing

The device addressing portion of a data transfer bus cycle comprises an
address setup and deskew time, and an address hold and deskew time. During
the address setup and deskew time, the bus master does the following.

* Asserts BDAL<21:00> L with the desired slave device address bits.
* Asserts BBS7 L if a device in the I/O page is being addressed.
* Asserts BWTBT L if the cycle is a DATO(B) or DATBO bus cycle.

During this time, the address, BBS7 L, and BWTBT L signals are asserted at
the slave bus receiver for at least 75 ns before BSYNC goes active. Devices
in the I/0 page ignore the 9 high-order address bits BDAL<21:13>, and
instead, decode BBS7 L along with the 13 low-order address bits. An active
BWTBT L signal during address setup time indicates that a DATO(B) or DATBO
operation follows, while an inactive BWTBT L indicates a DATI, DATBI, or
DATIO(B) operation.

The address hold and deskew time begins after BSYNC L is asserted.

The slave device uses the active BSYNC L bus received output to clock BDAL
address bits, BBS7 L, and BWTBT L into its internal logic. BDAL<21:00> L,
BBS7 L, and BWTBT L remain active for 25 ns (minimum) after BSYNC L bus
receiver goes active. BSYNC L remains active for the duration of the bus
cycle.

Memory and peripheral devices are addressed similarly, except for the way the
slave device responds to BBS7 L. Addressed peripheral devices must not decode
address bits on BDAL<21:13> L. Addressed peripheral devices may respond to a
bus cycle when BBS7 L is asserted (low) during the addressing portion of the
cycle. When asserted, BBS7 L indicates that the device address resides in the
I/O page (the upper 4KW address space). Memory devices generally do not
respond to addresses in the I/O page; however, some system applications may
permit memory to reside in the I/O page for use as DMA buffers, read-only
memory bootstraps, diagnostics, etc.

### A.3.3 DATI

Figure A-1: DATI Bus Cycle

The DATI bus cycle, shown in Figure A-1, is a read operation. During DATI,
data is input to the bus master. Data consists of 16-bit word transfers over
the bus. During the data transfer portion of the DATI bus cycle, the bus
master asserts BDIN L 100 ns (minimum) after BSYNC L is asserted. The slave
device responds to BDIN L active as follows.

* Asserts BRPLY L 0 ns (minimum) to 8 μs (maximum to avoid bus timeout)
  after receiving BDIN L, and 125 ns (maximum) before BDAL bus driver data
  bits are valid.
* Asserts BDAL<21:00> L with the addressed data and error information 0 ns
  (minimum) after receiving BDIN, and 125 ns (maximum) after assertion of
  BRPLY.

When the bus master receives BRPLY L, it does the following.

* Waits at least 200 ns deskew time and then accepts input data at
  BDAL<17:00> L bus receivers. BDAL <17:16> L are used for transmitting
  parity errors to the master.
* Negates BDIN L 200 ns (minimum) to 2 μs (maximum) after BRPLY L goes
  active.

The slave device responds to BDIN L negation by negating BRPLY L and removing
read data from BDAL bus drivers. BRPLY L must be negated 100 ns (maximum)
prior to removal of read data. The bus master responds to the negated BRPLY L
by negating BSYNC L. Conditions for the next BSYNC L assertion are as
follows.

* BSYNC L must remain negated for 200 ns (minimum).
* BSYNC L must not become asserted within 300 ns of previous BRPLY L
  negation.

Figure A-2 shows DATI bus cycle timing.

Figure A-2: DATI Bus Cycle Timing

> NOTE
>
> Continuous assertion of BSYNC L retains control of the bus by the bus
> master, and the previously addressed slave device remains selected. This is
> done for DATIO(B) bus cycles where DATO or DATOB follows a DATI without
> BSYNC L negation and a second device addressing operation. Also, a slow
> slave device can hold off data transfers to itself by keeping BRPLY L
> asserted, which causes the master to keep BSYNC L asserted.

### A.3.4 DATO(B)

Figure A-3: DATO or DATOB Bus Cycle

DATO(B), shown in Figure A-3, is a write operation. Data is transferred in
16-bit words (DATO) or 8-bit bytes (DATOB) from the bus master to the slave
device. The data transfer output can occur after the addressing portion of a
bus cycle when BWTBT L has been asserted by the bus master, or immediately
following an input transfer part of a DATIO(B) bus cycle.

The data transfer portion of a DATO(B) bus cycle comprises a data setup and
deskew time and a data hold and deskew time.

During the data setup and deskew time, the bus master outputs the data on
BDAL<15:00> L at least 100 ns after BSYNC L assertion. BWTBT L remains
negated for the length of the bus cycle. If the transfer is a byte transfer,
BWTBT L remains asserted. If it is the output of a DATIOB, BWTBT L becomes
asserted and lasts the duration of the bus cycle.

During a byte transfer, BDAL<00> L selects the high or low byte. This occurs
while in the addressing portion of the cycle. If asserted, the high byte
(BDAL<15:08> L) is selected; otherwise, the low byte (BDAL<07:00> L) is
selected. An asserted BDAL 16 L at this time forces a parity error to be
written into memory if the memory is a parity-type memory. BDAL 17 L is not
used for write operations. The bus master asserts BDOUT L at least 100 ns
after BDAL and BWTBT L bus drivers are stable. The slave device responds by
asserting BRPLY L within 10 μs to avoid bus timeout. This completes the data
setup and deskew time.

During the data hold and deskew time, the bus master receives BRPLY L and
negates BDOUT L, which must remain asserted for at least 150 ns from the
receipt of BRPLY L before being negated by the bus master. BDAL<17:00> L bus
drivers remain asserted for at least 100 ns after BDOUT L negation. The bus
master then negates BDAL inputs.

During this time, the slave device senses BDOUT L negation. The data is
accepted and the slave device negates BRPLY L. The bus master responds by
negating BSYNC L. However, the processor does not negate BSYNC L for at
least 175 ns after negating BDOUT L. This completes the DATO(B) bus cycle.
Before the next cycle, BSYNC L must remain unasserted for at least 200 ns.

Figure A-4 shows DATO(B) bus cycle timing.

Figure A-4: DATO or DATOB Bus Cycle Timing

### A.3.5 DATIO(B)

Figure A-5: DATIO or DATIOB Bus Cycle

The protocol for a DATIO(B) bus cycle is identical to the addressing and data
transfer portions of the DATI and DATO (B) bus cycles, and is shown in Figure
A-5. After addressing the device, a DATI cycle is performed as explained
earlier; however, BSYNC L is not negated. BSYNC L remains active for an
output word or byte transfer (DATO(B)). The bus master maintains at least 200
ns between BRPLY L negation during the DATI cycle and BDOUT L assertion. The
cycle is terminated when the bus master negates BSYNC L, as described for
DATO(B).

Figure A-6: DATIO or DATIOB Bus Cycle Timing

Figure A-6 illustrates DATIO(B) bus cycle timing.

## A.4 Direct Memory Access

The direct memory access (DMA) capability allows direct data transfer between
I/O devices and memory. This is useful when using mass storage devices (for
example, disks) that move large blocks of data to and from memory. A DMA
device needs to know only the starting address in memory, the starting
address in mass storage, the length of the transfer, and whether the
operation is read or write. When this information is available, the DMA
device can transfer data directly to or from memory. Since most DMA devices
must perform data transfers in rapid succession or lose data, DMA devices are
provided the highest priority.

DMA is accomplished after the processor (normally bus master) has passed bus
mastership to the highest-priority DMA device that is requesting the bus. The
processor arbitrates all requests and grants the bus to the DMA device
electrically closest to it. A DMA device remains bus master until it
relinquishes its mastership. The following control signals are used during
bus arbitration.

| Signal      | Description                        |
| ----------- | ---------------------------------- |
| BDMR L      | DMA request line                   |
| BDMGI L     | DMA grant input                    |
| BDMGO L     | DMA grant output                   |
| BSACK L     | Bus grant acknowledge              |

### A.4.1 DMA Protocol

A DMA transaction can be divided into three phases:

1. bus mastership acquisition phase;
2. data transfer phase;
3. bus mastership relinquishment phase.

During the bus mastership acquisition phase, a DMA device requests the bus by
asserting BDMR L. The processor arbitrates the request and initiates the
transfer of bus mastership by asserting BDMGO L.

The maximum time between BDMR L assertion and BDMGO L assertion is DMA
latency. This time is processor-dependent. BDMGO L/BDMGI L is one signal that
is daisy-chained through each module in the backplane. It is driven out of
the processor on the BDMGO L pin, enters each module on the BDMGI L pin, and
exits on the BDMGO L pin. This signal passes through the modules in
descending order of priority until it is stopped by the requesting device.
The requesting device blocks the output of BDMGO L and asserts BSACK L. If
BDMR L is continuously asserted, the bus hangs. During the data transfer
phase, the DMA device continues asserting BSACK L. The actual data transfer
is performed as described earlier.

The DMA device can assert BSYNC L for a data transfer 250 ns (minimum) after
it received BDMGI L and its BSYNC L bus receiver becomes negated.

During the bus mastership relinquishment phase, the DMA device gives up the
bus by negating BSACK L. This occurs after completing (or aborting) the last
data transfer cycle (BRPLY L negated). BSACK L may be negated up to a maximum
of 300 ns before negating BSYNC L. Figure A~7 shows the DMA protocol, and
Figure A-8 shows DMA request/grant timing.

> NOTE
>
> If multiple data transfers are performed during this phase, consideration
> must be given to the use of the bus for other system functions, such as
> memory refresh (if required).

Figure A~7: DMA Protocol

Figure A-8: DMA Request/Grant Timing

### A.4.2 Block Mode DMA

For increased throughput, block mode DMA may be implemented on a device for
use with memories that support this type of transfer. In a block mode
transaction, the starting memory address is asserted, followed by data for
that address, and data for consecutive addresses.

By eliminating the assertion of the address for each data word, the transfer
rate is almost doubled. The DATBI and DATBO bus cycles are described below.

#### A.4.2.1 DATBI

The device addressing portion of the cycle is the same as described earlier
for other bus cycles. (See Figure A-9.) The bus master gates BDAL<21:00>,
BBS7, and the negation of BWTBT onto the bus.

Figure A-9: DATBI Bus Cycle Timing

The master asserts the first BDIN 100 ns after BSYNC, and asserts BBS7 a
maximum of 50 ns after asserting BDIN for the first time. BBS7 is a request
to the slave for a block mode transfer. BBS7 remains asserted until a maximum
of 50 ns after the assertion of BDIN for the last time. BBS7 may be gated as
soon as the conditions for asserting BDIN are met.

The slave asserts BRPLY a minimum of 0 ns (8 μs maximum to avoid bus timeout)
after receiving BDIN. It asserts BREF concurrently with BRPLY if it is a
block mode device capable of supporting another BDIN after the current one.
The slave gates BDAL<15:00> onto the bus 0 ns (minimum) after the assertion
of BDIN, and 125 ns (maximum) after the assertion of BRPLY.

The master receives the stable data from 200 ns (maximum) after the assertion
of BRPLY until 20 ns (minimum) after the negation of BDIN. It negates BDIN
200 ns (minimum) after the assertion of BRPLY.

The slave negates BRPLY 0 ns (minimum) after the negation of BDIN. If BBS7
and BREF are both asserted when BRPLY is negated, the slave prepares for
another BDIN cycle. BBS7 is stable from 125 ns after BDIN is asserted until
150 ns after BRPLY is negated. The master asserts BDIN 150 ns (minimum) after
BRPLY is negated, and the cycle is continued as before. (BBS7 remains
asserted and the slave responds to BDIN with BRPLY and BREF.) BREF is stable
from 75 ns after BRPLY is asserted until 20 ns (minimum) after BDIN is
negated.

If BBS7 and BREF are not both asserted when BRPLY is negated, the slave
removes the data from the bus 0 ns (minimum) and 100 ns (maximum) after
negating BRPLY. The master negates BSYNC 250 ns (minimum) after the assertion
of the last BRPLY, and 0 ns (minimum) after the negation of that BRPLY.

#### A.4.2.2 DATBO

The device addressing portion of the cycle is the same as shown in Figure
A-10. The bus master gates BDAL<21:00>, BBS7, and the assertion of BWTBT onto
the bus.

Figure A-10: DATBO Bus Cycle Timing

A minimum of 100 ns after BSYNC is asserted, data on BDAL<15:00> and the
negated BWTBT are put onto the bus. The master then asserts BDOUT a minimum
of 100 ns after gating the data.

The slave receives stable data and BWTBT from 25 ns (minimum) before the
assertion of BDOUT to 25 ns (minimum) after the negation of BDOUT. The slave
asserts BRPLY 0 ns (minimum) after receiving BDOUT. It also asserts BREF
concurrently with BRPLY if it is a block mode device capable of supporting
another BDOUT after the current one.

The master negates BDOUT 150 ns (minimum) after the assertion of BRPLY. If
BREF was asserted when BDOUT was negated, and the master wants to transmit
more data in this block mode cycle, the new data is gated onto the bus 100 ns
(minimum) after BDOUT is negated. BREF is stable from 75 ns (maximum) after
BRPLY is asserted until 20 ns (minimum) after BDOUT is negated. The master
asserts BDOUT 100 ns (minimum) after gating new data onto the bus and 150 ns
minimum after BRPLY negates. The cycle continues as before.

If BREF was not asserted when BDOUT was negated, or if the bus master does
not want to transmit more data in this cycle, the master removes data from
the bus 100 ns (minimum) after negating BDOUT. The slave negates BRPLY 0 ns
(minimum) after negating BDOUT. The bus master negates BSYNC 175 ns (minimum)
after negating BDOUT, and 0 ns (minimum) after the negation of BRPLY.

### A.4.3 DMA Guidelines

1. Systems with memory refresh over the bus must not include devices that
   perform more than one transfer per acquisition.

2. Bus masters that do not use block mode are limited to four DATI, four
   DATO, or two DATIO transfers per acquisition.

3. Block mode bus masters that do not monitor BDMR are limited to eight
   transfers per acquisition.

4. If BDMR is not asserted after the seventh transfer, block mode bus masters
   that do monitor BDMR may continue making transfers until the bus slave
   fails to assert BREF, or until they reach the total maximum of 16
   transfers. Otherwise, they stop after eight transfers.

## A.5 Interrupts

The interrupt capability of the Q22-Bus allows an I/O device to temporarily
suspend (interrupt) current program execution and divert processor operation
to service the requesting device. The processor inputs a vector from the
device to start the service routine (handler). Like the device register
address, hardware fixes the device vector at locations within a designated
range below location 001000. The vector indicates the first of a pair of
addresses. The processor reads the contents of the first address, the
starting address of the interrupt handler. The contents of the second address
is a new processor status word (PS).

The new PS can raise the interrupt priority level, thereby preventing
lower-level interrupts from breaking into the current interrupt service
routine. Control is returned to the interrupted program when the interrupt
handler is ended. The original interrupted program's address (PC) and its
associated PS are stored on a stack. The original PC and PS are restored by a
return from interrupt (RTI or RTT) instruction at the end of the handler. The
use of the stack and the Q22-Bus interrupt scheme can allow interrupts to
occur within interrupts (nested interrupts), depending on the PS.

Interrupts can be caused by Q22-Bus options or the MicroVAX CPU. Those
interrupts that originate from within the processor are called “traps”. Traps
are caused by programming errors, hardware errors, special instructions, and
maintenance features.

The following are Q22-Bus signals used in interrupt transactions.

| Signal      | Description                        |
| ----------- | ---------------------------------- |
| BIRQ4 L     | Interrupt request priority level 4 |
| BIRQS L     | Interrupt request priority level 5 |
| BIRQ6 L     | Interrupt request priority level 6 |
| BIRQ7 L     | Interrupt request priority level 7 |
| BIAKI L     | Interrupt acknowledge input        |
| BIAKO L     | Interrupt acknowledge output       |
| BDAL<21:00> | Data/address lines                 |
| BDIN L      | Data input strobe                  |
| BRPLY L     | Reply                              |

### A.5.1 Device Priority

The Q22-Bus supports the following two methods of device priority.

1. Distributed Arbitration — Priority levels are implemented on the hardware.
   When devices of equal priority level request an interrupt, priority is
   given to the device electrically closest to the processor.

2. Position-Defined Arbitration — Priority is determined solely by electrical
   position on the bus. The closer a device is to the processor, the higher
   its priority is.

### A.5.2 Interrupt Protocol

Interrupt protocol on the Q22-Bus has three phases: the interrupt request
phase, interrupt acknowledge and priority arbitration phase, and interrupt
vector transfer phase. Figure A-11 shows the interrupt request/acknowledge
sequence.

Figure A-11: Interrupt Request/Acknowledge Sequence

The interrupt request phase begins when a device meets its specific
conditions for interrupt requests. For example, the device is ready, done, or
an error has occurred. The interrupt enable bit in a device status register
must be set. The device then initiates the interrupt by asserting the
interrupt request line(s). BIRQ4 L is the lowest hardware priority level and
is asserted for all interrupt requests for compatibility with previous Q22
processors. The level at which a device is configured must also be asserted.
A special case exists for level 7 devices that must also assert level 6. For
an explanation, refer to the discussion below on arbitration involving the
4-level scheme.

| Interrupt Level | Lines Asserted by Device  |
| --------------- | ------------------------- |
| 4               | BIRQ4 L                   |
| 5               | BIRQ4 L, BIRQ5 L          |
| 6               | BIRQ4 L, BIRQ6 L          |
| 7               | BIRQ4 L, BIRQ6 L, BIRQ7 L |

The interrupt request line remains asserted until the request is
acknowledged.

During the interrupt acknowledge and priority arbitration phase, the
LSI-11/23 processor acknowledges interrupts under the following conditions.

1. The device interrupt priority is higher than the current PS<7:5>.
2. The processor has completed instruction execution and no additional bus
   cycles are pending.

The processor acknowledges the interrupt request by asserting BDIN L, and 150
ns (minimum) later asserting BIAKO L. The device electrically closest to the
processor receives the acknowledge on its BIAKI L bus receiver.

At this point, the two types of arbitration must be discussed separately. If
the device that receives the acknowledge uses the 4-level interrupt scheme,
it reacts as follows.

1. If not requesting an interrupt, the device asserts BIAKO L and the
   acknowledge propagates to the next device on the bus.

2. If the device is requesting an interrupt, it must check that no
   higher-level device is currently requesting an interrupt. This is done by
   monitoring higher-level request lines. The table below lists the lines
   that need to be monitored by devices at each priority level.

   In addition to asserting levels 7 and 4, level 7 devices must drive
   level 6. This is done to simplify the monitoring and arbitration by level
   4 and 5 devices. In this protocol, level 4 and 5 devices need not monitor
   level 7 because level 7 devices assert level 6. Level 4 and 5 devices
   become aware of a level 7 request because they monitor the level 6
   request. This protocol has been optimized for level 4, 5, and 6 devices,
   since level 7 devices are very seldom necessary.

| Device Priority Level | Line(s) Monitored |
| --------------------- | ----------------- |
| 4                     | BIRQ5, BIRQ6      |
| 5                     | BIRQ6             |
| 6                     | BIRQ7             |
| 7                     | —                 |

3. If no higher-level device is requesting an interrupt, the acknowledge is
   blocked by the device. (BIAKO L is not asserted.) Arbitration logic within
   the device uses the a leading edge of BDIN L to clock a flip-flop that
   blocks BIAKO L. Arbitration is won, and the interrupt vector transfer
   phase begins.

4. If a higher-level request line is active, the device disqualifies itself
   and asserts BIAKO L to propagate the acknowledge to the next device along
   the bus.

Signal timing must be considered carefully when implementing 4-level
interrupts. See Figure A-12.

Figure A-12: Interrupt Protocol Timing

If a single-level interrupt device receives the acknowledge, it reacts as
follows.

1. If not requesting an interrupt, the device asserts BIAKO L and the
   acknowledge propagates to the next device on the bus.

2. If the device was requesting an interrupt, the acknowledge is blocked using
   the leading edge of BDIN L, and arbitration is won. The interrupt vector
   transfer phase begins.

The interrupt vector transfer phase is enabled by BDIN L and BIAKI L. The
device responds by asserting BRPLY L and its BDAL<15:00> L bus driver inputs
with the vector address bits. The BDAL bus driver inputs must be stable
within 125 ns (maximum) after BRPLY L is asserted. The processor then inputs
the vector address and negates BDIN L and BIAKO L. The device then negates
BRPLY L and 100 ns (maximum) later removes the vector address bits. The
processor then enters the device's service routine.

> NOTE
>
> Propagation delay from BIAKI L to BIAKO L must not be greater than 500 ns
> per Q22-Bus slot.
>
> The device must assert BRPLY L within 10 μs (maximum) after the processor
> asserts BIAKI L.

### A.5.3 4-Level Interrupt Configurations

If you have high-speed peripherals and desire better software performance,
you can use the 4-level interrupt scheme. Both position-independent and
position-dependent configurations can be used with the 4-level interrupt
scheme.

Figure A-13 shows the position-independent configuration. This allows
peripheral devices that use the 4-level interrupt scheme to be placed in the
backplane in any order. These devices must send out interrupt requests and
monitor higher-level request lines as described. The level 4 request is
always asserted from a requesting device regardless of priority. If two or
more devices of equally high priority request an interrupt, the device
physically closest to the processor wins arbitration. Devices that use the
single-level interrupt scheme must be modified, or placed at the end of the
bus, for arbitration to function properly.

Figure A-14: Position-Dependent Configuration

Figure A-14 shows the position-dependent configuration. This configuration is
simpler to implement. A constraint is that peripheral devices must be
inserted with the highest-priority device located closest to the processor,
and the remaining devices placed in the backplane in decreasing order of
priority (with the lowest-priority devices farthest from the processor). With
this configuration, each device has to assert only its own level and level 4.
Monitoring higher-level request lines is unnecessary. Arbitration is achieved
through the physical positioning of each device on the bus. Single-level
interrupt devices on level 4 should be positioned last on the bus.

