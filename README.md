# OneDnDCharacterCreator

This project is intended to be a way to keep character sheets up to date with OneD&amp;D UA releases as well as have the
ability to create new characters.

## To Run

```
python3 main.py CHARACTER1 CHARACTER2 --sources srd CUSTOMSOURCE1 CUSTOMSOURCE2 odnd1 odnd2 odnd3 odnd4
```

The order the sources are included is important because newer entries will overwrite older ones.

## What's included

I currently have in the `characters` folder the characters I have made for my own campaigns.
Due to not legally being able to distribute books other than the SRD and the UA, the `extra_sources` folder is where
you can place other books. It is a private repo because I have made most of them for myself but I cannot distribute.