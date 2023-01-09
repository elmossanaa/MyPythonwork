print('''type the [emotion] you are feeling from the following category: :
      happy, sad, excited, angry (otherwise, not emoji will be printed)''') 
message = input(">")
m = message.split(' ')
emotion = {
    "happy": "😊",
    "sad": "🙁",
    "excited": "😆",
    "angry": "👿"
    }
output =''
for e in m:
    output = "You are " + emotion.get(e,e)

print(output)
    



