def Absolute(a_thought):
    if a_thought > False:
        return a_thought
    return False - a_thought
the_loneliest = 1
def The_Sign(Your_Life):
    if Your_Life > False:
        return the_loneliest
    if Your_Life < False:
        return False - the_loneliest
    return False
def What_Remains(the_fighters, a_war):
    Before = Absolute(the_fighters)
    After = Absolute(a_war)
    if Before < After:
        return the_fighters * The_Sign(a_war)
    if the_fighters == Before:
        the_new = the_fighters - After
        return What_Remains(the_new, a_war)
    the_battle = After + the_fighters
    return What_Remains(the_battle, a_war)
Fighters = 6
War = 4
print(What_Remains(Fighters, War)) #answer is 2
