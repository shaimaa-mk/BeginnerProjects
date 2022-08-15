
story = """" 
There's {gender} called {name} who loved to play in house grand everyday {time}, 
sometimes made loudly noise where neighbors {past} bothering and told {pronoun} parents bad words!
{pronoun} parents {past} sadly, they asked themselves: what we should do ? 
{name} was ashamed, and decided to play gently and be polite. THE END
"""

name = input("Your name :")
gender = input("You are a boy or girl?")
time = input("Your best time to play morning, afternoon or evening?")
past_tense = input("The past tense of feel :")
if gender == 'boy':
    pronoun = "his"
else:
    pronoun = 'her'
print("Congratulations Your Story have made !")
print(story.format(gender=gender, name=name, time=time, past=past_tense, pronoun=pronoun))
