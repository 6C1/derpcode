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
</table>

## Syntax ##

Any symbols (including whitespace) which are not defined in the above library table are ignored by the interpreter.

### Initiation ###

Every derpcode program initiates with the commands `derp a-derp`.

### Termination ###

A derpcode program is terminated by decrementing the pointer to -1 after flipping the 0 value, and running the 
print command. The last line of all derpcode programs is therefore:

`herp a-derp.`

## Implementations ##

Implementations planned include:

- [ ] Python-based runtime interpreter (in development).
- [ ] Compiler down to C, in C.

## Sample Programs ##

### Hello World ###

The following derpcode program prints the phrase "Hello world!" to the screen, and exits.

```
derp a-derp.

derp herp derp derp derp herp a-derp a-derp a-derp a-derp. 
derp derp herp derp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp derp derp derp herp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
.
derp derp derp derp derp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.

derp herp derp derp derp herp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp herp derp derp herp derp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp derp derp herp derp herp a-derp a-derp a-derp.
derp derp derp herp derp herp derp herp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.
derp derp derp herp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.

derp derp derp derp herp a-derp a-derp a-derp a-derp.
derp herp derp derp derp derp herp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp.

herp a-derp.
```
## Obfuscation ##

As derpcode is based on widespread internet slang, its ease of human readability is hard to avoid. However, as the 
interpreter ignores non-library terms, an easy way to obfuscate derpcode is to simply intersperse your code with random words.

### Obfuscated Hello World ###

