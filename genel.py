from resim_cek import resim_cek
from ilk_secim_q3 import ilk_secim_q3
from kesilen_q3 import kesilen_q3
from sekil_q3 import sekil_q3
from esikleme_q3 import esikleme_q3
from sekil_siyah_q3 import sekil_siyah_q3
from benzerlik_q3 import benzerlik_q3
from jpg_dosyalari_sil import jpg_dosyalari_sil

import time

start_time = time.time()

resim_cek()
# İlk işlemi çağırın
ilk_secim_q3('w3.jpg')


# İkinci işlemi çağırın
kesilen_q3()

# İkinci işlemin tamamlanmasını bekle


# Diğer işlemleri sırayla çağırın ve her işlem tamamlandığında bekleyin
sekil_q3()


esikleme_q3()


sekil_siyah_q3()


benzerlik_q3()

jpg_dosyalari_sil()

end_time = time.time()
print(f"İlk işlem süresi: {end_time - start_time} saniye")
