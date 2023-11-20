import cv2

def benzerlik_q3(hedef_resim_sayisi=15, veritabani_resim_sayisi=15):
    for hedef_index in range(1, hedef_resim_sayisi + 1):
        try:
            # Hedef resmi yükleyin ve boyutunu alın
            hedef_resim = cv2.imread(f'zz_bk{hedef_index}.jpg', cv2.IMREAD_GRAYSCALE)
            hedef_genislik, hedef_yukseklik = hedef_resim.shape[::-1]

            # En yüksek benzerlik skorunu ve resmin adını saklamak için değişkenler
            en_yuksek_benzerlik_isim = None
            en_yuksek_benzerlik_skor = None

            # Veritabanı resimleri üzerinde döngü oluşturun
            for i in range(1, veritabani_resim_sayisi + 1):
                veritabani_resmi = cv2.imread(f'z_bk{i}.jpg', cv2.IMREAD_GRAYSCALE)
                sonuc = cv2.matchTemplate(veritabani_resmi, hedef_resim, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, _ = cv2.minMaxLoc(sonuc)

                # En yüksek benzerlik skorunu güncelle
                if en_yuksek_benzerlik_skor is None or max_val > en_yuksek_benzerlik_skor:
                    en_yuksek_benzerlik_isim = f'z_bk{i}'
                    en_yuksek_benzerlik_skor = max_val

            # Her hedef resmi için en benzer resmi ve skorunu yazdırın
            print(f"Hedef Resim {hedef_index}:")
            print(f"En Fazla Benzeyen Resim: {en_yuksek_benzerlik_isim} (Benzerlik Skoru: {en_yuksek_benzerlik_skor})")
            print()

            # En fazla benzeyen resmi ekranda gösterin
            en_iyi_resim = cv2.imread(f'{en_yuksek_benzerlik_isim}.jpg')
            #cv2.imshow(f"En Fazla Benzeyen Resim (Hedef {hedef_index})", en_iyi_resim)
            #cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        except Exception as e:
            print(f'Hata oluştu: {e}')
            continue  # Hata oluştuğunda işlemi devam ettir

# İşlevi çağırarak kodu çalıştırın
benzerlik_q3()

