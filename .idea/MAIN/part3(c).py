# Character-Based Diffing
import difflib

def char_diff(original, modified):
    differ = difflib.Differ()
    diff = differ.compare(list(original), list(modified))
    delta = ''.join(diff)
    return delta

# Example usage
document1 = '''
Dear Annabel,

I hope you're doing fine. Are you excited about the summer break? Thank you for your last letter. It's always lovely to hear about what's going on back home.

I'm writing to you to invite you to come to visit me during the holidays. If the weather is terrible, we could go to the art and history museums. We could even spend the day at the park, or walk around the state fair. We could go to that cafe you like or take a day trip on the boat.

It would be great to spend a few weeks with you here in the city. We'd have a lot of fun! I know how much you love the city.

Let me know your thoughts. If you decide to come, we can start making plans for what we'll do while you're here.

I hope to hear from you soon, and I hope to see you soon.

With best wishes,

Philip
'''
document2 = '''
Dear Annabel,

I hope you're doing great. Are you excited about the winter break? Thank you for your last letter. It's always lovely to hear about what's going on back home.

I'm writing to you to invite you to come to visit me during the holidays. If the weather is terrible, we could go to the art and history museums. We could even spend the day at the park, or walk around the state fair. We could go to that cafe you like or take a night trip on the boat.

It would be great to spend a few weeks with you here in the city. We'd have a lot of fun time! I know how much you love the city.

Let me know your thoughts. If you decide to come, we can start making plans for what we'll do while you're here.

I hope to hear from you soon, and I hope to see you soon.

With best wishes,

Philip
'''

delta = char_diff(document1, document2)
print(delta)