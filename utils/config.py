note_to_index = {
    'C': 0, 'B#': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'Fb': 4, 'E#': 5, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7,
    'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11, 'Cb': 11
}

index_to_note = {0: 'C', 1: 'Db', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb', 7: 'G', 8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B'}

"""Adds an interval to the vector based on the root note."""
interval_semitones = {
    'b2': 1, '2': 2, '#2': 3, 'b3': 3, '3': 4,
    '4': 5, '#4': 6, 'b5': 6, '5': 7, '#5': 8, 'b6': 8,
    '6': 9, 'bb7': 9, 'b7': 10, '7': 11,
    'b9': 13 - 12, '9': 14 - 12, '#9': 15 - 12, '11': 17 - 12, '#11': 18 - 12, 'b13': 20 - 12, '13': 21 - 12,
    'b5/#5': 8, 'b9/#9': 1
}


# Add intervals based on the tension
tension_intervals = {
    '' : ['3', '5'],
    '9b5': ['3', 'b5', 'b7', '9'],
    '7#11': ['3', '5', 'b7', '#11'],
    '-b6': ['b3', '5', 'b6'],
    '-7': ['b3', '5', 'b7'],
    '7b9#9': ['3', '5', 'b7', 'b9', '#9'],
    '13sus': ['4', '5', 'b7', '9', '11', '13'],
    '7b9b5': ['3', 'b5', 'b7', 'b9'],
    '13#9': ['3', '5', 'b7', '#9', '13'],
    '69': ['3', '5', '6', '9'],
    '^9#11': ['3', '5', '7', '9', '#11'],
    '7b9sus': ['4', '5', 'b7', 'b9'],
    '7b9': ['3', '5', 'b7', 'b9'],
    '7#9b5': ['3', 'b5', 'b7', '#9'],
    '13': ['3', '5', 'b7', '9', '11', '13'],
    '7#9#5': ['3', '#5', 'b7', '#9'],
    '-7b5': ['b3', 'b5', 'b7'],
    '^7#5': ['3', '#5', '7'],
    'h': ['b3', 'b5', 'b7'],
    '7#9#11': ['3', '5', 'b7', '#9', '#11'],
    '7b9#11': ['3', '5', 'b7', 'b9', '#11'],
    '^7': ['3', '5', '7'],
    '7sus': ['4', '5', 'b7'],
    'o7': ['b3', 'b5', 'bb7'],
    '-9': ['b3', '5', 'b7', '9'],
    '7b5': ['3', 'b5', 'b7'],
    '13b9': ['3', '5', 'b7', 'b9', '13'],
    'add9': ['3', '5', '9'],
    '13#11': ['3', '5', 'b7', '9', '#11', '13'],
    '7#9': ['3', '5', 'b7', '#9'],
    '^9': ['3', '5', '7', '9'],
    'sus': ['4', '5'],
    '-6': ['b3', '5', '6'],
    '7b13sus': ['4', '5', 'b7', 'b13'],
    '-': ['b3', '5'],
    '7b9#5': ['3', '#5', 'b7', 'b9'],
    '7b9b13': ['3', '5', 'b7', 'b9', 'b13'],
    'h7': ['b3', 'b5', 'b7'],
    'o^7': ['b3', 'b5', '7'],
    '7#5': ['3', '#5', 'b7'],
    '7alt': ['3', 'b5/#5', 'b7', 'b9/#9'],
    '+': ['3', '#5'],
    '9#11': ['3', '5', 'b7', '9', '#11'],
    '^13': ['3', '5', '7', '9', '11', '13'],
    '9sus': ['4', '5', 'b7', '9'],
    '9': ['3', '5', 'b7', '9'],
    '-11': ['b3', '5', 'b7', '9', '11'],
    '7susadd3': ['3', '4', '5', 'b7'],
    '^': ['3', '5', '7'],
    '2': ['2', '5'],
    '9#5': ['3', '#5', 'b7', '9'],
    '-#5': ['b3', '#5'],
    '6': ['3', '5', '6'],
    '-69': ['b3', '5', '6', '9'],
    '-^7': ['b3', '5', '7'],
    '7': ['3', '5', 'b7'],
    '^7#11': ['3', '5', '7', '#11'],
    '7b13': ['3', '5', 'b7', 'b13'],
    'o': ['b3', 'b5'],
    'h9': ['b3', 'b5', 'b7', '9'],
}

