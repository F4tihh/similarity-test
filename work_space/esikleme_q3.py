import cv2
import numpy as np

def esikleme_q3(image_path_prefix='y_st', output_prefix='zsb_', threshold_value=158):
    for i in range(1, 16):
        try:
            # Resmi yükleyin
            image = cv2.imread(f'{image_path_prefix}{i}.jpg')

            # Resmi siyah-beyaz yapın
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Eşik ayarı yapın (bu eşik değeri deneme yanılma ile ayarlanabilir)
            ret, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

            # Resmi kaydedin
            cv2.imwrite(f'{output_prefix}{i}.jpg', thresholded_image)
        
        except Exception as e:
            print(f'Hata oluştu: {e}')
            continue  # Hata oluştuğunda işlemi devam ettir

    # Pencereyi kapatın
    cv2.destroyAllWindows()

# İşlemleri çağırarak kodu çalıştırın
esikleme_q3()