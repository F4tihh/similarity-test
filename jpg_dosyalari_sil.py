import os

def jpg_dosyalari_sil():
    """
    Şu anki çalışma dizinindeki .jpg uzantılı dosyaları siler.
    Z_bk ile başlayan dosyalar hariç.
    """
    klasor_yolu = os.getcwd()  # Şu anki çalışma dizinini al
    for dosya in os.listdir(klasor_yolu):
        if dosya.endswith(".jpg") and not dosya.startswith("z_bk"):
            dosya_yolu = os.path.join(klasor_yolu, dosya)
            os.remove(dosya_yolu)
            print(f"{dosya} silindi.")

jpg_dosyalari_sil()