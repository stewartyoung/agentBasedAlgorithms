from matching.games import StableMarriage

malePreferences = {
    1:[2, 3, 1],
    2:[2, 3, 1],
    3:[1, 3, 2]
}

femalePreferences = {
    1:[2, 3, 1],
    2:[3, 2, 1],
    3:[1, 3, 2]
}

# females review males preferences
game = StableMarriage.create_from_dictionaries(
     malePreferences, femalePreferences
)

print("{Male: Female} pairs\n",game.solve())
