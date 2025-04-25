🖱️ MPU6050 ve Raspberry Pi RP2040-Zero ile Hareketle Fare Kontrolü
Bu proje, Raspberry Pi RP2040-Zero ve MPU6050 hareket sensörü ile bilgisayar faresini hareket ettirmenizi sağlar. 
Sensörden alınan ivme verilerine göre imleç yönlendirilir.


📦 Gereksinimler
Raspberry Pi RP2040-Zero

MPU6050 İvmeölçer/Jiroskop Sensörü

CircuitPython yazılımı (adafruit-circuitpython-raspberry_pi_pico-tr-9.2.7)
	
adafruit_hid, adafruit_mpu6050 gibi gerekli kütüphaneler(lib klasörünü direkt kopyala yapıştır yapabilirsin)

(İsteğe bağlı) Tıklama işlemleri için 2 adet buton


🚀 Kurulum Adımları
CircuitPython'u İndir ve Yükle
CircuitPython firmware dosyasını indir ve RP2040-Zero’ya yükle:
adafruit-circuitpython-raspberry_pi_pico-tr-9.2.7
	
Kütüphaneleri Kopyala

Yazılım yüklendikten sonra bilgisayarında CIRCUITPY adında bir USB sürücüsü belirecek.

Bu sürücüdeki lib klasörünü aç.

İndirdiğin lib klasörünün içindeki gerekli dosyaları buraya kopyala.
(örn. adafruit_hid, adafruit_mpu6050 vb.)(lib klasörünü direkt kopyala yapıştır yapabilirsin)

Kod Dosyasını Ekle


Hareket sensörü ile fareyi kontrol eden Python kodunu bu dosyaya yapıştır ve kaydet.

Projeyi Çalıştır

Raspberry Pi RP2040-Zero üzerindeki reset (sıfırlama) düğmesine bas.

Kod otomatik olarak çalışacak.

MPU6050’i hareket ettirerek imleci kontrol etmeye başlayabilirsin!


🛠️ Notlar
Koddaki sensitivity (hassasiyet) ve spanmin/spanmax gibi eşik değerlerini ayarlayarak imleç hareketlerini ince ayar yapabilirsin.

Sensör bağlantılarının I2C pinlerine uygun olduğundan emin ol (varsayılan: SDA=GP0, SCL=GP1).

GP2 pinine bir buton bağlayarak sağ tıklama gibi işlemleri de sonradan ekleyebilirsin.