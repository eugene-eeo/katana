Katana
======

**Katana** - Razor sharp parser written in Python. What makes
Katana different is that it uses a Trie and a look-ahead,
multi-stage parser. Note that at the moment the parser is not
academically proven, and may not work as expected. A basic
overview of the parser would be the following:

- The text is tokenised.
- "Simple" (no repetition) patterns are then stored in a trie.
  The reason a trie is used is because:

  - Tries are a good datastructure to represent trees and get
    possibilities.
  - It is the only reasonable datastructure- using tries one
    can perform look ahead queries in a more straightfoward
    way.
  - Simpler to implement than complicated FSMs- using a Trie
    and giving access to the token stream and stack is
    equivalent to using a non-deterministic state machine.

- Tokens are then grouped using the trie in a forward-looking,
  longest-matching manner. This is repeated as many times as
  needed.

Todo
----

- Refactor Trie and grouping machinery.
- More abstract quantifiers such as ``Repeat``, ``Sequence``,
  ``Any``.
- Think about multi-stage parsing.
