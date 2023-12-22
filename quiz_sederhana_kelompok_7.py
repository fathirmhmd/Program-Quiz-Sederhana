# -*- coding: utf-8 -*-
"""Quiz Sederhana-Kelompok 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AWJw5rU9hm_NyFVNFU0hJqkOjvNFXAkY
"""

import random

pertanyaan_jawaban = {
    "Apa ibukota Indonesia?": "jakarta",
    "Berapakah hasil dari 2 + 2?": "4",
    "Siapakah presiden pertama Indonesia?": "soekarno",
    "Apa nama planet terbesar di tata surya?": "jupiter",
    "Siapakah penulis novel To Kill a Mockingbird?": "harper lee",
    "Berapa jumlah gigi dewasa pada manusia biasanya?": "32",
    "Apa nama mata uang resmi Jepang?": "yen",
    "Siapakah penemu teleskop?": "galileo galilei" ,
    "Apa nama presiden pertama Amerika Serikat?": "george washington",
    "Apa singkatan dari DNA?": "deoksiribonukleat",
    "Siapa tokoh ilmuwan yang merumuskan hukum gravitasi?": "isaac newton",
    "Apa arti dari singkatan NASA?": "national aeronautics and space administration",
    "Siapakah penulis buku Harry Potter?": "j.k. rowling",
    "Golongan darah apa yang paling banyak di dunia?" : "O",
    "Vitamin yang paling banyak terkandung dalam buah buahan?": "C",
    "Sungai terpanjang di dunia adalah?": "nil",
    "Penemu lampu adalah?": "thomas alpha edison",
    "Dari partai mana Puan Maharani?": "pdip",
    "negara Asia yang tidak pernah dijajah?": "thailand",
    "berapa lama capung bertahan hidup?": "24 jam",
    "Simbol kimia perak adalah?": "ag",
    "Apa nama planet terdekat dari Matahari?": "merkurius",
    "Berapa banyak planet dalam tata surya kita?": "8",
    "Berapa banyak benua di dunia?": "7",
    "Apa nama bunga nasional Indonesia?": "melati",
    "Apa nama alat yang digunakan untuk mengukur suhu tubuh?": "termometer",
    "Sebutkan nama samudra terluas di dunia": "samudra pasifik",
    "15 menit sama dengan berapa detik?": "900",
    "Di manakah letak Menara Pisa?": "italia",
    "Siapakah pelukis terkenal yang menciptakan karya Mona Lisa?": "leonardo da vinci.18",
    "negara terpadat penduduknya di dunia?": "china",
    "Disebut apakah binatang yang dapat hidup di dua alam?": "amfibi",
    "Kota paling boros listrik di asia adalah?": "tokyo",
    "Penemu telepon adalah?": "alexander Ggraham bell",
    "Christopher Columbus merupakan Penemu Benua?": "amerika",
    "Ibukota thailand?": "bangkok",
    "benua terluas di permukaan bumi adalah?": "asia",
    "Binatang yang suka makan biji kopi dan kotorannya bisa dijadikan kopi adalah?": "luwak",
    "Siapa nama Presiden Indonesia yang menjabat selama 31 tahun": "soeharto",
    "Nama kerajaan yang pertama kali berdiri di Indonesia?": "kutai",
    "Gurun terluas di dunia?": "sahara",
    "Hewan paling cerdas di dunia adalah?": "simpanse",
    "Ada berapa negara yang tergabung dalam ASEAN?": "10",
    "Dasar negara Indonesia adalah?": "pancasila",
    "Pusat peredaran tata surya adalah?": "matahari",
    "Siapa nama Nabi yang pernah ditelan ikan paus?": "yunus",
    "Kerja paksa pada zaman penjajahan Jepang disebut apa?": "romusha",
    "Pusat keuangan kota Amerika Serikat adalah?": "new york",
    "Selain hiroshima kota yang juga di jatuhi bom oleh amerika ialah?": "nagasaki",
    "Hewan apakah yang memiliki kemampuan lari tercepat di dunia?": "cheetah",
    "Berapakah jumlah bulu sayap burung garuda?": "17",
    "Negara manakah yang memiliki wilayah terluas di dunia": "rusia",
    "Nama makanan khas Indonesia yang pernah dicanangkan sebagai makanan terenak di dunia adalah?": "rendang",
    "Sebutkan nama negara termuda yang tergabung dalam ASEAN!": "timor leste",
    "Ada pepatah lebih baik terlambat daripada ...?": "tidak sama sekali",
    "Hewan dengan julukan raja hutan?": "singa",
    "Terkenal dengan racun berupa bisa dengan bentuk tubuh memanjang dan bisa meliuk, siapa dia?": "ular",
    "Siapa nama pelatih timnas Indonesia?": "shin tae yong",
    "Pemain sepak bola yang di kenal dengan selebrasi siuuu adalah?": "ronaldo",
    "Nama mata uang Thailand adalah?": "bath",
    "Mata uang Malaysia?": "ringgit",
    "Candi Borubur merupakan candi agama?": "budha",
    "Jari-jari sebuah lingkaran 7 cm. Berapa luasnya!": "154 cm",
    "Mie favorit Jepang yaitu?": "ramen",
    "Minuman terfavorit di dunia adalah?": "teh",
    "Negara terkaya di dunia adalah?": "qatar",
    "Negara termiskin di dunia adalah?": "kongo",
    "Serangga yang memiliki rasa solidaritas tinggi adalah?": "semut",
    "Jumlah tangan ayam sebanyak?": "tidak ada",
    "Spongebob Squarepants tinggal di daerah?": "bikini bottom",
    "Negara terluas keempat di dunia adalah?": "amerika serikat",
    "Patung Sphinx kebanyakan terdapat di negara?": "mesir",
    "Hewan terkecil adalah?": "amuba",
    "Jumlah bidak papan catur adalah?": "64",
    "Pohon yang melambangkan hari natal adalah pohon?": "cemara",
    "Ibukota negara Rusia yaitu?": "moscow",
    "Paus pembunuh adalah nama lain dari paus?": "orca",
    "Rumput yang tumbuh paling cepat adalah?": "bambu",
    "Nama kapal pesiar yang tenggelam pada 15 Juni 1912 adalah?": "titanic",
    "Bahan utama pembuatan lipstik adalah?": "sisik ikan",
    "Produk makanan yang memiliki moto Berapa lapis? Ratusan adalah?": "tango",
    "Pakaian tradisional khas Indonesia yang bernilai seni tinggi adalah?": "batik",
    "Pakaian tradisional korea selatan adalah?": "hanbok",
    "Jumlah huruf abjad adalah?": "26",
    "Nama tokoh utama film toy story adalah?": "woody",
    "Tari kecak berasal dari daerah?": "bali'",
    "Nama panggilan anak kedua raffi ahmad dan nagita slavina adalah?": "cipung",
    "Kota terpadat di dunia adalah?": "seoul",
    "Mamalia tertinggi adalah?": "jerapah",
    "Kalau sedang sendiri, kakinya ada empat, kalau berdua, kakinya jadi ada delapan. Siapakah aku?": "kursi",
    "Siapakah yang mengetik naskah teks Proklamasi?": "sayuti melik",
    "Negara terkecil di dunia adalah?": "vatikan",
    "Kota terbesar ke 2 di Indonesia ialah?": "surabaya",
    "Makanan khas kota palembang?": "pempek",
    "Kota yang di juluki kota pahlawan ialah?": "surabaya",
    "Gunung tertinggi di dunia?": "everest",
    "Gedung tertinggi di dunia adalah?": "burj khalifa",
    "Kota padang terletak di pulau?": "sumatera",
    "Makanan khas makassar berupa pisang yang di balut adonan ialah?": "pisang ijo",
    "Tari kecak berasal dari?": "bali"
}
def acak_pertanyaan():
    pertanyaan = list(pertanyaan_jawaban.keys())
    random.shuffle(pertanyaan)
    return pertanyaan

def main():
    skor = 0
    pertanyaan_acak = acak_pertanyaan()
    hitung_pertanyaan = 0

    for pertanyaan in pertanyaan_acak:
        print(pertanyaan)
        jawaban_pengguna = input("Jawaban Anda: ").strip()

        if jawaban_pengguna.lower() == pertanyaan_jawaban[pertanyaan].lower():
            print("Benar!\n")
            skor += 10
        else:
            print(f"Salah. Jawaban yang benar adalah: {pertanyaan_jawaban[pertanyaan]}\n")

        hitung_pertanyaan += 1

        if hitung_pertanyaan == 10:
            pilihan = input("Anda sudah menjawab 10 pertanyaan. Apakah ingin melanjutkan? (ya/tidak): ").lower()
            if pilihan != 'ya':
                break
            else:
                acak_pertanyaan()
                main()

    print(f"Skor Anda: {skor}/{len(pertanyaan_jawaban)}")

if __name__ == "__main__":
    main()