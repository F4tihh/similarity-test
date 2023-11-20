import cv2

def benzerlik_fft(hedef_resim_sayisi=15, veritabani_resim_sayisi=15):
    for hedef_index in range(1, hedef_resim_sayisi + 1):
        try:
            # Hedef resmi yükleyin ve boyutunu alın
            hedef_resim = cv2.imread(f'zz_bk{hedef_index}.jpg', cv2.IMREAD_GRAYSCALE)
            hedef_genislik, hedef_yukseklik = hedef_resim.shape[::-1]

            # En yüksek benzerlik skorunu ve resmin adını saklamak için değişkenler
            en_yuksek_benzerlik_isim = None
            en_yuksek_benzerlik_skor = None

            # Hedef resmi SSIM benzerlik ölçümü için hazırlayın
            hedef_ssim_resmi = cv2.cvtColor(hedef_resim, cv2.COLOR_BGR2GRAY)

            # Veritabanı resimleri üzerinde döngü oluşturun
            for i in range(1, veritabani_resim_sayisi + 1):
                veritabani_resmi = cv2.imread(f'z_bk{i}.jpg', cv2.IMREAD_GRAYSCALE)
                
                # SSIM benzerlik ölçümünü hesaplayın
                ssim_degeri = cv2.compare_SSIM(hedef_ssim_resmi, veritabani_resmi)

                # En yüksek benzerlik skorunu güncelle
                if en_yuksek_benzerlik_skor is None or ssim_degeri > en_yuksek_benzerlik_skor:
                    en_yuksek_benzerlik_isim = f'z_bk{i}'
                    en_yuksek_benzerlik_skor = ssim_degeri

            # Her hedef resmi için en benzer resmi ve skorunu yazdırın
            print(f"Hedef Resim {hedef_index}:")
            print(f"En Fazla Benzeyen Resim: {en_yuksek_benzerlik_isim} (SSIM Benzerlik Skoru: {en_yuksek_benzerlik_skor})")
            print()

        except Exception as e:
            print(f'Hata oluştu: {e}')
            continue  # Hata oluştuğunda işlemi devam ettir

# İşlevi çağırarak kodu çalıştırın
benzerlik_fft()