# derpcode #

A joke esoteric language based on internet slang.

## Structure ##

derpcode consists of two objects: a one-ended *tape* of zero-initialized binary values, and a *pointer* 
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
    <td>.</td><td>Write the current bit and the next seven bits to the screen as an ASCII character.</td>
  </tr>
</table>

## Termination ##

A derpcode program is terminated by decrementing the pointer to -1 after flipping the 0 value, and running the 
print command. The last line of all derpcode programs is therefore:

`herp a-derp.`

## Hello World ##

The following derpcode program prints the phrase "Hello world!" to the screen, and exits.

```

derp herp derp derp derp herp a-derp a-derp a-derp a-derp. 
derp derp herp derp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp derp derp derp herp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp..
derp derp derp derp derp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.

```
