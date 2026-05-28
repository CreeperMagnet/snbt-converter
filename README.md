This repository contains code to [run Minecraft's data generators](https://minecraft.wiki/w/Tutorial:Running_the_data_generator) to process nbt files (most commonly found as structure template files) into snbt files.

In order to run this, you need a file named config.py with the following contents:

```
import os
target_path = os.path.abspath(<your path here>)
```

From there, you can stringify nbt into snbt, or unstringify snbt into nbt.

Since snbt is, well, stringified, this allows you to directly edit nbt files in text form and easily use other tools such as find & replace.

> [!CAUTION]
> Use this at your own risk.
> Version-control your files using git to prevent stupid mistakes.
> This is designed for my usecase and my usecase only. It will delete files if you point this at a folder that has non-nbt files.
> If you have no idea what nbt is, do not use this project.