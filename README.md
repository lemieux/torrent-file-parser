Torrent file decoder
====================

Usage :
`python app.py [torrent file]`

Description
-----------

The app has two parts : the bencode decoder and the lib. The bencode part is used to read and translate a torrent file to a dictionary. The library is taking the parsed dictionary and builds a Torrent object which contains the normalized data.


Things to improve/add
---------------------

- add comments
- had problems with the file checksum, not sure it is right
- more validation to detect non torrent files and edge cases
- tests