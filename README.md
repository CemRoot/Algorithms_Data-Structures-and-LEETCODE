<div align="center">

# 🚀 Algorithms & Data Structures

### A Comprehensive Journey Through Computer Science Fundamentals

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

[English](#english) | [Türkçe](#turkish)

</div>

---

## <a id="english"></a>🇬🇧 English

### 📖 Overview

This repository serves as a comprehensive collection of fundamental algorithms, data structures, and LeetCode problem solutions. Designed for both learning and interview preparation, it provides clear, well-documented implementations with detailed complexity analysis.

### ✨ Features

- **Clean Code**: Well-commented implementations with step-by-step explanations
- **Complexity Analysis**: Detailed Big-O notation for time and space complexity
- **Practical Examples**: Real-world use cases and test scenarios
- **Interview Ready**: Solutions to common coding interview problems
- **Bilingual**: Full documentation in both English and Turkish

### 📁 Repository Structure

```
Algorithms_Data-Structures-and-LEETCODE/
│
├── data-structures/           # Data structure implementations
│   └── linked-list/
│       ├── singly-linked-list/    # Singly linked list operations
│       └── doubly-linked-list/    # Doubly linked list operations
│
├── algorithms/                # Algorithm implementations
│   └── big-o-examples/        # Time complexity demonstrations
│
└── docs/                      # Additional documentation and notes
```

### 🔗 Data Structures

#### Singly Linked List
Complete implementation with the following operations:

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| `append(value)` | Add node to end | O(1) |
| `prepend(value)` | Add node to beginning | O(1) |
| `pop()` | Remove last node | O(n) |
| `pop_first()` | Remove first node | O(1) |
| `get(index)` | Access node by index | O(n) |
| `set_value(index, value)` | Update node value | O(n) |
| `insert(index, value)` | Insert at specific index | O(n) |
| `remove(index)` | Remove at specific index | O(n) |
| `reverse()` | Reverse the list | O(n) |

**📂 Location**: `data-structures/linked-list/singly-linked-list/`

#### Doubly Linked List
*(Under Development)*

**📂 Location**: `data-structures/linked-list/doubly-linked-list/`

### 📊 Big-O Complexity Reference

> 💡 **Resource**: [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

#### Complexity Guide

| Notation | Performance | Description |
|----------|-------------|-------------|
| O(1) | 🟢 Excellent | Constant time |
| O(log n) | 🟢 Excellent | Logarithmic time |
| O(n) | 🟡 Good | Linear time |
| O(n log n) | 🟠 Fair | Linearithmic time |
| O(n²) | 🔴 Poor | Quadratic time |
| O(2ⁿ) | 🔴 Terrible | Exponential time |
| O(n!) | 🔴 Terrible | Factorial time |

#### Common Data Structure Operations

| Data Structure | Access | Search | Insert | Delete | Space |
|----------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | N/A | O(1) | O(1) | O(1) | O(n) |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

#### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Mergesort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |

**📂 Practical Examples**: `algorithms/big-o-examples/`

### 🚀 Getting Started

#### Prerequisites
- Python 3.8 or higher
- Git

#### Installation

```bash
# Clone the repository
git clone https://github.com/CemRoot/Algorithms_Data-Structures-and-LEETCODE.git

# Navigate to the directory
cd Algorithms_Data-Structures-and-LEETCODE

# Run a specific example (e.g., Linked List Append)
python data-structures/linked-list/singly-linked-list/SOLUTION-LL-Append.py
```

### 💡 Usage Examples

#### Singly Linked List

```python
# Import the LinkedList class
from linked_list import LinkedList

# Create a new linked list
my_list = LinkedList()

# Add elements
my_list.append(1)
my_list.append(2)
my_list.prepend(0)

# Access elements
node = my_list.get(1)  # Returns node at index 1

# Modify elements
my_list.set_value(1, 10)  # Sets value at index 1 to 10

# Remove elements
my_list.pop()  # Removes last element
my_list.remove(1)  # Removes element at index 1
```

### 🎯 Learning Path

1. **Start with Big-O Notation**: Understand time and space complexity
   - 📂 `algorithms/big-o-examples/`

2. **Master Data Structures**: Learn fundamental data structures
   - 📂 `data-structures/linked-list/`

3. **Practice Problems**: Apply your knowledge to real problems
   - 📂 Coming soon: LeetCode solutions

### 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 📚 Additional Resources

- **Big-O Cheat Sheet**: [bigocheatsheet.com](https://www.bigocheatsheet.com/)
- **LeetCode**: [leetcode.com](https://leetcode.com/)
- **Python Documentation**: [python.org](https://www.python.org/)

---

## <a id="turkish"></a>🇹🇷 Türkçe

### 📖 Genel Bakış

Bu depo, temel algoritmaların, veri yapılarının ve LeetCode problem çözümlerinin kapsamlı bir koleksiyonudur. Hem öğrenme hem de mülakat hazırlığı için tasarlanmış olup, detaylı karmaşıklık analizi ile birlikte açık ve iyi dokümante edilmiş uygulamalar sunar.

### ✨ Özellikler

- **Temiz Kod**: Adım adım açıklamalarla birlikte iyi yorumlanmış uygulamalar
- **Karmaşıklık Analizi**: Zaman ve alan karmaşıklığı için detaylı Big-O notasyonu
- **Pratik Örnekler**: Gerçek dünya kullanım senaryoları ve test durumları
- **Mülakat Hazırlığı**: Yaygın kodlama mülakat problemlerine çözümler
- **İki Dilli**: İngilizce ve Türkçe tam dokümantasyon

### 📁 Depo Yapısı

```
Algorithms_Data-Structures-and-LEETCODE/
│
├── data-structures/           # Veri yapısı uygulamaları
│   └── linked-list/
│       ├── singly-linked-list/    # Tek yönlü bağlı liste işlemleri
│       └── doubly-linked-list/    # Çift yönlü bağlı liste işlemleri
│
├── algorithms/                # Algoritma uygulamaları
│   └── big-o-examples/        # Zaman karmaşıklığı gösterimleri
│
└── docs/                      # Ek dokümantasyon ve notlar
```

### 🔗 Veri Yapıları

#### Tek Yönlü Bağlı Liste (Singly Linked List)
Aşağıdaki işlemlerle tam uygulama:

| İşlem | Açıklama | Zaman Karmaşıklığı |
|-------|----------|---------------------|
| `append(value)` | Sona düğüm ekle | O(1) |
| `prepend(value)` | Başa düğüm ekle | O(1) |
| `pop()` | Son düğümü çıkar | O(n) |
| `pop_first()` | İlk düğümü çıkar | O(1) |
| `get(index)` | İndekse göre düğüme eriş | O(n) |
| `set_value(index, value)` | Düğüm değerini güncelle | O(n) |
| `insert(index, value)` | Belirli indekse ekle | O(n) |
| `remove(index)` | Belirli indeksten çıkar | O(n) |
| `reverse()` | Listeyi ters çevir | O(n) |

**📂 Konum**: `data-structures/linked-list/singly-linked-list/`

#### Çift Yönlü Bağlı Liste (Doubly Linked List)
*(Geliştirilme Aşamasında)*

**📂 Konum**: `data-structures/linked-list/doubly-linked-list/`

### 📊 Big-O Karmaşıklık Referansı

> 💡 **Kaynak**: [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

#### Karmaşıklık Rehberi

| Notasyon | Performans | Açıklama |
|----------|------------|----------|
| O(1) | 🟢 Mükemmel | Sabit zaman |
| O(log n) | 🟢 Mükemmel | Logaritmik zaman |
| O(n) | 🟡 İyi | Doğrusal zaman |
| O(n log n) | 🟠 Orta | Doğrusal-logaritmik zaman |
| O(n²) | 🔴 Zayıf | Karesel zaman |
| O(2ⁿ) | 🔴 Korkunç | Üstel zaman |
| O(n!) | 🔴 Korkunç | Faktöriyel zaman |

#### Yaygın Veri Yapısı İşlemleri

| Veri Yapısı | Erişim | Arama | Ekleme | Silme | Alan |
|-------------|--------|-------|--------|-------|------|
| Dizi (Array) | O(1) | O(n) | O(n) | O(n) | O(n) |
| Bağlı Liste | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Tablosu | N/A | O(1) | O(1) | O(1) | O(n) |
| İkili Arama Ağacı | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| AVL Ağacı | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

#### Sıralama Algoritmaları

| Algoritma | En İyi | Ortalama | En Kötü | Alan | Kararlı |
|-----------|--------|----------|---------|------|---------|
| Hızlı Sıralama | O(n log n) | O(n log n) | O(n²) | O(log n) | Hayır |
| Birleştirme Sıralaması | O(n log n) | O(n log n) | O(n log n) | O(n) | Evet |
| Yığın Sıralaması | O(n log n) | O(n log n) | O(n log n) | O(1) | Hayır |
| Kabarcık Sıralaması | O(n) | O(n²) | O(n²) | O(1) | Evet |
| Ekleme Sıralaması | O(n) | O(n²) | O(n²) | O(1) | Evet |

**📂 Pratik Örnekler**: `algorithms/big-o-examples/`

### 🚀 Başlarken

#### Ön Gereksinimler
- Python 3.8 veya üzeri
- Git

#### Kurulum

```bash
# Depoyu klonlayın
git clone https://github.com/CemRoot/Algorithms_Data-Structures-and-LEETCODE.git

# Dizine gidin
cd Algorithms_Data-Structures-and-LEETCODE

# Belirli bir örneği çalıştırın (örn: Bağlı Liste Append)
python data-structures/linked-list/singly-linked-list/SOLUTION-LL-Append.py
```

### 💡 Kullanım Örnekleri

#### Tek Yönlü Bağlı Liste

```python
# LinkedList sınıfını içe aktarın
from linked_list import LinkedList

# Yeni bir bağlı liste oluşturun
my_list = LinkedList()

# Eleman ekleyin
my_list.append(1)
my_list.append(2)
my_list.prepend(0)

# Elemanlara erişin
node = my_list.get(1)  # İndeks 1'deki düğümü döndürür

# Elemanları değiştirin
my_list.set_value(1, 10)  # İndeks 1'deki değeri 10 yapar

# Eleman çıkarın
my_list.pop()  # Son elemanı çıkarır
my_list.remove(1)  # İndeks 1'deki elemanı çıkarır
```

### 🎯 Öğrenme Yolu

1. **Big-O Notasyonu ile Başlayın**: Zaman ve alan karmaşıklığını anlayın
   - 📂 `algorithms/big-o-examples/`

2. **Veri Yapılarında Ustalaşın**: Temel veri yapılarını öğrenin
   - 📂 `data-structures/linked-list/`

3. **Problem Pratiği Yapın**: Bilginizi gerçek problemlere uygulayın
   - 📂 Yakında: LeetCode çözümleri

### 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Depoyu fork edin
2. Özellik dalı oluşturun (`git checkout -b feature/HarikaOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika özellik eklendi'`)
4. Dalınıza push edin (`git push origin feature/HarikaOzellik`)
5. Pull Request açın

### 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

### 📚 Ek Kaynaklar

- **Big-O Cheat Sheet**: [bigocheatsheet.com](https://www.bigocheatsheet.com/)
- **LeetCode**: [leetcode.com](https://leetcode.com/)
- **Python Dokümantasyonu**: [python.org](https://www.python.org/)

---

<div align="center">

**Made with ❤️ for the Computer Science Community**

**Bilgisayar Bilimi Topluluğu için ❤️ ile Yapıldı**

</div>
