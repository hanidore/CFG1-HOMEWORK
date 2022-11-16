
#Create required phrase.
#----------------------
#You are given a string of available characters and a string representing a word or a phrase that you need to generate.
#Write a function that checks if you cab generate required word/phrase using the characters provided.
#If you can, then please return True, otherwise return False.
#NOTES:
# You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
  #  than frequency in the document string.
#FOR EXAMPLE:
   # characters = "cbacba"
    #phrase = "aabbccc"
   # In this case you CANNOT create required phrase, because you are 1 character short!
#IMPORTANT:
   # The phrase you need to create can contain any characters including special characters, capital letter, numbers
   # and spaces.
   # You can always generate an empty string.

a="hani1"
b="hani_1"
dict={}
def generate_phrase(char,ph):

    for i in char:
        count=char.count(str(i))
        dict[i]=str(count)
        print(dict)

        dict1={}
        for a in ph:
            count1=ph.count(str(a))
            dict1[a]=str(count1)
            print(dict1)

        if len(char)< len(ph):
            print("phrase can not be generated")
            return False
        else:
            for i in dict:
                for a in dict1:
                    if i==a :
                        if dict[i]>=dict1[a]
                            return True
x=generate_phrase("hani1","hani_1")
print(x)

