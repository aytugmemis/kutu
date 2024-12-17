import discord
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$1.adım'):
        await message.channel.send("Atiklarinizi Ayriştirin")

    elif message.content.startswith("$2.adım"):
        await message.channel.send("Cam Kullanimina Ağirlik Verin")

    elif message.content.startswith("$3.adım"):
        await message.channel.send("Gıdaları Kompost Yapı") 

    elif message.content.startswith("$4.adım"):
        await message.channel.send("Tek Kullanımlık Ürünlerden Kaçının") 
    
    elif message.content.startswith("$5.adım"):
        await message.channel.send("atık kutulardan geri dönüşüm kutusu yapabilirsin")

client.run("BURASI GİZLİ")
