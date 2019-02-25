import discord
import asyncio


client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-------------------")
    await client.change_presence(game=discord.Game(name= '매니저명령어',type=1))

@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요!")

    if message.content.startswith("!투표"):
        vote = message.content[4:].split("/")
        await client.send_message(message.channel, "투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, "```" + vote[i] + "```")
            await client.add_reaction(choose, '⭕')

    if "씨발" in messagege_content or "바보" in message.content:
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        member = discord.utils.get(client.get_all_members(), id="547995283095814144")
        for i in range(1, 31):
            if str(sheet["A" + str(i)].value) == str(message_author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                if int(sheet["B" + str(i)].value) == 3:
                    await client.ban(member, 1)
                break
            if str(sheet["A" + str(i)].value) == "-":
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 1
                break
        file.save["경고.xlsx"]
        await client.send_message(message.channel, "경고를 받았습니다. 조심해주시기 바랍니다.")


client.run("NTQ3OTk1MjgzMDk1ODE0MTQ0.D0-4XA.EGvGMotYZii5Sa0lbCsdQa-wZ4s")