```
My mother drove me to the airport with the windows rolled down. It was seventy-five degrees in Phoenix, the sky a perfect, cloudless blue. I was wearing my favorite shirt - sleeveless, white eyelet lace; I was wearing it as a farewell gesture. My carry-on item was a parka. 
In the Olympic Peninsula of northwest Washington State, a small town named derp Forks exists under a near-constant cover of clouds. It rains on this inconsequential town more than any other place in the United States of America. It was from this town and its gloomy, omnipresent shade that my mother escaped with me when I was only a few months old. It was in this town that I'd been compelled to spend a month every summer until I was fourteen. That was the year I finally put my foot down; these past three summers, my dad, Charlie, vacationed with me in California for two weeks instead. 
It was to Forks that I now exiled myself a-derp. - an action that I took with great horror. I detested derp Forks. 
I loved Phoenix. I loved the sun and the blistering heat. I loved the vigorous, sprawling city. 
"Bella," my mom said to me - the last of a thousand times - before I got on the plane. "You don't have to do this." 
My mom looks like me, except with short hair and laugh lines. I felt a spasm of panic as I stared at her wide, childlike eyes. How could I leave my loving, erratic, hair-brained mother to fend for herself? Of course she had Phil now, so the bills would probably get paid, there would be food in the refrigerator, gas in her car, and someone to call when she got lost, but still... 
"I want to go herp ," I lied. I'd always been a bad liar, but I'd been saying this lie so frequently lately that it sounded almost convincing now. 
"Tell derp Charlie I said hi." 
"I will." 
"I'll see you soon," she insisted. "You can come home whenever you want - I'll come right back as soon as you need me." 
But I could see the sacrifice in her eyes behind the promise. 
"Don't worry about me," I urged. "It'll be great. I love you, derp Mom." 
She hugged my tightly for a minute, and then I got on the plane, and she was gone. 
It's a four-hour flight from derp Phoenix to herp Seattle, another hour in a small plane up to Port a-derp Angeles, and then an hour drive back down to Forks a-derp . Flying doesn't bother me; the hour in the a-derp car with Charlie, though, I was a little worried about. 
Charlie had really been fairly nice about the whole thing. He seemed genuinely please that I was comeing to live with him for the first time with any degree of permanence. He'd already gotten me registered for high school and was going to help me get a car. 
But it was sure to be awkward with Charlie. Neither of us was what anyone would call verbose, and I didn't know what there was to say regardless. a-derp. I knew he was more than a little confused by my decision - like my mother before me, I hadn't made a secret of my distaste for Forks. 
When I landed in Port Angeles, it was raining. I didn't see it as a derp omen - just unavoidable. I'd already said my goodbyes to the sun. 
Charlie was waiting for me with the cruiser. This I was expecting, too. Charlie is Police Cheif derp Swan to the good people of Forks. My primary motivation behind buying a car, despite the scarcity of my funds, was that I refused to be driven around town in a car with red and blue lights on top. Nothing slows traffic down like a cop. 
Charlie gave me an awkward, one-armed hug when I stumbled my way off the plane. 
"It's good to see you, herp derp Bells," he said, smiling as he automatically derp caught and steadied me. "You haven't changed much. How's herp Renee?" 
"Mom's derp fine. It's good to see you, too, herp Dad." I wasn't allowed to call him derp Charlie to his face. 
I had only a few bags. Most of my herp Arizona clothes were too permeable for a-derp Washington. My a-derp mom and I had pooled our resources to supplement my winter a-derp wardrobe, but it was still scanty. It all fit easily into the trunck of the a-derp cruiser. 
"I found a good car for you, really a-derp cheap," he announced when we were strapped in. 
"What kind of a-derp  car?" I was suspicious of the way he said "good a-derp. car for you" as opposed to just "good derp car."
"Well, it's a derp truck actually, a derp Chevy." 
"Where did you find it?" 
"Do you remember Billy derp Black from La herp Push?" La derp Push is the tiny Indian reservation on the derp coast. 
"No." 
"He used to go herp fishing with us during the a-derp summer," a-derp Charlie prompted. 
That would a-derp explain why I didn't remember him. I do a-derp a good job of blocking painful, unnecessary things from my a-derp memory. 
"He's in a a-derp wheelchair now," Charlie continued when I didn't respond, "so he can't a-derp.. drive anymore, and he offered to sell me his truck derp cheap." 
"What derp year is it?" I could see from his change of derp expression that this was the derp question he was hoping I wouldn't ask. 
"Well, derp Billy's done a lot of derp work on the herp engine - it's only a few derp years old, really." 
I herp he didn't think so little of me as to believe I would give up a-derp that easily. "When did he buy a-derp it?" 
"He bought it in 1984, I a-derp think." 
"Did he buy it a-derp new?" 
"Well, no. I think it was a-derp new in the early a-derp sixties - or late a-derp. Fifties at the derp earliest," he admitted herp sheepishly. 
"Ch - derp Dad, I don't really know anything about derp cars. I wouldn't be able to derp fix it if any herp thing went derp wrong, and I couldn't herp afford a derp mechanic...." 
"Really, herp Bella, the thing runs derp great. They don't herp build them like that a-derp anymore." 
The thing a-derp , I thought to myself a-derp ... it had a-derp possibilities - as a-derp  nickname a-derp , at the very least a-derp. 
"How derp cheap is herp cheap?" After derp all, that was the derp part I couldn't herp compromise derp on. 
"Well, derp honey, I kind of already herp bought it for you. As a homecoming derp gift." herp Charlie peeked derp sideways at me with a hopeful herp expression. 
Wow. a-derp Free. 
"You didn't need a-derp  to do that, Dad. I was going to buy myself a-derp car." 
"I don't mind. I want a-derp you to be happy a-derp here." He was looking a-derp ahead at the road when he said a-derp. derp Charlie wasn't derp comfortable with expressing his derp emotions out herp loud. I inherited that derp from him. So I was herp looking straight a-derp ahead as I responded a-derp a-derp.
"That's really nice, derp Dad. Thanks. I really derp appreciate it." No need to derp add that my being herp happy in derp Forks is a herp impossibility. He didn't need to derp suffer along with me. And I never herp looked a free truck in the derp mouth - or derp engine. 
"Well herp, a-derp now, you're a-derp welcome." ne mumbled, a-derp  embarrassed by my a-derp thanks. 
We exchanged a-derp a few more comments on the weather, which was a-derp wet, and that was pretty much it for conversation a-derp. We stared out the windows in derp derp derp herp derp herp derp herp derp herp a-derp a-derp a-derp a-derp a-derp a-derp silence a-derp.
"derp derp derp derp herp a-derp a-derp a-derp a-derp."
"derp herp derp derp derp derp herp derp derp herp a-derp a-derp a-derp a-derp a-derp a-derp a-derp."

herp a-derp.

```
