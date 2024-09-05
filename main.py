import os
from nextcord.ext import commands
from dotenv import load_dotenv
import nextcord
from nextcord import Interaction

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém o token do bot a partir do .env
TOKEN = os.getenv('DISCORD_TOKEN')

# Verifica se o token foi obtido corretamente
if not TOKEN:
    raise ValueError("O token do bot não foi encontrado. Certifique-se de que a variável DISCORD_TOKEN está definida no arquivo .env.")

# Configura os intents para permitir acesso ao conteúdo das mensagens
intents = nextcord.Intents.default()
intents.message_content = True  # Habilita o intent de conteúdo de mensagem

# Cria a instância do bot com os intents configurados
bot = commands.Bot(command_prefix='/', intents=intents)

# Evento para quando o bot estiver pronto
@bot.event
async def on_ready():
    try:
        print(f'{bot.user.name} está online e pronto para uso!')
    except Exception as e:
        print(f"Erro ao iniciar o bot: {e}")

# Comando para enviar botões de suporte usando barra
@bot.slash_command(name='link', description="🔗Envia links de nosso servidor🔔:")
async def send_links(interaction: Interaction):
    try:
        # Criando os botões
        button_youtube = nextcord.ui.Button(label="YouTube", url="https://www.youtube.com/channel/UCLCKK_dJVqdzQWmMyhNCARQ", style=nextcord.ButtonStyle.blurple)
        button_instagram = nextcord.ui.Button(label="Instagram", url="https://www.instagram.com/gamedosurdo/", style=nextcord.ButtonStyle.blurple)
        button_discord = nextcord.ui.Button(label="Discord", url="https://discord.com/invite/n3Wu5AQqEb", style=nextcord.ButtonStyle.blurple)
        button_bluesky = nextcord.ui.Button(label="BlueSky", url="https://bsky.app/profile/gamesdossurdos.bsky.social", style=nextcord.ButtonStyle.blurple)

        # Criando a view e adicionando os botões
        myview = nextcord.ui.View(timeout=180)
        myview.add_item(button_youtube)
        myview.add_item(button_instagram)
        myview.add_item(button_discord)
        myview.add_item(button_bluesky)

        # Criando o embed
        embed = nextcord.Embed(
            title="Links de nosso servidor",
            description="Escolha um dos links abaixo.\n🚀 Lançamento do nosso o novo!\n\n 🎮 Hoje marcamos o início da nossa jornada de surdos/DA com o Games dos Surdos! 🧏‍♂️🧏‍♀️✨ :",
            color=0x00ff00  # Cor verde
        )
        
        # Adiciona uma imagem de fundo ao embed (thumbnail)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1112468471905796137/1280593464425451521/Logotipo_para_canal_do_YouTube_Games_Grunge_em_Preto_Cinza_Aqua_1.png?ex=66d9f69a&is=66d8a51a&hm=1509153aa01994200fff0809432e7c0bff72a15dec2f172f0a1d5fb6e1c717c2&=&format=webp&quality=lossless&width=657&height=657")
        embed.set_image(url="https://media.discordapp.net/attachments/1112468471905796137/1280238211393781791/standard_2gif.gif?ex=66d9fd3f&is=66d8abbf&hm=802c32feb3de68fe4f841c3c7d88c9c7f59b323ea62c88d7c576a9a34b5c8dd5&=")

        # Enviando a mensagem com o embed e botões
        await interaction.send(embed=embed, view=myview)
    except Exception as e:
        await interaction.send(f"Erro: {e}")

# Comando para exibir informações do bot usando barra
@bot.slash_command(name="info", description="Consulte informações sobre o bot.")
async def info(interaction: Interaction):
    try:
        # Cria um embed com as informações do bot
        embed = nextcord.Embed(
            title="Informações do Bot",
            description="**Fui criada em 29 de agosto de 2024**\nEu fui programado em Python usando a biblioteca Nextcord.",
            color=0x00ff00  # Cor verde
        )
        
        # Adiciona o avatar do bot como autor do embed
        embed.set_author(
            name=bot.user.name,
            icon_url=bot.user.display_avatar.url
        )
        
        # Adiciona uma thumbnail
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/1112468471905796137/1280593464425451521/Logotipo_para_canal_do_YouTube_Games_Grunge_em_Preto_Cinza_Aqua_1.png?ex=66d9f69a&is=66d8a51a&hm=1509153aa01994200fff0809432e7c0bff72a15dec2f172f0a1d5fb6e1c717c2&=&format=webp&quality=lossless&width=657&height=657"
        )
        embed.set_image(url="https://media.discordapp.net/attachments/1112468471905796137/1280238211393781791/standard_2gif.gif?ex=66d9fd3f&is=66d8abbf&hm=802c32feb3de68fe4f841c3c7d88c9c7f59b323ea62c88d7c576a9a34b5c8dd5&=")    
        
        # Adiciona campos adicionais
        embed.add_field(
            name="Nome do Bot",
            value=bot.user.name,
            inline=False
        )
        embed.add_field(
            name="ID do Bot",
            value=bot.user.id,
            inline=False
        )
        embed.add_field(
            name="Servidor",
            value=interaction.guild.name if interaction.guild else "DM",
            inline=False
        )
        
        # Envia o embed com as informações
        await interaction.send(embed=embed)
    except Exception as e:
        await interaction.send(f"Erro: {e}")

# Evento para quando o bot estiver pronto, definindo o status corretamente
@bot.event
async def on_ready():
    # Define o status como "Playing [alguma coisa]"
    await bot.change_presence(
        activity=nextcord.Game(name="Black Myth: Wukong!"),
        status=nextcord.Status.online
    )
    print(f"Bot {bot.user.name} está online e pronto!")        

# Executa o bot
if __name__ == '__main__':
    bot.run(TOKEN)
