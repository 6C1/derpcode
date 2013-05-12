# derpcode #

A joke esoteric language based on internet slang.

## Structure ##

derpcode consists of three objects: a one-ended tape of binary values, a pointer (i.e., Turing "head"), and a 
print buffer.

## Library ##

<table>
  <tr>
    <td><b>Command</b></td><td><b>Description</b></td>
  </tr>
  <tr>
    <td>`herp`</td><td>Flip the current bit.</td>
  </tr>
  <tr>
    <td>`derp`</td><td>Increment the pointer.</td>
  </tr>
  <tr>
    <td>`a-derp`</td><td>Decrement the pointer.</td>
  </tr>
  <tr>
    <td>`.`</td><td>Write the current bit to the print buffer</td>
  </tr>
</table>

## Printing ##

The print buffer is an 8-bit stack, written to via the `.` command. When the stack fills, it automatically
writes the contents to the `stdout` as a single ASCII character.
