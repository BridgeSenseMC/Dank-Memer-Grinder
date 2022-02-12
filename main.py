import asyncio
import random
import re
import threading
import json
import discord

from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='-', guild_subscription_options=discord.GuildSubscriptionOptions.off(), self_bot=True)

config_file = open("Config.json", "r+", encoding="utf8")
config_dict = json.load(config_file)
if len(config_dict) != 3 or input("Configure bot? (Y/N): ").upper() == "Y":
    channel_id = int(input("Discord channel id (e.g., 846362236988817446): "))
    config_dict.update({"channel_id": channel_id})
    disc_token = input("Discord token (e.g., NzIyMDg3NjExODQ1NDQzNjA0.YbNqTA.GAc8feHuTB3gMh301gXLZ4jDcrg): ")
    config_dict.update({"discord_token": disc_token})
    config_file.seek(0)
    json.dump(config_dict, config_file, ensure_ascii=False, indent=4)
else:
    channel_id = config_dict["channel_id"]
    disc_token = config_dict["discord_token"]
config_file.close()

Games = {"Among Us": 0, "Animal Crossing": 1, "Apex Legends": 2, "Battlefield 2042": 3,
         "Counter-Strike Global Offensive": 4, "Crab Game": 5, "Dark Souls II": 6, "Destiny 2": 7, "Diablo II": 8,
         "Dota 2": 9, "FIFA 22": 10, "Fortnite": 11, "Forza Horizon 5": 12, "Genshin Impact": 13, "Get Stuffed": 14,
         "Grand Theft Auto V": 15, "Hearthstone": 16, "League of Legends": 17, "Mario": 18, "Minecraft": 19,
         "New World": 20, "Overwatch": 21, "Phasmophobia": 22, "Rocket League": 23, "Valorant": 24}

trivia_file = open("Trivia.json", "r", encoding="utf8")
trivia_dict = json.load(trivia_file)
trivia_file.close()


def update():
    global commands_dict
    global config_dict
    threading.Timer(10, update).start()
    config_file = open("Config.json", "r", encoding="utf8")
    config_dict = json.load(config_file)
    config_file.close()
    commands_file = open("Commands.json", "r", encoding="utf8")
    commands_dict = json.load(commands_file)
    commands_file.close()


update()


@bot.event
async def on_ready():
    global channel
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(channel_id)
    print(f"Sending messages in {channel}")


# pls triv
@tasks.loop(seconds=random.randint(20, 23))
async def pls_triv():
    if commands_dict["pls triv"] == "true":
        await channel.send("pls triv")


pls_triv.start()


@pls_triv.before_loop
async def before_pls_triv():
    await asyncio.sleep(4)


# pls dig
@tasks.loop(seconds=random.randint(42, 45))
async def pls_dig():
    if commands_dict["pls dig"] == "true":
        await channel.send("pls dig")


pls_dig.start()


@pls_dig.before_loop
async def before_pls_dig():
    await asyncio.sleep(6)


# pls fish
@tasks.loop(seconds=random.randint(42, 45))
async def pls_fish():
    if commands_dict["pls fish"] == "true":
        await channel.send("pls fish")


pls_fish.start()


@pls_fish.before_loop
async def before_pls_fish():
    await asyncio.sleep(8)


# pls hunt
@tasks.loop(seconds=random.randint(42, 45))
async def pls_hunt():
    if commands_dict["pls hunt"] == "true":
        await channel.send("pls hunt")


pls_hunt.start()


@pls_hunt.before_loop
async def before_pls_hunt():
    await asyncio.sleep(10)


# pls pm
@tasks.loop(seconds=random.randint(42, 45))
async def pls_pm():
    if commands_dict["pls pm"] == "true":
        await channel.send("pls pm")


pls_pm.start()


@pls_pm.before_loop
async def before_pls_pm():
    await asyncio.sleep(12)


# pls hl
@tasks.loop(seconds=random.randint(42, 45))
async def pls_hl():
    if commands_dict["pls hl"] == "true":
        await channel.send("pls hl")


pls_hl.start()


@pls_hl.before_loop
async def before_pls_hl():
    await asyncio.sleep(14)


# pls search
@tasks.loop(seconds=random.randint(42, 45))
async def pls_search():
    if commands_dict["pls search"] == "true":
        await channel.send("pls search")


pls_search.start()


@pls_search.before_loop
async def before_pls_search():
    await asyncio.sleep(16)


# pls beg
@tasks.loop(seconds=random.randint(57, 60))
async def pls_beg():
    if commands_dict["pls beg"] == "true":
        await channel.send("pls beg")


pls_beg.start()


@pls_beg.before_loop
async def before_pls_beg():
    await asyncio.sleep(18)


