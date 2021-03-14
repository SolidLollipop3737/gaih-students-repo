# -*- coding: utf-8 -*-
"""Colaboratory'ye Hoş Geldiniz

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

<p><img alt="Colaboratory logo" height="45px" src="/img/colab_favicon.ico" align="left" hspace="10px" vspace="0px"></p>

<h1>Colaboratory nedir?</h1>

Colaboratory &#40;ya da kısaca "Colab"&#41;, tarayıcınızda Python'u yazmanızı ve çalıştırmanızı sağlar. Üstelik: 
- Hiç yapılandırma gerektirmez
- GPU'lara ücretsiz erişim imkanı sunar
- Kolay paylaşım imkanı sunar

İster <strong>öğrenci</strong> ister <strong>veri bilimci</strong> ister <strong>yapay zeka araştırmacısı</strong> olun, Colab işinizi kolaylaştırabilir. Daha fazla bilgi edinmek için <a href="https://www.youtube.com/watch?v=inN8seMm7UI">Colab'e Giriş</a> videosunu izleyebilir ya da aşağıdan hemen kullanmaya başlayabilirsiniz.

## <strong>Başlarken</strong>

Okuduğunuz doküman statik bir web sayfası değil, kod yazmanıza ve yürütmenize imkan veren <strong>Colab not defteri</strong> adında etkileşimli bir ortamdır.

Örneğin, buradaki <strong>kod hücresinde</strong>, bir değeri hesaplayan, bir değişken içinde saklayan ve sonucu yazdıran kısa bir Python dizesi görebilirsiniz:
"""

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

"""Yukarıdaki hücrede kodu yürütmek için tıklayarak seçin, ardından ya kodun sol tarafındaki oynat düğmesine basın ya da "Command/Ctrl+Enter" klavye kısayolunu kullanın. Kodu düzenlemek için hücreyi tıklamanız yeterlidir. Sonrasında düzenlemeye başlayabilirsiniz.

Bir hücrede tanımladığınız değişkenler daha sonra başka hücrelerde kullanılabilir:
"""

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week

"""Colab not defterleri; <strong>yürütülebilir kod</strong>, <strong>zengin metin</strong>, <strong>resimler</strong>, <strong>HTML</strong>, <strong>LaTeX</strong> ve diğer öğeleri tek bir dokümanda birleştirmenizi sağlar. Oluşturduğunuz Colab not defterleri Google Drive hesabınızda saklanır. Colab not defterlerinizi arkadaşlarınızla veya iş arkadaşlarınızla kolayca paylaşabilir, not defterlerinize yorum yapmalarını, hatta düzenlemelerini sağlayabilirsiniz. Daha fazla bilgiyi <a href="/notebooks/basic_features_overview.ipynb">Colab'e Genel Bakış</a> bölümünde bulabilirsiniz. Yeni bir Colab not defteri oluşturmak için yukarıdaki Dosya menüsünü ya da <a href="http://colab.research.google.com#create=true">yeni bir Colab not defteri oluşturma</a> bağlantısını kullanabilirsiniz.

Colab not defterleri, Colab tarafından barındırılan Jupyter not defterleridir. Jupyter projesi hakkında daha fazla bilgiyi <a href="https://www.jupyter.org">jupyter.org</a> adresinde bulabilirsiniz.

## Veri bilimi

Colab ile popüler Python kitaplıklarının tüm avantajlarından yararlanarak veri analiz edip görselleştirebilirsiniz. Aşağıdaki kod hücresi rastgele veri oluşturmak için <strong>numpy</strong>'yi, bu veriyi görselleştirmek için de <strong>matplotlib</strong>'i kullanır. Kodu düzenlemek için hücreyi tıklamanız yeterlidir. Sonrasında düzenlemeye başlayabilirsiniz.
"""

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

