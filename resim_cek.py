import cv2

def resim_cek(kayit_yolu="w3.jpg"):
    try:
        # Kamera bağlantısını başlatın (varsayılan olarak 0, birincil kamera)
        kamera = cv2.VideoCapture(1)

        # Kameradan bir kare çekin
        ret, kare = kamera.read()

        if not ret:
            print("Kamera bağlantısı başarısız.")
            return

        # Çekilen kareyi belirlediğiniz kayıt yolunda kaydedin
        cv2.imwrite(kayit_yolu, kare)

        # Kamera bağlantısını kapatın
        kamera.release()

        print(f"{kayit_yolu} adında bir resim kaydedildi.")
    
    except Exception as e:
        print(f'Hata oluştu: {e}')

# Fonksiyonu çağırarak kodu çalıştırın
resim_cek()