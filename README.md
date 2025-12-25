# Gemini Text Summarizer

Gemini API (Google GenAI) ve Gradio kullanılarak geliştirilmiş,  
kullanıcıdan alınan metni hızlıca özetleyen basit ve modern bir web uygulaması.

## 🚀 Özellikler

- Gemini 2.5 Flash modeli ile metin özetleme
- Gradio tabanlı sade ve kullanıcı dostu arayüz
- Docker ile tek komutla çalıştırma
- API key güvenliği (`.env` kullanımı)
- Gradio 6.x uyumlu yapı

---

## 🖥️ Ekran Görüntüsü

<img width="1868" height="931" alt="image" src="https://github.com/user-attachments/assets/6e5a4075-6af5-40c8-93b9-a4b714e40717" />
<img width="1652" height="914" alt="image" src="https://github.com/user-attachments/assets/bafafdd4-3e28-491a-b640-b99267b7ab5f" />



---

## 📦 Gereksinimler

### Lokal çalıştırma için:
- Python 3.10+
- pip

### Docker ile çalıştırma için:
- Docker
- Docker Desktop (Windows / macOS)

---

## 🔑 Ortam Değişkenleri

Proje kök dizininde bir `.env` dosyası oluştur:

```env
GEMINI_API_KEY=buraya_api_keyini_yaz
