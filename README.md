This repository contains code to [run Minecraft's data generators](https://minecraft.wiki/w/Tutorial:Running_the_data_generator) to process nbt files (most commonly found as structure template files) into snbt files.

Since snbt is, well, stringified nbt, these scripts allow you to directly edit nbt files in text form and easily use other tools such as find & replace.




In order to run this, you need a file named config.py with the following contents:
```
import os
target_path = os.path.abspath(<your path here>)
```
This determines which folder will be targeted by the stringify/unstringify scripts.

From there, you can stringify nbt into snbt, or unstringify snbt into nbt.

This requires the ID of the specific version you're working on. These can be found on the [version manifest](https://launchermeta.mojang.com/mc/game/version_manifest.json).

> [!CAUTION]
> Use this at your own risk. Version-control your files using git to prevent stupid mistakes.
>
> This is designed for my usecase and my usecase only. It will delete files if you point this at a folder that has non-nbt files.
>
> If you have no idea what nbt is, do not use this project.