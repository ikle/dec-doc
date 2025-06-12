# Chapter 1. Introduction

This publication is a handbook for Digital Equipment Corporation’s PDP-11. It
provides a comprehensive overview of the system structure, the instruction
repertoire, input/output programming, peripherals, general interfacing,
software, and console operation.

PDP-11 is Digital’s answer to the demand for a modular system for real-time
data acquisition, analysis and control. PDP-11 systems can handle a wide
variety of real-time control applications — each system being individually
tailored from a comprehensive array of modular building blocks. Digital is
unique among manufacturers of small-scale computers in its ability to provide
not only fast and efficient processing units, but also a large family of its
own compatible I/O devices including A/D and D/A converters, magnetic tape,
disk storage, paper tape, and displays, as well as a wide range of
general-purpose modules. This capability offers the user a new, more
efficient approach to real-time systems.

The following paragraphs introduce the new PDP-11 by way of highlighting
several of the important design features that set it apart from other
machines in its class. Subsequent chapters of this manual place these
features in their proper context and provide detailed descriptions of each.

## PDP-11 Systems

The PDP-11 is available in two versions designated as PDP-11/10 and
PDP-11/20. The PDP-11/10 contains a KA11 processor, 1,024 words of 16-bit
read-only memory, and 128 16-bit words of read-write memory. The basic
PDP-11/20 contains a KA11 processor and 4,096 words of 16-bit read-write core
memory, a programmer’s console, and an ASR-33 Teletype. Both versions can be
similarly expanded with either read-write or read-only memory and peripheral
devices.

## Unibus

Unibus is the name given to the single bus structure of the PDP-11. The
processor, memory and all peripheral devices share the same high-speed bus.
The Unibus enables the processor to view peripheral devices as active memory
locations which perform special functions. Peripherals can thus be addressed
as memory. In other words, memory reference instructions can operate directly
on control, status, or data registers in peripheral devices. Data transfers
from input to output devices can bypass the processor completely.

## KA11 Processor

The KA11 processor incorporates a unique combination of powerful features not
previously available in 16-bit computers.

### Priority Interrupts

A four-level automatic priority interrupt system permits the processor to
respond automatically to conditions outside the system, or in the processor
itself. Any number of separate devices can be attached to each level.

Each peripheral device in a PDP-11 system has a hardware pointer to its own
unique pair of memory locations which, in turn, point to the device’s service
routine. This unique identification eliminates the need for polling of
devices to identify an interrupt, since the interrupt servicing hardware
selects and begins executing the appropriate service routine.

The device’s interrupt priority and service routine priority are independent.
This allows dynamic adjustment of system behavior in response to real-time
conditions.

The interrupt system allows the processor continually to compare its own
priority levels with the levels of any interrupting devices and to
acknowledge the device with the highest level above the processor’s priority
level. Servicing an interrupt for a device can be interrupted for servicing a
higher priority device. Service to the lower priority device can be resumed
automatically upon completion of the higher level servicing. Such a process,
called nested interrupt servicing, can be carried out to any level.

### Reentrant Code

Both the interrupt handling hardware and the subroutine call hardware are
designed to facilitate writing reentrant code for the PDP-11. This type of
code allows use of a single copy of a given subroutine or program to be
shared by more than one process or task. This reduces the amount of core
needed for multi-task applications such as the concurrent servicing of many
peripheral devices.

### General Register

The PDP-11 is equipped with eight general registers. All are
program-accessible and can be used as accumulators, as pointers to memory
locations, or as full-word index registers. Six registers are used for
general-purpose access while the seventh and eighth registers are used as a
stack pointer and program counter respectively.

### Instruction Set

An important feature of the PDP-11 instruction set is the availability of
double operand instructions. These instructions allow memory-to-memory
processing and eliminate the need to use registers for storage of
intermediate results. By using double operand instructions, every memory
location can be treated as an accumulator. This significantly reduces the
length of programs by eliminating load and store operations associated with
single operand machines.

### Addressing

Much of the power of the PDP-11 is derived from its wide range of addressing
capabilities. PDP-11 addressing modes include list sequential addressing,
full address indexing, full 16-bit word addressing, 8-bit byte addressing,
stack addressing, and direct addressing to 32K words.

Variable length instruction formatting allows a minimum number of bits to be
used for each addressing mode. This results in efficient use of program
storage space.

### Asynchronous Operation

The PDP-11’s memory and processor operations are asynchronous. As a result,
I/O devices transferring directly to or from memory may steal memory cycles
during instruction operation.

## Packaging

The PDP-11 has adopted a modular approach to allow custom configuring of
systems, easy expansion, and easy servicing. Systems are composed of basic
building blocks, called System Units, which are completely independent
subsystems connected only by pluggable Unibus and power connections.

There is no fixed wiring between them. An example of this type of subsystem
is a 4,096-word memory module.

System Units can be mounted in many combinations within the PDP-11 hardware,
since there are no fixed positions for memory or I/O device controllers.
Additional units can be mounted easily and connected to the system in the
field. In case maintenance is required, defective System Units can be
replaced with spares and operation resumed within a few minutes.

## Software

A complete package of user-oriented software includes:

* Absolute assembler providing object and source listings.
* String-oriented editor.
* Debugging routines capable of operating in a priority interrupt environment.
* Input/output handlers for standard peripherals.
* Relocatable integer and floating point math library.

* * *

![Pic 1-1](i/pic-012-1.jpg "All PDP-11 processors, memories and peripherals
are electrically and mechanically modular subsystems supported in System
Units which are simply plugged together to form a computer tailored to user
needs.")

All PDP-11 processors, memories and peripherals are electrically and
mechanically modular subsystems supported in System Units which are simply
plugged together to form a computer tailored to user needs.

