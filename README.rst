Katana
======

**Katana** - Razor sharp parser written in Python.
What makes Katana different is that it uses a Trie
and a look-ahead, multi-stage parser. Note that at
the moment the parser is not academically proven,
and may not work as expected. A basic overview of
the parser would be the following:

 - The text is tokenised.
 - "Simple" (no repetition) patterns are then stored
   in a trie. The reason a trie is used is because:
     - Tries are a good datastructure to represent
       trees and get possibilities.
     - It is the only reasonable datastructure- the
       other would be a generated table similar to
       LALR parsers.
 - The tokens are then grouped according to the
   given patterns.
 - Second stage grouping where more complex patetrns
   can be resolved.