"""Kendi verilerinizi Google Drive hesabınızdan &#40;e-tablolar dahil&#41;, GitHub'dan ve diğer pek çok kaynaktan Colab not defterlerine aktarabilirsiniz. Veri içe aktarma ve Colab'in veri bilimi için nasıl kullanılabileceği hakkında daha fazla bilgi edinmek için <a href="#working-with-data">Verilerle Çalışma</a> bölümünün altındaki bağlantılara bakabilirsiniz.

## Makine öğrenimi

Colab ile bir resim veri kümesini içe aktarabilir, üzerinde bir resim sınıflandırıcıyı eğitebilir ve modeli değerlendirebilirsiniz. Hem de sadece <a href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb">birkaç satır kodla</a>. Colab not defterleri Google'ın bulut sunucularında kod yürütür. Yani makinenizin gücünden bağımsız olarak, <a href="#using-accelerated-hardware">GPU'lar ve TPU'lar</a> dahil Google donanımının gücünden yararlanabilirsiniz. Tek ihtiyacınız olan şey bir tarayıcıdır.

Colab, makine öğrenimi topluluğunda yaygın olarak şu uygulamalarla kullanılır:
- TensorFlow'u kullanmaya başlama
- Nöral ağ geliştirme ve eğitme
- TPU'lar ile deneme yapma
- Yapay zeka araştırmalarını yayma
- Eğitici oluşturma

Makine öğrenimi uygulamalarını açıklayarak tanıtan örnek Colab not defterlerini görmek için aşağıdaki <a href="#machine-learning-examples">makine öğrenimi örneklerine</a> bakabilirsiniz.

## Diğer Kaynaklar

### Colab'de Not Defterleriyle Çalışma
- [Colaboratory'ye Genel Bakış](/notebooks/basic_features_overview.ipynb)
- [Markdown rehberi](/notebooks/markdown_guide.ipynb)
- [Kitaplıkları içe aktarma ve bağımlıları yükleme](/notebooks/snippets/importing_libraries.ipynb)
- [GitHub'da not defteri kaydetme ve yükleme](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
- [Etkileşimli formlar](/notebooks/forms.ipynb)
- [Etkileşimli widget'lar](/notebooks/widgets.ipynb)
- <img src="/img/new.png" height="20px" align="left" hspace="4px" alt="New"></img>
 [Colab'de TensorFlow 2](/notebooks/tensorflow_version.ipynb)

<a name="working-with-data"></a>
### Verilerle Çalışma
- [Veri yükleme: Drive, E-Tablolar ve Google Cloud Storage](/notebooks/io.ipynb) 
- [Grafikler: Veri görselleştirme](/notebooks/charts.ipynb)
- [BigQuery'yi kullanmaya başlama](/notebooks/bigquery.ipynb)

### Makine Öğrenimi Hızlandırılmış Kursu
Google'ın online Makine Öğrenimi kursundan birkaç not defterini burada bulabilirsiniz. Daha fazlası için <a href="https://developers.google.com/machine-learning/crash-course/">tam kurs web sitesine</a> bakın.
- [Pandas'a giriş](/notebooks/mlcc/intro_to_pandas.ipynb)
- [TensorFlow kavramları](/notebooks/mlcc/tensorflow_programming_concepts.ipynb)
- [TensorFlow ile ilk adımlar](/notebooks/mlcc/first_steps_with_tensor_flow.ipynb)
- [Nöral ağlara giriş](/notebooks/mlcc/intro_to_neural_nets.ipynb)
- [Seyrek veriler ve yerleştirilmiş öğelere giriş](/notebooks/mlcc/intro_to_sparse_data_and_embeddings.ipynb)

<a name="using-accelerated-hardware"></a>
### Hızlandırılmış Donanım Kullanma
- [GPU'lar ile TensorFlow](/notebooks/gpu.ipynb)
- [TPU'lar ile TensorFlow](/notebooks/tpu.ipynb)

<a name="machine-learning-examples"></a>

## Makine Öğrenimi Örnekleri

Colaboratory'nin mümkün kıldığı etkileşimli makine öğrenimi analizlerinin uçtan uca örneklerini görmek için, <a href="https://tfhub.dev">TensorFlow Hub</a>'daki modelleri kullanan bu eğiticilere bakın.

Öne çıkan birkaç örnek:

- <a href="https://tensorflow.org/hub/tutorials/tf2_image_retraining">Bir Resim Sınıflandırıcıyı Yeniden Eğitme</a>: Çiçekleri ayırt etmek için önceden eğitilmiş bir resim sınıflandırıcının üzerine bir Keras modeli inşa eder.
- <a href="https://tensorflow.org/hub/tutorials/tf2_text_classification">Metin Sınıflandırma</a>: IMDB'deki film yorumlarını <em>olumlu</em> veya <em>olumsuz</em> olarak sınıflandırır.
- <a href="https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization">Stil Aktarımı</a>: Resimler arasında stil aktarımı yapmak için derin öğrenmeyi kullanır.
- <a href="https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa">Çok Dilli Evrensel Cümle Kodlayıcı Soru-Cevap</a>: SQuAD veri kümesinden soruları cevaplamak için bir makine öğrenimi modeli kullanır.
- <a href="https://tensorflow.org/hub/tutorials/tweening_conv3d">Video İnterpolasyonu</a>: Bir videonun ilk ve son karesi arasında ne olduğunu tahmin eder.
"""

x=1
y=2
z=0
print("10 soruluk yarismamiza hos geldiniz!")
print("Sorular tek cevaplidir.")
print("5 soruyu doğru bilirseniz basarili olursunuz.")

while x<y:
  x=x+1
  print ("1. soru: 12'nin karesi kactir?")
  cevap = input("cevabiniz?")
  if cevap == "144":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("2. soru: en koyu renk? ")
  cevap = input("cevabiniz?")
  if cevap == "Siyah":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("3. soru: Türk bayraginda ay yanında ne vardir?")
  cevap = input("cevabiniz?")
  if cevap == "Yildiz":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("4. soru: Türkiyenin en kalabalik sehri ?")
  cevap = input("cevabiniz?")
  if cevap == "Istanbul":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("5. soru: dijital tarih baslangic yili?")
  cevap = input("cevabiniz?")
  if cevap == "1970":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("6. soru: atatürkün 2. adı nedir?")
  cevap = input("cevabiniz?")
  if cevap == "Kemal":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("7. soru: Benim adim nedir?")
  cevap = input("cevabiniz?")
  if cevap == "Onur":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("8. soru: Python mu C++ mı?")
  cevap = input("cevabiniz?")
  if cevap == "Python":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("9. soru: dik üçgenin dik açısı?")
  cevap = input("cevabiniz?")
  if cevap == "90":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("10. soru: Denizlide deniz var mi?")
  cevap = input("cevabiniz?")
  if cevap == "Hayir":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1

if z < 5:
  print("basarisiz oldunuz")
  print("dogru sayiniz: ", z )
else:
  print("Helal ödülü hak ettin")
  print("dogru sayiniz: ", z )