tension_intervals_reduced = {
    '' : ['3', '5'],
    #'9b5': ['3', 'b5', 'b7', '9'],
    '7#11': ['3', '5', 'b7', '#11'],
    #'-b6': ['b3', '5', 'b6'],
    '-7': ['b3', '5', 'b7'],
    #'7b9#9': ['3', '5', 'b7', 'b9', '#9'],
    #'13sus': ['4', '5', 'b7', '9', '11', '13'],
    #'7b9b5': ['3', 'b5', 'b7', 'b9'],
    '13#9': ['3', '5', 'b7', '#9', '13'],
    '69': ['3', '5', '6', '9'],
    '^9#11': ['3', '5', '7', '9', '#11'],
    '7b9sus': ['4', '5', 'b7', 'b9'],
    '7b9': ['3', '5', 'b7', 'b9'],
    '7#9b5': ['3', 'b5', 'b7', '#9'],
    '13': ['3', '5', 'b7', '9', '11', '13'],
    '7#9#5': ['3', '#5', 'b7', '#9'],
    #'-7b5': ['b3', 'b5', 'b7'],
    '^7#5': ['3', '#5', '7'],
    #'h': ['b3', 'b5', 'b7'],
    '7#9#11': ['3', '5', 'b7', '#9', '#11'],
    '7b9#11': ['3', '5', 'b7', 'b9', '#11'],
    '^7': ['3', '5', '7'],
    '7sus': ['4', '5', 'b7'],
    'o7': ['b3', 'b5', 'bb7'],
    '-9': ['b3', '5', 'b7', '9'],
    '7b5': ['3', 'b5', 'b7'],
    '13b9': ['3', '5', 'b7', 'b9', '13'],
    'add9': ['3', '5', '9'],
    '13#11': ['3', '5', 'b7', '9', '#11', '13'],
    '7#9': ['3', '5', 'b7', '#9'],
    '^9': ['3', '5', '7', '9'],
    'sus': ['4', '5'],
    #'-6': ['b3', '5', '6'],
    #'7b13sus': ['4', '5', 'b7', 'b13'],
    '-': ['b3', '5'],
    '7b9#5': ['3', '#5', 'b7', 'b9'],
    '7b9b13': ['3', '5', 'b7', 'b9', 'b13'],
    'h7': ['b3', 'b5', 'b7'],
    'o^7': ['b3', 'b5', '7'],
    '7#5': ['3', '#5', 'b7'],
    #'7alt': ['3', 'b5/#5', 'b7', 'b9/#9'],
    '+': ['3', '#5'],
    '9#11': ['3', '5', 'b7', '9', '#11'],
    #'^13': ['3', '5', '7', '9', '11', '13'],
    #'9sus': ['4', '5', 'b7', '9'],
    '9': ['3', '5', 'b7', '9'],
    '-11': ['b3', '5', 'b7', '9', '11'],
    '7susadd3': ['3', '4', '5', 'b7'],
    #'^': ['3', '5', '7'],
    #'2': ['2', '5'],
    '9#5': ['3', '#5', 'b7', '9'],
    #'-#5': ['b3', '#5'],
    #'6': ['3', '5', '6'],
    '-69': ['b3', '5', '6', '9'],
    '-^7': ['b3', '5', '7'],
    '7': ['3', '5', 'b7'],
    '^7#11': ['3', '5', '7', '#11'],
    '7b13': ['3', '5', 'b7', 'b13'],
    'o': ['b3', 'b5'],
    #'h9': ['b3', 'b5', 'b7', '9'],

    '-/3': ['b3', '5', '3'],       # '-/' chord with bass note a major 3rd above the root
    '/4': ['3', '5', '4'],         # '/' chord with bass note a perfect 4th above the root
    '7b9/4': ['3', '5', 'b7', 'b9', '4'],  # '7b9' with bass note a perfect 4th above the root
    'o7/b7': ['b3', 'b5', 'bb7', 'b7'],    # 'o7' with bass note a minor 7th above the root
    'o7/b2': ['b3', 'b5', 'bb7', 'b2'],    # 'o7' with bass note a minor 2nd above the root
    'h7/b2': ['b3', 'b5', 'b7', 'b2'],     # 'h7' with bass note a minor 2nd above the root
    '^7/b6': ['3', '5', '7', 'b6'],        # '^7' with bass note a minor 6th above the root
    'o/3': ['b3', 'b5', '3'],              # 'o' with bass note a major 3rd above the root
    '^7#5/5': ['3', '#5', '7', '5'],       # '^7#5' with bass note a perfect 5th above the root
    '-7/b2': ['b3', '5', 'b7', 'b2'],      # '-7' with bass note a minor 2nd above the root
    'o7/5': ['b3', 'b5', 'bb7', '5'],      # 'o7' with bass note a perfect 5th above the root
    '-6/b7': ['b3', '5', '6', 'b7'],       # '-6' with bass note a minor 7th above the root
    '/b3': ['3', '5', 'b3'],               # '/' with bass note a minor 3rd above the root
    'o7/3': ['b3', 'b5', 'bb7', '3'],      # 'o7' with bass note a major 3rd above the root
    '13b9/4': ['3', '5', 'b7', 'b9', '13', '4'],  # '13b9' with bass note a perfect 4th above the root
    '-/2': ['b3', '5', '2'],               # '-/' with bass note a major 2nd above the root
    '/b5': ['3', '5', 'b5'],               # '/' with bass note a diminished 5th above the root
    '-/4': ['b3', '5', '4'],               # '-/' with bass note a perfect 4th above the root
    '-^7/2': ['b3', '5', '7', '2'],        # '-^7' with bass note a major 2nd above the root
    '7#9/2': ['3', '5', 'b7', '#9', '2'],  # '7#9' with bass note a major 2nd above the root
}

