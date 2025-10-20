import os
import requests
from PyroUbot import *

# Masukkan API Key Anda di sini
API_KEY = "Btz-bxwol"  # Ganti dengan API key yang benar

__MODULE__ = "ᴛᴇxᴛᴘʀᴏ5"
__HELP__ = """
<b>TextPro2 Commands</b>

<blockquote><b>Perintah : <code>blackpink</code>
Penjelasan : Membuat gambar dengan efek blackpink.</b></blockquote>
<blockquote><b>Perintah : <code>glasses</code>
Penjelasan : Membuat gambar dengan efek glasses.
<blockquote><b>Perintah : <code>coverpubg</code>
Penjelasan : Membuat gambar dengan efek coverpubg.
<blockquote><b>Perintah : <code>greenbrush</code>
Penjelasan : Membuat gambar dengan efek greenbrush.
<blockquote><b>Perintah : <code>blackpink2</code>
Penjelasan : Membuat gambar dengan efek blackpink2.
<blockquote><b>Perintah : <code>pig</code>
Penjelasan : Membuat gambar dengan efek pig.</b></blockquote>
"""

def fetch_image(api_url, text):
    """
    Fungsi untuk mengambil gambar dari API
    """
    params = {"text": text, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            print("Response bukan gambar:", response.text)  # Debugging
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")  # Debugging jika ada kesalahan
        return None

async def process_image_command(client, message, api_url, command_name):
    """
    Fungsi umum untuk menangani perintah pembuatan gambar
    """
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text(f"<b><i>Gunakan perintah /{command_name} <teks> untuk membuat gambar.</i></b>")
        return

    request_text = args[1]
    await message.reply_text("<b><i>Sedang memproses, mohon tunggu...</i></b>")

    image_content = fetch_image(api_url, request_text)
    if image_content:
        temp_file = f"{command_name}.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)
        await message.reply_photo(photo=temp_file)
        os.remove(temp_file)
    else:
        await message.reply_text("Gagal membuat gambar. Coba lagi nanti.")

# Handler untuk setiap perintah
@PY.UBOT("blackpink")
async def blackpink_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/blackpink"
    await process_image_command(client, message, api_url, "blackpink")

@PY.UBOT("glasses")
async def glasses_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/glasses"
    await process_image_command(client, message, api_url, "glasses")
    
@PY.UBOT("pig")
async def pig_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/pig"
    await process_image_command(client, message, api_url, "pig")
    
@PY.UBOT("blackpink2")
async def blackpink2_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/blackpink2"
    await process_image_command(client, message, api_url, "blackpink2")
    
@PY.UBOT("coverpubg")
async def coverpubg_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/coverpubg"
    await process_image_command(client, message, api_url, "coverpubg")
    
@PY.UBOT("greenbrush")
async def greenbrush_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/ephoto/greenbrush"
    await process_image_command(client, message, api_url, "greenbrush")