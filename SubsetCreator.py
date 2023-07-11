import pandas as pd

# Read the JSON data into a DataFrame
df = pd.read_json('data/cleanedAggregateData.json')

# Create the subset based on your criteria
subset = df[df['title'].str.contains('digital game | digital games | game | games | RPG | DGBL | DGBLL | game-based | game based | massive multiplayer online | massive multiplayer online role-playing game | massive multiplayer | computer game | computer games | simulation game | simulation games | game based learning | digital game-based | digital game based | video game | video games | xbox | playstation | world of warcraft | final fantasy | game play | educational game | educational games | online game | online games | game-generated | novel game | novel games | interactive novel | interactive novels | visual game | visual games | mobile game | mobile games ', case=False) |
            df['subject'].str.contains('digital game | digital games | game | games | RPG | DGBL | DGBLL | game-based | game based | massive multiplayer online | massive multiplayer online role-playing game | massive multiplayer | computer game | computer games | simulation game | simulation games | game based learning | digital game-based | digital game based | video game | video games | xbox | playstation | world of warcraft | final fantasy | game play | educational game | educational games | online game | online games | game-generated | novel game | novel games | interactive novel | interactive novels | visual game | visual games | mobile game | mobile games ', case=False) |
            df['description'].str.contains('digital game | digital games | game | games | RPG | DGBL | DGBLL | game-based | game based | massive multiplayer online | massive multiplayer online role-playing game | massive multiplayer | computer game | computer games | simulation game | simulation games | game based learning | digital game-based | digital game based | video game | video games | xbox | playstation | world of warcraft | final fantasy | game play | educational game | educational games | online game | online games | game-generated | novel game | novel games | interactive novel | interactive novels | visual game | visual games | mobile game | mobile games ', case=False) 
            #uncomment to also search geotag
            #df['identifiersgeo'].str.contains('Japan|Japanese|JSL|JFL', case=False)
            ]

# Export the subset to a new JSON file
subset.to_json('DGBLLsubset.json', orient='records')
