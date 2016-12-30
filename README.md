# butter-fingers
A python library to generate highly realistic typos (fuzz-testing)

## Roadmap

Implement the following features:

- change probability that a typo will be made given that one has been
- account for hands shifting on keys (and that the user doesn't look up)
- add support for multiple types of keyboards (i.e dvorak)
- sticky shift key (user presses shift too early/late or for too long)
- probability user will notice typo and correct it
- add features to change how the user types based on how far away their hands are and what keys each hand presses (touch typing or other)
- add support for user pressing two keys at once
- increase probability of typo if the user is typing something all on one line (like typewriter) or decrease it
- change probability if the user has to switch between many different words (for example typing was then zebra since their hand is covering "a" and is hard to see the "z")
