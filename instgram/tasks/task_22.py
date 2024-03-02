pragraph="I have a pet dog named Bruno. He is brown and furry. He is named after my mothers favourite singer, Bruno Mars. Bruno came into my life when I was 4 years old. I clearly remember the day when I saw him for the first time. My older brother and I went to the Adoption Centre for Rescued Dogs. Initially, Bruno was very scared of everything around him. With proper care, love and attention Bruno started to be friendly with us. He slowly became energetic and along with it naughty as well. He is very protective of all of us and one day even saved my mothers bag from being stolen. His loyalty and enthusiasm are what I love the most. I will spend many years in his company full of joy and happiness." #input()

word_for_remove="I" #input()
word_for_replace="and" #input()

pragraph_1=pragraph.replace(word_for_remove,word_for_replace)
print(pragraph_1)

couting_value=pragraph.count(word_for_remove)
print("replacing value is :",couting_value)