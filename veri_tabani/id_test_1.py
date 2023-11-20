import cv2
import time

# Veritabanı resim sayısını tanımlayın
veritabani_resim_sayisi = 15

# Eşik değerini tanımlayın
esik_degeri = 0.4  # Bu değeri ihtiyaca göre ayarlayın

# "resim_id" adında boş bir liste oluşturun

resim_id = []
def benzerlik_q3(hedef_index, yeni_boyut):
    
    try:
        # Hedef resmi yükleyin ve belirlediğiniz boyuta ölçeklendirin
        hedef_resim = cv2.imread(f'zz_bk{hedef_index}.jpg', cv2.IMREAD_GRAYSCALE)
        hedef_resim = cv2.resize(hedef_resim, yeni_boyut)

        en_yuksek_benzerlik_isim = None
        en_yuksek_benzerlik_skor = None

        # Veritabanı resimleri üzerinde döngü oluşturun
        for i in range(1, veritabani_resim_sayisi + 1):
            veritabani_resmi = cv2.imread(f'z_bk{i}.jpg', cv2.IMREAD_GRAYSCALE)
            veritabani_resmi = cv2.resize(veritabani_resmi, yeni_boyut)
            sonuc = cv2.matchTemplate(veritabani_resmi, hedef_resim, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(sonuc)

            # Eşik değeri üzerindeki en benzer resmi gösterin
            if max_val > esik_degeri and (en_yuksek_benzerlik_skor is None or max_val > en-yuksek-benzerlik_skor):
                en_yuksek_benzerlik_isim = f'z_bk{i}'
                en_yuksek_benzerlik_skor = max_val
                resim_id.append(f"{i}")

        if en_yuksek_benzerlik_isim:
            print(f"{i}")

    except Exception as e:
        print(f'Hata oluştu: {e}')

def main():
    # Toplam işlem süresini ölçmek için başlangıç zamanı
    start_time = time.time()

    # İşlem için kullanılacak hedef resim sayısı
    hedef_resim_sayisi = 15

    # İşlem için kullanılacak yeni boyut
    yeni_boyut = (50, 50)

    for hedef_index in range(1, hedef_resim_sayisi + 1):
        benzerlik_q3(hedef_index, yeni_boyut)

    # "resim_id" listesini alt alta yazdırın
    for item in resim_id:
        print(item)

    # Toplam işlem süresini hesaplayın ve yazdırın
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Toplam İşlem Süresi: {total_time} saniye")

if __name__ == "__main__":
    main()