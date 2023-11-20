import cv2
import numpy as np

def sekil_siyah_q3(image_prefix='zsb_', output_prefix='zz_bk'):
    for i in range(1, 16):
        try:
            # Görüntüyü yükle
            image = cv2.imread(f'{image_prefix}{i}.jpg')  # Resminizin adını ve yolunu verin

            # Görüntüyü gri tona dönüştür
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Beyaz kartın etrafını beyaz yapmak için bir maske oluşturun
            _, thresholded = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Beyaz kartın etrafındaki en büyük konturu bulun
            largest_contour = max(contours, key=cv2.contourArea)

            # Beyaz kartın etrafını beyaz ile doldurun
            mask = np.zeros_like(gray)
            cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

            # Beyaz kartın etrafını beyaz yapmak için maskeyi kullanın
            image[mask == 0] = [255, 255, 255]  # Beyaz renk (BGR formatında)

            # Sonucu kaydedin veya gösterin
            #cv2.imshow(f'Kart{i}', image)
            cv2.imwrite(f'{output_prefix}{i}.jpg', image)
            #cv2.waitKey(0)
        
        except Exception as e:
            print(f'Hata oluştu: {e}')
            continue  # Hata oluştuğunda işlemi devam ettir

    cv2.destroyAllWindows()

# İşlevi çağırarak kodu çalıştırın
sekil_siyah_q3()