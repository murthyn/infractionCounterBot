# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *
import json

thread_id = "1599716096804784"
thread_type = ThreadType.GROUP

with open("infractions.json") as infractionsDB:
    infractions = json.loads(infractionsDB.read())

def writeInfractionsToFile():
    with open("infractions.json", "w") as js:
        js.write(json.dumps(infractions))

class InfractionClient(Client):
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        if "++" in message_object.text:
            for chatter in infractions:
                if chatter.lower() in message_object.text.lower():
                    infractions[chatter] += 1
            client.send(Message(text=str(infractions)), thread_id=thread_id, thread_type=thread_type)
            worstChatter = ""
            worstScore = 0
            for chatter in infractions:
                if infractions[chatter] > worstScore:
                    worstScore = infractions[chatter]
                    worstChatter = chatter
            client.send(Message(text="Fuck " + worstChatter), thread_id=thread_id, thread_type=thread_type)
            writeInfractionsToFile()
        elif "--" in message_object.text:
            for chatter in infractions:
                if chatter.lower() in message_object.text.lower():
                    infractions[chatter] -= 1
            client.send(Message(text=str(infractions)), thread_id=thread_id, thread_type=thread_type)
            writeInfractionsToFile()
        elif ("infraction" in message_object.text or "Infraction" in message_object.text) and str(author_id) != "100033965962382":
            client.send(Message(text="I like it when my friends remember me :)"), thread_id=thread_id, thread_type=thread_type)
        elif ("guideline" in message_object.text or "Guideline" in message_object.text) and str(author_id) != "100033965962382":
            client.send(Message(text="""*community guidelines*
                    - First and foremost, fair usage applies so no spamming. 
                    - Be discretionary while giving strikes. Remember, power is linearly correlated with responsibility - Spiderman 
                    - Remove strikes if the other person does something nice."""), thread_id=thread_id, thread_type=thread_type)
        elif "rip" in message_object.text or "RIP" in message_object.text:
            client.send(Message(text="F"), thread_id=thread_id, thread_type=thread_type)
        elif ("sad" in message_object.text or "SAD" in message_object.text) and str(author_id) != "100033965962382":
            client.send(Message(text="this is so sad alexa play despacito\nhttps://www.youtube.com/watch?v=kJQP7kiw5Fk"), thread_id=thread_id, thread_type=thread_type)
        elif "👀" in message_object.text and str(author_id) != "100033965962382":
            client.send(Message(text="👀"), thread_id=thread_id, thread_type=thread_type)
        elif "cute" in message_object.text.lower() and str(author_id) != "100033965962382":
            client.sendLocalImage(
                "images/cute.jpg",
                message=Message(text="awww you too!! <3"),
                thread_id=thread_id,
                thread_type=thread_type,
            )
          
client = InfractionClient("neuralnetmemes@gmail.com", "infractionBot")
client.listen()



# Will send a message to the thread
#client.send(Message(text="this is a test"), thread_id=thread_id, thread_type=thread_type)

# Will send the default `like` emoji
# client.send(
#     Message(emoji_size=EmojiSize.LARGE), thread_id=thread_id, thread_type=thread_type
# )

# # Will send the emoji `👍`
# client.send(
#     Message(text="👍", emoji_size=EmojiSize.LARGE),
#     thread_id=thread_id,
#     thread_type=thread_type,
# )

# # Will send the sticker with ID `767334476626295`
# client.send(
#     Message(sticker=Sticker("767334476626295")),
#     thread_id=thread_id,
#     thread_type=thread_type,
# )

# # Will send a message with a mention
# client.send(
#     Message(
#         text="This is a @mention", mentions=[Mention(thread_id, offset=10, length=8)]
#     ),
#     thread_id=thread_id,
#     thread_type=thread_type,
# )

# # Will send the image located at `<image path>`
# client.sendLocalImage(
#     "<image path>",
#     message=Message(text="This is a local image"),
#     thread_id=thread_id,
#     thread_type=thread_type,
# )

# # Will download the image at the url `<image url>`, and then send it
# client.sendRemoteImage(
#     "<image url>",
#     message=Message(text="This is a remote image"),
#     thread_id=thread_id,
#     thread_type=thread_type,
# )


# # Only do these actions if the thread is a group
# if thread_type == ThreadType.GROUP:
#     # Will remove the user with ID `<user id>` from the thread
#     client.removeUserFromGroup("<user id>", thread_id=thread_id)

#     # Will add the user with ID `<user id>` to the thread
#     client.addUsersToGroup("<user id>", thread_id=thread_id)

#     # Will add the users with IDs `<1st user id>`, `<2nd user id>` and `<3th user id>` to the thread
#     client.addUsersToGroup(
#         ["<1st user id>", "<2nd user id>", "<3rd user id>"], thread_id=thread_id
#     )


# # Will change the nickname of the user `<user_id>` to `<new nickname>`
# client.changeNickname(
#     "<new nickname>", "<user id>", thread_id=thread_id, thread_type=thread_type
# )

# # Will change the title of the thread to `<title>`
# client.changeThreadTitle("<title>", thread_id=thread_id, thread_type=thread_type)

# # Will set the typing status of the thread to `TYPING`
# client.setTypingStatus(
#     TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type
# )

# # Will change the thread color to `MESSENGER_BLUE`
# client.changeThreadColor(ThreadColor.MESSENGER_BLUE, thread_id=thread_id)

# # Will change the thread emoji to `👍`
# client.changeThreadEmoji("👍", thread_id=thread_id)

# # Will react to a message with a 😍 emoji
# client.reactToMessage("<message id>", MessageReaction.LOVE)
