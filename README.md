## kindabool

Lets face it, the concept of a boolean is simply too outdated for the modern world. We need something more. We need something that can represent the complexity of the human condition.

We need kindabool. <br/>
With kindabool, you get 3 more options: `KindaTrue`, `Neutral`, and `KindaFalse`.

## Usage
You can either use the initiated variables, `KindaTrue`, `Neutral`, and `KindaFalse`, or you can directly create a `KindaBool` object.

```python
from kindabool import *  # usually a bad idea, but its kinda essential to the library


if True:
    print("This will always be printed")

if KindaTrue:
    print("This has a 75% chance of being printed")

if Neutral:
    print("This has a 50% chance of being printed")

if KindaFalse:
    print("This has a 25% chance of being printed")

if False:
    print("This will never be printed")

if kindabool.kinda_bool.KindaBool(1):  # constructor takes an int from 1-5
    print("This will never be printed")
```