# pls crime
# await asyncio.sleep(20)

# pls dep all
@tasks.loop(minutes=random.randint(5, 10))
async def pls_dep_all():
    if commands_dict["pls dep all"] == "true":
        await channel.send("pls dep all")


pls_dep_all.start()


@pls_dep_all.before_loop
async def before_pls_dep_all():
    await asyncio.sleep(22)


# pls stream
@tasks.loop(minutes=random.randint(11, 14))
async def pls_stream():
    if commands_dict["pls stream"] == "true":
        await channel.send("pls stream")


pls_stream.start()


@pls_stream.before_loop
async def before_pls_stream():
    await asyncio.sleep(24)


# on message events
@bot.event
async def on_message(message):
    try:
        if message.author == bot.user or message.guild.id != 846362236658515998:
            return
        embeds = message.embeds  # return list of embeds
        for embed in embeds:
            # pls triv answer
            try:
                if embed.to_dict()["fields"][0]["name"] == "Difficulty":
                    category = embed.to_dict()["fields"][1]["value"][1:-1]
                    triv_question = embed.to_dict()["description"].split("\n")[0][2:-2]
                    answer = trivia_dict[category][triv_question]
                    chance = config_dict["Trivia_correct_chance"]
                    if random.random() <= chance:
                        if message.components[0].children[0].label == answer:
                            await message.components[0].children[0].click()
                        elif message.components[0].children[1].label == answer:
                            await message.components[0].children[1].click()
                        elif message.components[0].children[2].label == answer:
                            await message.components[0].children[2].click()
                        elif message.components[0].children[3].label == answer:
                            await message.components[0].children[3].click()
                    else:
                        if message.components[0].children[0].label != answer:
                            await message.components[0].children[0].click()
                        else:
                            await message.components[0].children[1].click()
            except UnboundLocalError:
                print(f"cant find answer {message.components}")
            except:
                pass

            # pls pm button
            try:
                if "meme posting session" in embed.to_dict()["author"]["name"]:
                    await message.components[0].children[random.randint(0, 4)].click()
            except:
                pass

            # Dtrend game
            try:
                if embed.to_dict()["title"] == "Trending stream":
                    global game
                    game = Games[(re.search("\*\*(.*?)\*\*", embed.to_dict()["description"]).group(1)).title()]
                    print(game)
            except:
                pass

            # Go live
            try:
                if embed.to_dict()["fields"][1]["name"] == "Last Live":
                    try:
                        await message.components[0].children[0].click()

                        # get trending game
                        await channel.send("Dtrend")
                        await asyncio.sleep(4)

                        # select game
                        await message.components[0].children[0].choose(
                            message.components[0].children[0].options[game])
                        await asyncio.sleep(1)
                        await message.components[1].children[0].click()
                        await asyncio.sleep(1)
                        await message.components[0].children[1].click()
                        await asyncio.sleep(1)
                        await message.components[1].children[1].click()
                    except:
                        await message.components[0].children[2].click()
            except:
                pass

            # Read chat
            try:
                if embed.to_dict()["fields"][1]["name"] == "Live Since":
                    try:
                        await message.components[0].children[1].click()  # Read Chat
                        await asyncio.sleep(1)
                        await message.components[1].children[1].click()  # End Interaction
                    except:
                        await message.components[1].children[1].click()  # End Interaction
            except:
                pass

        # pls hl button
        try:
            if "I just chose a secret number" in embed.to_dict()["description"]:
                num = int((re.search("\*\*(.*?)\*\*", embed.to_dict()["description"]).group(1)).title())
                if num >= 50:
                    column = 0
                else:
                    column = 2
                await message.components[0].children[column].click()  # Click button High or Low
        except:
            pass

        # pls search button
        try:
            if "search" in message.content or "searching" in message.content:
                await message.components[0].children[0].click()  # Click first button
        except:
            pass
        await bot.process_commands(message)
    except Exception as e:
        print(e)
        pass


@bot.command()
async def start(ctx, *, args):
    if args in commands_dict:
        print(f"Starting {args}")
        commands_dict[args] = "true"
        commands_file = open("Commands.json", "w")
        json.dump(commands_dict, commands_file, ensure_ascii=False, indent=4)
        commands_file.close()
    else:
        print(f"{args} does not exist")


@bot.command()
async def stop(ctx, *, args):
    if args in commands_dict:
        print(f"stopping {args}")
        commands_dict[args] = "false"
        commands_file = open("Commands.json", "w")
        json.dump(commands_dict, commands_file, ensure_ascii=False, indent=4)
        commands_file.close()
    else:
        print(f"{args} does not exist")


bot.run(disc_token)
