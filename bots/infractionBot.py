# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

infractionsList = open("infractionsList.txt")
infractionsDict = {}

thread_id = "1599716096804784"
thread_type = ThreadType.GROUP

# Read infractionList file
for line in infractionsList:
	line = line.split(":")
	infractionsDict[line[0]] = int(line[1].strip())

infractionsList.close()


class InfractionClient(Client):
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        # Do something with message_object here
        if "++" in message_object.text:
        	for chatter in infractionsDict:
        		if chatter.lower() in message_object.text.lower():
        			infractionsDict[chatter] += 1

        	client.send(Message(text=str(infractionsDict)), thread_id=thread_id, thread_type=thread_type)

        	worstChatter = ""
        	worstScore = 0
        	for chatter in infractionsDict:
        		if infractionsDict[chatter] > worstScore:
        			worstScore = infractionsDict[chatter]
        			worstChatter = chatter

        	client.send(Message(text="Fuck you " + worstChatter), thread_id=thread_id, thread_type=thread_type)
        	writeInfractionsDict(infractionsDict)

client = InfractionClient("neuralnetmemes@gmail.com", "infractionBot")
client.listen()

def writeInfractionsDict(dictionary):
	infractionsList = open("infractionsList.txt", "w")
	for chatter in dictionary:
		infractionsList.write(chatter + ": " + str(dictionary[chatter]))
	infractionsList.close()


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
