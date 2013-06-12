# derpcode #

A tape-based esoteric language based on internet slang.

## Structure ##

derpcode consists of two objects: a one-ended **tape** of zero-initialized binary values, and a **pointer** 
(i.e., Turing "head").

## Library ##

<table>
  <tr>
    <td><b>Command</b></td><td><b>Description</b></td>
  </tr>
  <tr>
    <td>herp</td><td>Flip the current bit.</td>
  </tr>
  <tr>
    <td>derp</td><td>Increment the pointer.</td>
  </tr>
  <tr>
    <td>a-derp</td><td>Decrement the pointer.</td>
  </tr>
  <tr>
    <td>.</td><td>Write the current bit and the next seven bits to stdout as an ASCII character.</td>
  </tr>
  <tr>
    <td>?</td><td>Get an ASCII character from stdin and store it in the current bit and the next seven bits.</td>
  </tr>
  <tr>
    <td>!</td><td>If current bit c == 1, concatenate c+4 through c+7, interpret as a 4-bit binary number d, and increment the pointer d steps.</td>
  </tr>
</table>

## Syntax ##

Any words and symbols (including whitespace) which are not defined in the above library table are ignored by the interpreter.

### Initiation ###

Every derpcode program initiates with the commands `derp a-derp`.

### Termination ###

A derpcode program is terminated by decrementing the pointer to -1 after flipping the 0 value, and running the 
print command. The last line of all derpcode programs is therefore:

`herp a-derp.`

## Implementations ##

Implementations planned include:

- [ ] python-based runtime interpreter (in development).
- [ ] compiler down to C, in C.

## Sample Programs ##

### Hello World ###

The following derpcode program prints the phrase "Hello world!" to the screen, and exits.

```
derp a-derp.

derp herp derp derp derp herp a-derp a-derp a-derp a-derp.
derp derp herp derp derp herp derp herp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp derp derp derp herp derp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
.
derp derp derp derp derp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.

derp herp derp derp derp herp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp herp derp derp herp derp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp derp derp herp derp herp a-derp a-derp a-derp a-derp.
derp derp derp herp derp herp derp herp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp derp derp herp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp.

derp derp derp derp herp a-derp a-derp a-derp a-derp.
derp herp derp derp derp derp herp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.

herp a-derp.
```
## Obfuscation ##

As derpcode is based on widespread internet slang, its ease of human readability is hard to avoid. However, as the 
interpreter ignores non-library terms, an easy way to obfuscate derpcode is to simply intersperse your code within
another text document.
