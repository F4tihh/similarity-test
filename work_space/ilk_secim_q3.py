import cv2
import numpy as np

def ilk_secim_q3(image_path, output_prefix='Bk_', min_kart_boyutu=100, maksimum_kart_sayisi=15):
    try:
        # Resmi yükleyin
        karton_resmi = cv2.imread(image_path)

        # Resmi gri tona dönüştürün
        gri_karton = cv2.cvtColor(karton_resmi, cv2.COLOR_BGR2GRAY)

        # Kenar algılamayı (örneğin, Canny kenar algılama) uygulayın
        kenarlar = cv2.Canny(gri_karton, threshold1=30, threshold2=100)

        # Kenarlar üzerinde konturları bulun
        konturlar, _ = cv2.findContours(kenarlar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Beyaz kartları tespit etmek için bir bölge listesi oluşturun
        beyaz_kart_bolgeleri = []

        for kontur in konturlar:
            x, y, w, h = cv2.boundingRect(kontur)  # Konturun sınırlayıcı kutusunu alın

            # Kartların boyutunu ve şeklini filtrelemek için uygun bir kriter kullanın
            if w > min_kart_boyutu and h > min_kart_boyutu:
                beyaz_kart_bolgeleri.append((x, y, w, h))

                # Maksimum kart sayısını kontrol edin
                if len(beyaz_kart_bolgeleri) >= maksimum_kart_sayisi:
                    break  # Maksimum kart sayısına ulaştığınızda döngüden çıkın

        # Her bir beyaz kartı kesin ve ayrı bir dosya olarak kaydedin
        for i, (x, y, w, h) in enumerate(beyaz_kart_bolgeleri):
            kart_resmi = karton_resmi[y:y+h, x:x+w]  # Beyaz kartı kesin

            # Kartın içeriğini işlemek için burada ek işlemleri ekleyebilirsiniz
            # Örneğin, renkli şekil tespiti veya diğer işlemler

            # Her bir kartı ayrı bir dosya olarak kaydedin
            cv2.imwrite(f'{output_prefix}{i + 1}.jpg', kart_resmi)

        cv2.destroyAllWindows()
    except Exception as e:
        print(f'Hata: {e}. İşlev çalıştırılamadı.')

# İşlevi çağırarak kodu çalıştırın
ilk_secim_q3('w3.jpg')
