letter = ''' Dear <|Name|>,
            you are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", "Gagan").replace("<|Date|>", "20 september 2010"))