from time import time

# resim_id dizisini tanımlayın (sırayla okunacak sayıları içermelidir)
resim_id = [1, 2, 3, 4, 5]  # Örnek olarak ilk beş sayıyı içerir

def read_process():
    reads = dict()
    poll_duration_in_s = 2.5
    try:
        old_time = 0
        total_read = 0
        while True:
            if time() - old_time < poll_duration_in_s:
                for resim in resim_id:
                    reads[len(reads) + 1] = resim
                total_read += 1
            else:
                if total_read != 0:
                    return reads
                for number, resim in sorted(reads.items()):
                    print("Okunan Resim ID: %d" % resim)
                reads.clear()
                print("Toplam Okuma = %d.\tCihazları okuyor..." % total_read)
                total_read = 0
                old_time = time()
                sleep(0.05)
                sleep(0.05)
    except KeyboardInterrupt:
        raise