# Gmod-cached-server-addon-extractor
A python script that extracts server client-side lua scripts from the compressed files saved in the cache folder.

## why?
I spent hours looking for a script that could extract gmods lzma compressed files but i couldn't find one that worked, so i made this one!

## How it works
- First python opens the compressed binary file and removes the first 32 bytes. It does this because the gmod lzma files use different headers from regular lzma files and doing this is the only way the next step works. This file is then saved in the temp folder. </br>
- Next python runs `.\lzma d <temp file> <save file>` this decodes the temp file and saves it as the save file. </br>
- Once all files are decoded and saved, python clears the temp folder and quits. </br>
- **Ensure you empty the output folder before running the script again to avoid overwriting files as the same names are used every time.**

## Setup
The only setup is downloading the code unless you don't want to run the lzma.exe I have included. You can get it from 7zip [here](https://www.7-zip.org/sdk.html) in the bin directory of the lzma sdk.
