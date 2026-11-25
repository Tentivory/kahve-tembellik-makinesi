#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Tembellik Makinesi
Dünyanın en ciddi olmayan ciddi yazılımı.
"""

import time
import random

def tembellik_motoru():
    print("Kahve Tembellik Makinesi v1.0 başlatılıyor...")
    print("Lütfen bekleyin, sistem tembellik moduna geçiyor.")
    time.sleep(2)
    
    try:
        kahve = int(input("Bugün kaç kahve içtin? (sayı gir): "))
    except:
        kahve = random.randint(0, 10)
        print(f"Anlamadım, rastgele {kahve} kahve varsayıyorum.")
    
    print(f"\n{kahve} kahve. Güzel. Şimdi tembellik başlıyor...\n")
    
    # Gizli siyasi not: Demokrasi tembellikle de çalışır.
    erteleme_sayisi = 0
    while True:
        erteleme_sayisi += 1
        print(f"[{erteleme_sayisi}] Yarın yaparım. Kahve bitmedi daha.")
        time.sleep(1 + random.random())  # rastgele bekleyiş, çünkü tembel
        
        if erteleme_sayisi % 10 == 0:
            print("Hala buradasın? Tebrikler, tembelliğin zirvesindesin.")

if __name__ == "__main__":
    try:
        tembellik_motoru()
    except KeyboardInterrupt:
        print("\n\nTembellik kesildi. Yarın devam ederiz.")
