#!/usr/bin/env python
import json
import random

quotes: list[str] = [
    "“Perceive that which cannot be seen with the eye.” - Miyamoto Musashi",
    "“Do nothing which is of no use.” - Miyamoto Musashi",
    "“It is difficult to understand the universe if you only study one planet.” - Miyamoto Musashi",
    "“You must understand that there is more than one path to the top of the mountain.” - Miyamoto Musashi",
    "“Truth is not what you want it to be; it is what it is. And you must bend to its power or live a lie.” - Miyamoto Musashi",
    "“Study strategy over the years and achieve the spirit of the warrior. Today is victory over yourself of yesterday; tomorrow is your victory over lesser men.” - Miyamoto Musashi",
    "“Generally speaking, the Way of the warrior is resolute acceptance of death.” - Miyamoto Musashi", 
    "“Perception is strong and sight weak. In strategy it is important to see distant things as if they were close and to take a distanced view of close things.” - Miyamoto Musashi",
    "“The first half of life is devoted to forming a healthy ego, the second half is going inward and letting go of it.” - Carl Jung",
    "“The best among you is the one who doesn't harm others with his tongue and hands.” - Prophet Muhammad (peace be upon him)",
    "“Strive always to excel in virtue and truth.” - Prophet Muhammad (peace be upon him)",
    "“The strongest among you is the one who controls his anger.” - Prophet Muhammad (peace be upon him)",
    "“A father gives nothing better than good education.” - Prophet Muhammad (peace be upon him)",
]
data = {
    'text': quotes[random.randrange(len(quotes))],
}

print(json.dumps(data))