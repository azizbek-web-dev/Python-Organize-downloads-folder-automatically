# Downloads Folder Organizer

Python skripti, yuklab olingan fayllarni turli formatlar bo'yicha to'g'ri papkalarga avtomatik tashlab beradi. Skript Pythonning standart kutubxonasidan foydalanadi va to'liq sharhlangan kod bo'lib, har bir funksiya aniq izoh berilgan. Ikki xil fayl uzanib qolsa, ikkinchisiga raqam qo'shib qo'yadi. Jarayon yakunida hisobot ko'rsatadi.

## Xususiyatlar

Skript quyidagi imkoniyatlarga ega. Fayllar avtomatik ravishda tegishli papkalarga tushadi. Agar papkada xuddi shu nomdagi fayl bo'lsa, yangi faylga raqam qo'shib saqlashadi. Ishlash tugallangacha fayl topish, qayerga qo'yilishi va barqaror ishlash holatini kuzatib boradi. Oxirida umumiy statistik ma'lumot ko'rsatiladi. Tashqi kutubxonalar kerak emas, faqat Python o'zi yetadi. Kodga ko'z tashlasangiz, har bir qismi tushunarli va alohida sharhlangan.

## Fayl Kategoriyalari

Bu script fayllarni quyidagi papkalarga ajratadi. Rasmlar uchun images papkasiga, video fayllar uchun videos papkasiga, musiqa uchun music papkasiga, hujjatlar uchun documents papkasiga, arxivlar uchun archives papkasiga, dasturlar uchun executables papkasiga, kod fayllari uchun code papkasiga, fontlar uchun fonts papkasiga, jadvallar uchun spreadsheets papkasiga, taqdimotlar uchun presentations papkasiga tushadi. Agar fayl qo'shimcha kategoriyalarga mos kelmasa, others papkasiga qo'yiladi.

Rasm formatlari: jpg, jpeg, png, gif, bmp, svg, webp, ico, tiff, heic. Video formatlari: mp4, avi, mov, mkv, flv, wmv, webm, m4v, 3gp. Musiqa formatlari: mp3, wav, flac, aac, ogg, wma, m4a. Hujjatlar: pdf, doc, docx, txt, rtf, xls, xlsx, ppt, pptx, csv. Arxivlar: zip, rar, 7z, tar, gz, bz2, xz, iso. Dasturlar: exe, msi, dmg, pkg, deb, rpm, appimage. Kod: py, js, html, css, java, cpp, c, php, rb, go, ts. Fontlar: ttf, otf, woff, woff2, eot. Jadval formatlari: csv, xlsx, xls, ods. Taqdimotlar: pptx, ppt, odp.

## Talablar

Bu loyihani ishga tushirish uchun Python 3.6 yoki undan yuqori versiya o'rnatilgan bo'lishi kerak. Qo'shimcha kutubxonalar talab qilinmaydi, faqat Python standart kutubxonasi ishlatiladi.

## O'rnatish

Birinchidan, GitHub'dan loyihani clone qilib oling. Terminal yoki cmd ochib quyidagi buyruqlarni bajaring. Avval repository'ni klonlang, so'ng loyiha papkasiga kirib oling. Boshqa hech narsa o'rnatish shart emas, faqat Python bilan skriptni ishga tushiring.

```bash
git clone https://github.com/azizbek-web-dev/Python---Organize-downloads-folder-automatically.git
cd Python---Organize-downloads-folder-automatically
```

## Qanday Ishlatiladi

Skriptni ishga tushirish uchun terminalda yoki PowerShellda quyidagi buyruqni kiriting. Bu skript avtomatik ravishda Downloads papkangizdagi barcha fayllarni to'g'ri papkalarga tashlab beradi. Har bir fayl qayerda borligini ekranga chiqaradi va yakunida jami qancha fayl ko'chirilgani haqida hisobot beradi.

```bash
python organize_downloads.py
```

Agar Downloads papkasi o'rniga boshqa papkani tartibga solmoqchi bo'lsangiz, koddagi downloads_path o'zgaruvchisiga kerakli manzilni kiriting va sakriptni o'sha papka uchun moslashtiring.

```python
organizer = DownloadsOrganizer(downloads_path="C:/Users/YourName/Desktop/MyFolder")
organizer.organize_files()
```

## Ishlash Natijasi

Skript ishga tushirilganda quyidagi kabi chiqadi. Avval skript nomi va murojaat ko'rsatiladi, so'ng Downloads papkasi qidiriladi va tarkibi tekshiriladi. Har bir fayl ko'chirilganda qaysi papkaga qo'yilgani ko'rsatiladi. Agar takroriy fayl bo'lsa, unga raqam qo'shib saqlanadi. Yakunida jami qancha fayl topilgani, qanchasini tashlaganlari, qanchasi takroriy bo'lgani va xatolar miqdori ko'rsatiladi.

```
============================================================
Downloads Folder Organizer
============================================================

Organizing files in: C:\Users\YourName\Downloads
------------------------------------------------------------
document.pdf -> documents/document.pdf
image.jpg -> images/image.jpg
video.mp4 -> videos/video.mp4
Renamed duplicate: document.pdf -> document_1.pdf
------------------------------------------------------------
Organization Summary:
  Total files found: 25
  Files organized: 25
  Duplicates renamed: 3
  Errors: 0

Your Downloads folder is now organized.
```

## Qanday Ishlaydi

Skript ishga tushganda Downloads papkasini to'liq ko'rib chiqadi va har bir faylni o'qidi. Keyin fayl kengaytmasi asosida qaysi kategoriyaga tegishli ekanligini aniqlaydi. Fayllar tegishli papkalarga ko'chiriladi va takroriy fayllar uchun raqam qo'shiladi. Jarayon tugagandan so'ng hisobot ko'rsatiladi.

## Xavfsizlik

Skript faqat Downloads papkasi ichidagi fayllarni ko'chirib beradi, tashqariga chiqmaydi. Takroriy fayllar o'rniga yangi raqam qo'shiladi, tushmaydigan fayllar uchun xato bilan ishlash kodi bor. Fayllar o'chirilmaydi, faqat ko'chiriladi va Downloads papkasining asl struktura saqlanadi.

## O'zgartirish

Agar yangi kategoriya qo'shmoqchi bo'lsangiz, organize_downloads.py faylini oching va FILE_CATEGORIES lug'atiga yangi qator qo'shing. Papka nomlarini o'zgartirmoqchi bo'lsangiz, lug'at kalitlarini yangilang. Yangi fayl formatlarini qo'shmoqchi bo'lsangiz, tegishli kategoriya ichiga kiriting.

Misol uchun:
```python
FILE_CATEGORIES = {
    'images': ['.jpg', '.jpeg', '.png', '.your-extension'],
    'your-category': ['.ext1', '.ext2'],
}
```

## Qo'shimcha Ma'lumotlar

Skript faqat Downloads papkasining asosiy papkasidagi fayllarni tartibga oladi, ichki papkalarga kirmaydi. Kategoriya papkalarida allaqachon bo'lgan fayllar o'chirilmaydi, faqat yangilariga raqam qo'shiladi. Skriptni istalgan vaqtda ishga tushirib, Downloads papkangizni tartibda saqlashingiz mumkin.
