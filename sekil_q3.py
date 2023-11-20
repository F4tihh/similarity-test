import cv2
import numpy as np

def sekil_q3(image_prefix='kesilen_st_', output_prefix='y_st', alt_sinir=[150, 100, 100], ust_sinir=[255, 255, 255], new_size=(600, 600)):
    for i in range(1, 16):
        try:
            # Resmi yükleyin
            resim = cv2.imread(f'{image_prefix}{i}.jpg')

            # Yeni boyutları belirtin ve resmi yeni boyuta yeniden boyutlandırın
            resim = cv2.resize(resim, new_size)

            # Renk eşikleri tanımlayın (BGR formatında)
            alt_sinir = np.array(alt_sinir, dtype=np.uint8)  # Alçak sınır (beyaza yakın renkler)
            ust_sinir = np.array(ust_sinir, dtype=np.uint8)  # Üst sınır (beyaz)

            # Resmi renk aralığına göre filtreleyin
            maske = cv2.inRange(resim, alt_sinir, ust_sinir)

            # Beyaz renkteki pikselleri orijinal renkli resimle birleştirin
            sonuc_resim = cv2.bitwise_and(resim, resim, mask=maske)

            # Sonucu gösterin
            #cv2.imshow(f'Sadece Beyaza Yakın Renkler{i}', sonuc_resim)
            #cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Sonucu aynı yere kaydetmek için
            cv2.imwrite(f'{output_prefix}{i}.jpg', sonuc_resim)
        
        except Exception as e:
            print(f'Hata oluştu: {e}')
            continue  # Hata oluştuğunda işlemi devam ettir

# İşlevi çağırarak kodu çalıştırın
sekil_q3()