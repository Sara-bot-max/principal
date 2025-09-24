import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    # Lista de recetas con huevos
recetas_huevos = [
    {
        "nombre": "Huevos revueltos",
        "descripcion": "Clásicos huevos batidos con mantequilla, sal y pimienta. Perfectos para el desayuno."
    },
    {
        "nombre": "Tortilla de patatas",
        "descripcion": "Una receta española: papas fritas, cebolla y huevos batidos, cocinados como tortilla gruesa."
    },
    {
        "nombre": "Huevos a la mexicana",
        "descripcion": "Huevos revueltos con jitomate, cebolla y chile verde, típicos en México."
    },
    {
        "nombre": "Shakshuka",
        "descripcion": "Huevos escalfados en salsa de tomate con especias, típico del Medio Oriente."
    },
    {
        "nombre": "Omelette de queso",
        "descripcion": "Huevos batidos doblados con queso derretido en su interior."
    }
]

# Comando para pedir recetas con huevos
@bot.command(name="recetahuevos")
async def receta_huevos(ctx):
    receta = random.choice(recetas_huevos)
    embed = discord.Embed(
        title=f"🥚 {receta['nombre']}",
        description=receta['descripcion'],
        color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("") 
