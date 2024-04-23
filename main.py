import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def baixar_e_converter_mp3():
    url = url_entry.get()
    try:
        # Baixar o vídeo do YouTube
        yt = YouTube(url)
        video_title = yt.title

        # Baixar o áudio do YouTube diretamente como um arquivo MP3
        audio_stream = yt.streams.filter(only_audio=True).first()
        download_path = os.path.join(os.getcwd(), 'downloads')
        audio_stream.download(output_path=download_path)
        
        # Renomear o arquivo para ter o mesmo nome do vídeo, com a extensão .mp3
        original_file_path = os.path.join(download_path, audio_stream.default_filename)
        mp3_file_path = os.path.join(download_path, f"{video_title}.mp3")
        os.rename(original_file_path, mp3_file_path)
        
        messagebox.showinfo("Concluído", f"Download e conversão concluídos. O arquivo de áudio está disponível como '{video_title}.mp3'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Configuração da janela principal
root = tk.Tk()
root.title("Download e Conversão de Vídeo do YouTube para MP3")

# Rótulo e entrada para o URL do vídeo do YouTube
url_label = tk.Label(root, text="URL do vídeo do YouTube:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Botão para iniciar o processo de download e conversão
download_button = tk.Button(root, text="Baixar e Converter", command=baixar_e_converter_mp3)
download_button.pack(pady=10)

# Executar a interface
root.mainloop()
