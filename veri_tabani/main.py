# main.py
from id_test_1 import benzerlik_q3  # Görüntü işleme işlevini içe aktarın
from cardreader import read_process  # Kart okuma işlevini içe aktarın

if __name__ == "__main__":
    # İşlem için gerekli ayarlar veya başlangıç işlemleri
    # Eğer herhangi bir ayar yapmanız gerekiyorsa, burada yapabilirsiniz.

    try:
        # Kart okuma işlemini başlatın
        read_process()

        # Görüntü işleme sonuçlarından gelen kimlikleri kullanarak istediğiniz işlemleri yapabilirsiniz.
        # Örneğin:
        #   - Kimlik tanınan bir kişiye özel bir işlem yapma
        #   - Kimlik tanınan bir kişiyi bir veritabanında arama
        #   - Kimlik tanınan bir kişiyi sistemden çıkarma

    except KeyboardInterrupt:
        # İşlemi kullanıcı tarafından kesmek için Ctrl+C tuşları kullanılırsa temizlik işlemleri yapın.
        # Örneğin, GPIO pinlerini temizleme işlemi burada yapılabilir.

        pass
