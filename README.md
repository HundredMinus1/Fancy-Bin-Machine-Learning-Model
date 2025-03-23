# **📝 Waste Classification - by FancyBin** 

Klasifikasi sampah anorganik dan organik menggunakan Tensorflow dan Keras (Deep Learning) berdasarkan input gambar.

File yang digunakan `Model.ipynb`

## **✅ Team Machine Learning ✅**
- Habib Septrian Priyanto
- Juan Andrean Miliandza

## **💼 Dataset 💼**
Dataset yang digunakan "Waste Classification Data" dari Kagglemenggunakan Kaggle API.

`!kaggle datasets download techsash/waste-classification-data`

## **📍 Model Baseline📍**
Model yang digunakan **Convolutional Neural Network (CNN)** yang terdiri dari beberapa lapisan parameter:

- Conv2D: Lapisan konvolusi dengan 32 filter dan ukuran kernel (3,3).

- MaxPooling2D: Lapisan pooling untuk mengurangi dimensi fitur.

- Flatten: Mengubah fitur yang diekstrak menjadi bentuk vektor 1D.

- Dense (64 neuron): Lapisan fully connected dengan fungsi aktivasi ReLU.

- Dropout (0.2): Mengurangi overfitting dengan mengabaikan 20% dari neuron secara acak.

- BatchNormalization: Normalisasi agar jaringan lebih stabil.

- Output Layer: Menggunakan 1 neuron dengan aktivasi sigmoid untuk klasifikasi biner.

## **📍 Hasil Evaluasi Model📍**

Accuracy: 99.21%
Validation Accuracy: 92.58%
Epoch Total: 8

# **💻 Application 💻** 
Aplikasi berbasis Flask yang menyediakan endpoint untuk melakukan klasifikasi sampah berdasarkan gambar yang diunggah pengguna.

File yang digunakan `app.ipynb`

 ## **📍 Endpoint📍**
 ### Prediksi Sampah

- URL: /predict
- Method: POST
- Input: Gambar
- Output: JSON yang berisi hasil klasifikasi (Organic atau Anorganic) beserta probabilitasnya.