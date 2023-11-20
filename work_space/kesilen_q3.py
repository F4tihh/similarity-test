import cv2
import numpy as np

def kesilen_q3(image_prefix='Bk_', output_prefix='kesilen_st_', min_threshold=30, max_threshold=100):
    for i in range(1, 16):
        try:
            # Resmi yükleyin
            resim = cv2.imread(f'{image_prefix}{i}.jpg')

            # Gri tonlamalı bir kopya oluşturun
            gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

            # Canny kenar tespiti ile kenarları bulun
            kenarlar = cv2.Canny(gri, threshold1=min_threshold, threshold2=max_threshold)

            # Kenarları daha belirgin hale getirmek için kenarları genişletin (isteğe bağlı)
            kenarlar = cv2.dilate(kenarlar, None, iterations=2)

            # Konturları bulun
            konturlar, _ = cv2.findContours(kenarlar.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Beyaz kart üzerindeki en büyük konturu bulun
            en_buyuk_kontur = max(konturlar, key=cv2.contourArea)

            # Yeşil etrafı dışındaki alanları siyah yapın
            maske = np.zeros(resim.shape[:2], dtype=np.uint8)   # Başlangıçta maskeyi beyaz yapın
            cv2.drawContours(maske, [en_buyuk_kontur], -1, 255, thickness=cv2.FILLED)  # Konturu siyah çizin
            resim[maske == 0] = 0 

            # Sonucu kaydedin
            cv2.imwrite(f'{output_prefix}{i}.jpg', resim)

            # Sonucu gösterin
            #cv2.imshow(f'Yeşil Etrafı Kes {i}', resim)
            #cv2.waitKey(0)
        
        except Exception as e:
            print(f'Hata oluştu: {e}')
            continue  # Hata oluştuğunda işlemi devam ettir

    # Tüm pencereleri kapat
    cv2.destroyAllWindows()

# İşlevi çağırarak kodu çalıştırın
kesilen_q3()