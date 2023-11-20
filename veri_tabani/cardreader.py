# cardreader.py
from time import sleep, time
from id_test_1 import benzerlik_q3  # Görüntü işleme işlevini içe aktarın

def read_process():
    reads = dict()
    poll_duration_in_s = 2.5
    total_read = 0

    try:
        old_time = 0
        while True:
            if time() - old_time < poll_duration_in_s:
                id = benzerlik_q3(resim_id)  # Görüntü işleme sonuçlarına dayalı kimlik tanıma
                if id:
                    reads[total_read + 1] = id
                    total_read += 1
                else:
                    if total_read != 0:
                        return reads
                    total_read = 0
                    old_time = time()
                    sleep(0.05)
                    sleep(0.05)

    except KeyboardInterrupt:
        raise
