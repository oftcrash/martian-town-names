Martian Town Names - A town name generator for OpenTTD

==============================
Current Version: Martian Town Names 1.0.1
==============================

Contents
1 About Martian Town Names
2 Downloading and Installing Martian Town Names
3 Obtaining Source Files
4 Building Martian Town Names
5 Reporting Bugs and Contributing
6 License


1 About Martian Town Names
==========================

Martian Town Names is a newgrf for OpenTTD that uses real Martian geographic features to create town names during creation of
a map at the start of an OpenTTD game. The names are assembled from lists found on Wikipedia.

Names on Mars are generally given a base name, then assigned a fairly standard prefix or suffix. Olympus Mons, for example,
has a base name of Olympus and a suffix of Mons, meaning mountain. There are numerous others.

Names are constructed 4 ways.
* The real name, taken as is, and plunked into the game
* Just the base name, stripped of any prefix or suffix
* Random prefix plus a random base name
* Random base name plus a random suffix

The most common is the last, random base plus suffix, in keeping with the general pattern of naming on Mars.

As of this writing, its not possible to assign land features in names to corresponding features on the map. Mare Australae,
for example, would imply a town next to a sea, or Cydonia Planum a town on an open plain. Alas, maybe someday in the future this can be done.


2 Downloading and Installing Martian Town Names
===============================================

Martian Town Names is available from Bananas, the in-game content download service in OpenTTD. Any other download locations
may not be the original or the latest version.


3 Obtaining Source Files
========================

At the time of this writing, the source for this newgrf is available at:
https://github.com/oftcrash/martian-town-names

No guarantee is made that the source is still available at that location by the time you read this, however.


4 Building Martian Town Names
=============================
Martian Town Names is built using a python build script that constructs NML, then uses NMLC to actually compile the file.
It requires Python 2.6 (3.0 won't work), plus Jinja2 template libraries. I freely admit its kind of an ugly build script, but take it as it is and improve it, or just grab the final NML from the build directory.

5 Reporting bugs and contributing
=================================

If you notice any bugs, incorrect data, or what to contribute, you can submit an issue to project the source control system above or post it in the development forum at TT-forums.net:
http://www.tt-forums.net/viewtopic.php?f=26&t=64381


6 License
=========
Martian Town names is Copyright 2013 by Kris Knowlton (Oftcrash) under the CC by 3.0 license. There should be an attached license.txt file included with this release.

