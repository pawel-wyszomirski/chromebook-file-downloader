import streamlit as st
import requests
from urllib.parse import urlparse, unquote
import os

def get_filename_from_url(url):
    path = urlparse(url).path
    path = unquote(path)
    filename = os.path.basename(path)
    return filename or "pobrany_plik"

def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content, get_filename_from_url(url)
    except Exception as e:
        st.error(f"Wystąpił błąd: {str(e)}")
        return None, None

st.title('Pobieranie plików')

url = st.text_input('Wklej adres URL pliku')

if st.button('Pobierz plik'):
    if url:
        content, filename = download_file(url)
        if content is not None:
            st.download_button(
                label="Kliknij aby pobrać plik",
                data=content,
                file_name=filename,
                mime="application/octet-stream"
            )
    else:
        st.warning('Proszę podać adres URL')