list_fr = [
    "Blues For Alice", "Stella By Starlight", "Satin Doll", "Daahoud",
    "There Will Never Be Another You", "Don't Get Around Much Anymore",
    "On Green Dolphin Street", "Indiana (Back Home Again In)", "Donna Lee",
    "Honeysuckle Rose", "Scrapple From The Apple", "Autumn Leaves",
    "Girl From Ipanema, The", "Wave", "Misty", "My Funny Valentine",
    "Someday My Prince Will Come", "I Got Rhythm", "Anthropology", "All Of Me",
    "Bye Bye Blackbird", "Epistrophy", "Impressions", "So What", "Nardis",
    "My Romance", "Sweet Georgia Brown", "Dig",
    "What Is This Thing Called Love", "Hot House", "Night And Day",
    "Maiden Voyage", "A Night In Tunisia", "All Blues",
    "Have You Met Miss Jones?", "Woody'n You"
]

list_so = [
    "Secret Love", "Confirmation", "Like Someone In Love", "I Hear A Rhapsody",
    "I Love You", "Our Love is Here to Stay", "Prelude To A Kiss", "Star Dust",
    "Here's That Rainy Day", "Days Of Wine And Roses",
    "Embraceable You", "Body And Soul", "Cherokee",
    "What's New", "Afternoon In Paris", "Alone Together", "Yesterdays",
    "Fee-Fi-Fo-Fum", "All The Things You Are", "Milestones (Old)", "Bluesette",
    "Corcovado", "Don't Blame Me", "In Your Own Sweet Way", "Four",
    "Lady Bird", "Joy Spring", "Minority"
]
# Freedom Jazz Dance, A Day In The Life Of A Fool

list_jr = [
    "All Of Me", "Beautiful Love", "Everything Happens To Me", "Song Is You, The",
    "Dearly Beloved", "How High The Moon", "Ornithology", "Meditation",
    "I Can't Get Started", "I Got It Bad",
    "End Of A Love Affair, The", "I Remember You", "One Finger Snap",
    "In a Sentimental Mood", "Invitation", "Seven Steps To Heaven",
    "Dolphin Dance", "My One And Only Love", "I'll Take Romance",
    "Up Jumped Spring", "Out Of Nowhere", "Round Midnight",
    "Way You Look Tonight, The", "Sophisticated Lady", "Giant Steps",
    "You Stepped Out Of A Dream", "Tenderly", "When I Fall In Love",
    "Just One Of Those Things", "Over The Rainbow (Somewhere)", "Speak No Evil"
]

list_mm1 = [
    "It Could Happen To You", "Con Alma", "Nica's Dream", "Spring Is Here",
    "It Might As Well Be Spring", "Spring Can Really Hang You Up The Most",
    "Pensativa", "Upper Manhattan Medical Group", "You Don't Know What Love Is",
    "Round Midnight", "Falling Grace", "These Foolish Things", "Once I Loved",
    "Speak Low", "Pent Up House", "Polkadots And Moonbeams", "My Shining Hour",
    "I'm Old Fashioned", "Soul Eyes", "I Thought About You",
    "Everything Happens To Me", "Moment's Notice", "El Gaucho", "Airegin",
    "All God's Chillun Got Rhythm", "Little Willie Leaps", "Angel Eyes",
    "Lament", "But Not For Me", "But Beautiful", "Caravan"
]

# Consolidate all songs into a validation set
validation_set = set(list_fr + list_so + list_jr + list_mm1)
