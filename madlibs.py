def get_part(partOfSpeech):
    return input("Give me a " + partOfSpeech + ": ")


adjective1 = get_part("adjective")
adjective2 = get_part("adjective")
bird = get_part("type of bird")
room = get_part("room in a house")
verb1 = get_part("verb (past tense)")
verb2 = get_part("verb")
relative = get_part("relative's name")
noun1 = get_part("noun")
liquid = get_part("liquid")
verbIng = get_part("verb ending in -ing")
bodyParts = get_part("part of body (plural)")
noun2 = get_part("plural noun")
verbIng2 = get_part("verb ending in -ing")
noun3 = get_part("noun")

print(f"""
It was a {adjective1}, cold November day. I woke up to the {adjective2}
smell of {bird} roasting in the {room} downstains. I 
{verb1} down the stairs to see if I could help {verb2}
the dinner.  My mom said, "See if {relative} needs a 
fresh {noun1}." So I carried a tray of glasses full of
{liquid} into the {verbIng} room. When I got there,
I couldn't believe my {bodyParts}! THere were
{noun2} {verbIng2} on the {noun3}
""")