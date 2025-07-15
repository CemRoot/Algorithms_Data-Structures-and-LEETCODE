# My Algorithms, Data Structures & LeetCode Journey

This repository is dedicated to the study, implementation, and exploration of fundamental algorithms, data structures, and solutions to LeetCode problems. The primary goal is to serve as a comprehensive learning resource and a personal tracker of progress in mastering these crucial computer science concepts.

## 🌟 Why This Repository?

Understanding algorithms and data structures is paramount for any aspiring or established software engineer. They are the building blocks of efficient and scalable software. This repository aims to:

*   **Deepen Understanding:** Provide clear implementations and explanations.
*   **Track Progress:** Serve as a log of learned concepts and solved problems.
*   **Share Knowledge:** Offer a resource for others on a similar learning path.
*   **Prepare for Interviews:** Practice common problems asked in technical interviews.

## 📚 What's Inside?

This repository is organized to provide a structured approach to learning:

*   **Data Structures:** Implementations of common data structures with explanations of their operations, complexities, and use cases.
    *   **Singly Linked List:** A comprehensive implementation of a singly linked list in Python (found in `SOLUTION-LL-*.py` files). This includes detailed, commented code for the following operations:
        *   Constructor (`__init__`)
        *   Append to end (`append`)
        *   Prepend to beginning (`prepend`)
        *   Pop from end (`pop`)
        *   Pop from beginning (`pop_first`)
        *   Get node by index (`get`)
        *   Set value of node by index (`set_value`)
        *   Insert node at a specific index (`insert`)
        *   Remove node at a specific index (`remove`)
        *   Reverse the list in-place (`reverse`)
        *   Print all values in the list (`print_list`)
        *   Make the list empty (`make_empty`)
    These implementations, like `SOLUTION-LL-Append.py`, `SOLUTION-LL-Pop.py`, `SOLUTION-LL-Reverse.py`, etc., serve as excellent learning examples, with clear, teacher-like explanations of how each operation works step-by-step.
    *   Consider creating a `Data_Structures` directory and linking it here: `[Link to Data Structures Directory if applicable]`
*   **Algorithms:** Implementations of various algorithms categorized by type (e.g., Sorting, Searching, Graph Traversal, Dynamic Programming, Greedy Algorithms) with detailed explanations and complexity analysis.
    *   Consider creating an `Algorithms` directory and linking it here: `[Link to Algorithms Directory if applicable]`
*   **LeetCode Solutions:** Solutions to a curated list of LeetCode problems, categorized by difficulty and topic. Each solution aims to be well-commented and explained.
    *   Consider creating a `LeetCode_Solutions` directory and linking it here: `[Link to LeetCode Solutions Directory if applicable]`
*   **Notes & Explanations:** Theoretical notes, cheat sheets, and conceptual explanations related to algorithms and data structures (e.g., Big O notation examples like `O(1).py`, `O(n).py`, `O(n^2).py`).

## 📊 Big-O Complexity Reference

> **Reference:** [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

Understanding time and space complexity is crucial for algorithm analysis. Below are comprehensive tables showing the complexities of common data structures and algorithms.

### Complexity Chart Guide

| Complexity | Description | Color Code |
|------------|-------------|------------|
| **O(1)** | Excellent - Constant time | 🟢 |
| **O(log n)** | Excellent - Logarithmic time | 🟢 |
| **O(n)** | Good - Linear time | 🟡 |
| **O(n log n)** | Fair - Linearithmic time | 🟠 |
| **O(n²)** | Bad - Quadratic time | 🔴 |
| **O(2^n)** | Horrible - Exponential time | 🔴 |
| **O(n!)** | Horrible - Factorial time | 🔴 |

### Common Data Structure Operations

| Data Structure | Average Time Complexity ||||||| Worst Time Complexity ||||||| Space Complexity |
|----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|                | Access | Search | Insertion | Deletion | Access | Search | Insertion | Deletion | Worst |
| **Array** | Θ(1) | Θ(n) | Θ(n) | Θ(n) | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Stack** | Θ(n) | Θ(n) | Θ(1) | Θ(1) | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | Θ(n) | Θ(n) | Θ(1) | Θ(1) | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Singly-Linked List** | Θ(n) | Θ(n) | Θ(1) | Θ(1) | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Doubly-Linked List** | Θ(n) | Θ(n) | Θ(1) | Θ(1) | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Hash Table** | N/A | Θ(1) | Θ(1) | Θ(1) | N/A | O(n) | O(n) | O(n) | O(n) |
| **Binary Search Tree** | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | O(n) | O(n) | O(n) | O(n) | O(n) |
| **AVL Tree** | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **B-Tree** | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Red-Black Tree** | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

### Array Sorting Algorithms

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stable? |
|-----------|-----------|-------------|------------|------------------|---------|
| **Quicksort** | Ω(n log n) | Θ(n log n) | O(n²) | O(log n) | No |
| **Mergesort** | Ω(n log n) | Θ(n log n) | O(n log n) | O(n) | Yes |
| **Heapsort** | Ω(n log n) | Θ(n log n) | O(n log n) | O(1) | No |
| **Bubble Sort** | Ω(n) | Θ(n²) | O(n²) | O(1) | Yes |
| **Insertion Sort** | Ω(n) | Θ(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | Ω(n²) | Θ(n²) | O(n²) | O(1) | No |
| **Counting Sort** | Ω(n+k) | Θ(n+k) | O(n+k) | O(k) | Yes |
| **Radix Sort** | Ω(nk) | Θ(nk) | O(nk) | O(n+k) | Yes |

### Key Insights for Algorithm Analysis

1. **Linked Lists vs Arrays:**
   - **Access:** Arrays win with O(1), Lists need O(n)
   - **Insertion/Deletion:** Lists win with O(1) at head/tail, Arrays need O(n)
   - **Memory:** Lists use extra space for pointers

2. **When to Use Each Sorting Algorithm:**
   - **Quick Sort:** General purpose, good average performance
   - **Merge Sort:** When stability is needed and O(n log n) guarantee
   - **Heap Sort:** When constant space is critical
   - **Insertion Sort:** Small datasets or nearly sorted data
   - **Counting/Radix Sort:** When data range is limited

3. **Tree Structures:**
   - **BST:** Simple but can degrade to O(n) if unbalanced
   - **AVL/Red-Black:** Self-balancing, guaranteed O(log n)
   - **Hash Tables:** O(1) average but O(n) worst case

### Big-O Examples in This Repository

You can find practical examples of different time complexities in these files:
- `O(1).py` - Constant time operations
- `O(n).py` - Linear time algorithms  
- `O(n^2).py` - Quadratic time complexity
- `Drop+Const.py` - How constants are dropped in Big-O analysis
- `Different+Terms.py` - O(a + b) complexity analysis

## 🚀 Getting Started & How to Use

This repository can be used in several ways:

1.  **Learning Specific Concepts (e.g., Linked Lists):**
    *   Navigate to the relevant files (e.g., `SOLUTION-LL-Append.py`, `SOLUTION-LL-Get.py`).
    *   Review the source code. Most implementations will be in Python.
    *   Read the detailed comments within the code for explanations, step-by-step logic, complexity analysis (where applicable), and usage examples.

2.  **Solving LeetCode Problems:**
    *   Browse the `LeetCode_Solutions` directory (if you create one).
    *   Look for problems by name or category.
    *   Study the provided solution and try to understand the logic behind it. It's highly recommended to attempt the problem yourself before looking at the solution.

3.  **Running the Code (If Applicable):**
    *   **Prerequisites:** Ensure you have `Python 3.x` installed (as most examples are in Python).
    *   **Cloning the Repository:**
        ```bash
        git clone [URL of this Repository - YOU NEED TO FILL THIS IN AFTER CREATING THE GITHUB REPO]
        cd [Your Repository Directory Name]
        ```
    *   **Running a specific file (example for a Python linked list solution):**
        ```bash
        python SOLUTION-LL-Append.py
        ```
    *   *(Add more specific instructions if there's a common way to run tests or examples in your project)*

4.  **Contributing:**
    *   Contributions are welcome! Please see the "Contributing" section below. If you plan to have a more detailed contribution process, consider creating a `CONTRIBUTING.md` file.

## 🧑‍💻 Who is this for?

*   Students learning computer science fundamentals, especially data structures like linked lists.
*   Software developers looking to refresh their knowledge or learn new languages/paradigms through problem-solving.
*   Anyone preparing for technical interviews where data structures and algorithms are key.
*   Hobbyists interested in competitive programming or algorithmic challenges.

## 🛠️ Technologies & Tools Used (Example - Customize this!)

*   **Primary Language(s):** `Python 3.x`
*   **Testing Framework(s):** `[e.g., pytest for Python]` (if you use them)
*   **Development Environment:** `[e.g., VS Code with Python Extension]` (optional, for context)
*   **Version Control:** Git

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page]([Link to your repository's issues page - FILL THIS IN]) of this repository.
If you'd like to contribute, please:

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

Please make sure your code adheres to any styling guidelines used in the project and include tests if applicable.

## 📜 License

Distributed under the `[Choose a License, e.g., MIT, Apache 2.0, GPLv3]` License. Create a `LICENSE.txt` or `LICENSE` file in your repository with the chosen license text. See `[e.g., LICENSE.txt]` for more information.

---
---

# Benim Algoritmalar, Veri Yapıları & LeetCode Yolculuğum

Bu depo, temel algoritmaların, veri yapılarının ve LeetCode problemlerine yönelik çözümlerin incelenmesi, uygulanması ve keşfedilmesine adanmıştır. Temel amaç, bu kritik bilgisayar bilimi kavramlarında uzmanlaşmada kapsamlı bir öğrenme kaynağı ve kişisel bir ilerleme takipçisi olarak hizmet etmektir.

## 🌟 Neden Bu Depo?

Algoritmaları ve veri yapılarını anlamak, yazılım mühendisi olmak isteyen veya bu alanda çalışan herkes için büyük önem taşır. Bunlar, verimli ve ölçeklenebilir yazılımların temel yapı taşlarıdır. Bu depo şunları amaçlar:

*   **Anlayışı Derinleştirmek:** Açık uygulamalar ve açıklamalar sunmak.
*   **İlerlemeyi Takip Etmek:** Öğrenilen kavramların ve çözülen problemlerin bir kaydı olarak hizmet etmek.
*   **Bilgiyi Paylaşmak:** Benzer bir öğrenme yolunda olan başkalarına kaynak sunmak.
*   **Mülakatlara Hazırlanmak:** Teknik mülakatlarda sıkça sorulan problemleri pratik etmek.

## 📚 İçinde Neler Var?

Bu depo, öğrenmeye yapılandırılmış bir yaklaşım sunmak üzere organize edilmiştir:

*   **Veri Yapıları:** Yaygın veri yapılarının işlemleri, karmaşıklıkları ve kullanım durumlarına ilişkin açıklamalarla birlikte uygulamaları.
    *   **Tek Yönlü Bağlı Liste (Singly Linked List):** Python'da (`SOLUTION-LL-*.py` dosyaları) tek yönlü bağlı listenin kapsamlı bir uygulaması. Bu, aşağıdaki işlemler için detaylı, öğretmen üslubunda yorumlanmış kodları içerir:
        *   Yapıcı Metot (`__init__`)
        *   Sona Ekleme (`append`)
        *   Başa Ekleme (`prepend`)
        *   Sondan Çıkarma (`pop`)
        *   Baştan Çıkarma (`pop_first`)
        *   Indekse Göre Düğüm Alma (`get`)
        *   Indekse Göre Değer Ayarlama (`set_value`)
        *   Belirli Bir Indekse Düğüm Ekleme (`insert`)
        *   Belirli Bir Indeksten Düğüm Silme (`remove`)
        *   Listeyi Yerinde Ters Çevirme (`reverse`)
        *   Listedeki Tüm Değerleri Yazdırma (`print_list`)
        *   Listeyi Boşaltma (`make_empty`)
    `SOLUTION-LL-Append.py`, `SOLUTION-LL-Pop.py`, `SOLUTION-LL-Reverse.py` gibi bu uygulamalar, her bir işlemin adım adım nasıl çalıştığına dair net açıklamalarla mükemmel öğrenme örnekleri olarak hizmet eder.
    *   Bir `Veri_Yapilari` dizini oluşturmayı ve buraya bağlamayı düşünebilirsiniz: `[Veri Yapıları Dizini Bağlantısı - Varsa]`
*   **Algoritmalar:** Çeşitli algoritmaların türlerine göre (örneğin, Sıralama, Arama, Graf Gezinme, Dinamik Programlama, Açgözlü Algoritmalar) sınıflandırılmış, detaylı açıklamalar ve karmaşıklık analizleriyle birlikte uygulamaları.
    *   Bir `Algoritmalar` dizini oluşturmayı ve buraya bağlamayı düşünebilirsiniz: `[Algoritmalar Dizini Bağlantısı - Varsa]`
*   **LeetCode Çözümleri:** Seçilmiş LeetCode problemlerine yönelik, zorluk seviyesine ve konuya göre kategorize edilmiş çözümler. Her çözümün iyi yorumlanmış ve açıklanmış olması hedeflenir.
    *   Bir `LeetCode_Cozumleri` dizini oluşturmayı ve buraya bağlamayı düşünebilirsiniz: `[LeetCode Çözümleri Dizini Bağlantısı - Varsa]`
*   **Notlar & Açıklamalar:** Algoritmalar ve veri yapılarıyla ilgili teorik notlar, özet bilgiler (cheat sheets) ve kavramsal açıklamalar (örn: `O(1).py`, `O(n).py`, `O(n^2).py` gibi Big O notasyonu örnekleri).

## 📊 Big-O Karmaşıklık Referansı

> **Kaynak:** [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

Zaman ve alan karmaşıklığını anlamak algoritma analizi için çok önemlidir. Aşağıda yaygın veri yapıları ve algoritmaların karmaşıklıklarını gösteren kapsamlı tablolar bulunmaktadır.

### Karmaşıklık Tablosu Rehberi

| Karmaşıklık | Açıklama | Renk Kodu |
|-------------|----------|-----------|
| **O(1)** | Mükemmel - Sabit zaman | 🟢 |
| **O(log n)** | Mükemmel - Logaritmik zaman | 🟢 |
| **O(n)** | İyi - Doğrusal zaman | 🟡 |
| **O(n log n)** | Orta - Doğrusal-logaritmik zaman | 🟠 |
| **O(n²)** | Kötü - Karesel zaman | 🔴 |
| **O(2^n)** | Korkunç - Üstel zaman | 🔴 |
| **O(n!)** | Korkunç - Faktöriyel zaman | 🔴 |

### Yaygın Veri Yapısı İşlemleri

| Veri Yapısı | Ortalama Zaman Karmaşıklığı ||||||| En Kötü Zaman Karmaşıklığı ||||||| Alan Karmaşıklığı |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|             | Erişim | Arama | Ekleme | Silme | Erişim | Arama | Ekleme | Silme | En Kötü |
| **Dizi (Array)** | Θ(1) | Θ(n) | Θ(n) | Θ(n) | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Yığın (Stack)** | Θ(n) | Θ(n) | Θ(1) | Θ(1) | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Kuyruk (Queue)** | Θ(n) | Θ(n) | Θ(1) | Θ(1) | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Tek Yönlü Bağlı Liste** | Θ(n) | Θ(n) | Θ(1) | Θ(1) | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Çift Yönlü Bağlı Liste** | Θ(n) | Θ(n) | Θ(1) | Θ(1) | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Hash Tablosu** | N/A | Θ(1) | Θ(1) | Θ(1) | N/A | O(n) | O(n) | O(n) | O(n) |
| **İkili Arama Ağacı** | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | O(n) | O(n) | O(n) | O(n) | O(n) |
| **AVL Ağacı** | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **B-Ağacı** | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Kırmızı-Siyah Ağaç** | Θ(log n) | Θ(log n) | Θ(log n) | Θ(log n) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

### Dizi Sıralama Algoritmaları

| Algoritma | En İyi Zaman | Ortalama Zaman | En Kötü Zaman | Alan Karmaşıklığı | Kararlı? |
|-----------|-------------|---------------|---------------|------------------|----------|
| **Hızlı Sıralama (Quicksort)** | Ω(n log n) | Θ(n log n) | O(n²) | O(log n) | Hayır |
| **Birleştirme Sıralaması (Mergesort)** | Ω(n log n) | Θ(n log n) | O(n log n) | O(n) | Evet |
| **Yığın Sıralaması (Heapsort)** | Ω(n log n) | Θ(n log n) | O(n log n) | O(1) | Hayır |
| **Kabarcık Sıralaması (Bubble Sort)** | Ω(n) | Θ(n²) | O(n²) | O(1) | Evet |
| **Ekleme Sıralaması (Insertion Sort)** | Ω(n) | Θ(n²) | O(n²) | O(1) | Evet |
| **Seçim Sıralaması (Selection Sort)** | Ω(n²) | Θ(n²) | O(n²) | O(1) | Hayır |
| **Sayma Sıralaması (Counting Sort)** | Ω(n+k) | Θ(n+k) | O(n+k) | O(k) | Evet |
| **Radix Sıralama** | Ω(nk) | Θ(nk) | O(nk) | O(n+k) | Evet |

### Algoritma Analizi İçin Temel Bilgiler

1. **Bağlı Listeler vs Diziler:**
   - **Erişim:** Diziler O(1) ile kazanır, Listeler O(n) gerektirir
   - **Ekleme/Silme:** Listeler baş/kuyrukta O(1) ile kazanır, Diziler O(n) gerektirir
   - **Bellek:** Listeler işaretçiler için ekstra alan kullanır

2. **Hangi Sıralama Algoritması Ne Zaman Kullanılır:**
   - **Hızlı Sıralama:** Genel amaçlı, iyi ortalama performans
   - **Birleştirme Sıralaması:** Kararlılık gerektiğinde ve O(n log n) garantisi
   - **Yığın Sıralaması:** Sabit alan kritik olduğunda
   - **Ekleme Sıralaması:** Küçük veri setleri veya neredeyse sıralı veriler
   - **Sayma/Radix Sıralama:** Veri aralığı sınırlı olduğunda

3. **Ağaç Yapıları:**
   - **BST:** Basit ama dengelenmezse O(n)'e düşebilir
   - **AVL/Kırmızı-Siyah:** Kendi kendini dengeler, garantili O(log n)
   - **Hash Tabloları:** O(1) ortalama ama O(n) en kötü durum

### Bu Depodaki Big-O Örnekleri

Bu dosyalarda farklı zaman karmaşıklıklarının pratik örneklerini bulabilirsiniz:
- `O(1).py` - Sabit zamanlı işlemler
- `O(n).py` - Doğrusal zaman algoritmaları  
- `O(n^2).py` - Karesel zaman karmaşıklığı
- `Drop+Const.py` - Big-O analizinde sabitlerin nasıl atıldığı
- `Different+Terms.py` - O(a + b) karmaşıklık analizi

## 🚀 Başlarken & Nasıl Kullanılır?

Bu depo birkaç şekilde kullanılabilir:

1.  **Belirli Kavramları Öğrenmek (örn: Bağlı Listeler):**
    *   İlgili dosyalara gidin (örn: `SOLUTION-LL-Append.py`, `SOLUTION-LL-Get.py`).
    *   Kaynak kodunu inceleyin. Çoğu uygulama Python dilinde olacaktır.
    *   Adım adım mantığı, karmaşıklık analizini (varsa) ve kullanım örneklerini anlamak için koddaki detaylı yorumları okuyun.

2.  **LeetCode Problemlerini Çözmek:**
    *   `LeetCode_Cozumleri` dizinine göz atın (eğer oluşturursanız).
    *   Problemleri ada veya kategoriye göre arayın.
    *   Sunulan çözümü inceleyin ve arkasındaki mantığı anlamaya çalışın. Çözüme bakmadan önce problemi kendiniz çözmeye çalışmanız şiddetle tavsiye edilir.

3.  **Kodu Çalıştırmak (Eğer Uygulanabilirse):**
    *   **Önkoşullar:** Çoğu örnek Python'da olduğu için `Python 3.x`'in kurulu olduğundan emin olun.
    *   **Depoyu Klonlamak:**
        ```bash
        git clone [Bu Deponun URL'si - GITHUB DEPOSUNU OLUŞTURDUKTAN SONRA BUNU DOLDURMANIZ GEREKİR]
        cd [Deponuzun Dizin Adı]
        ```
    *   **Belirli bir dosyayı çalıştırmak (Python bağlı liste çözümü için örnek):**
        ```bash
        python SOLUTION-LL-Append.py
        ```
    *   *(Projenizde testleri veya örnekleri çalıştırmanın yaygın bir yolu varsa daha spesifik talimatlar ekleyin)*

4.  **Katkıda Bulunmak:**
    *   Katkılarınızı bekliyoruz! Lütfen aşağıdaki "Katkıda Bulunma" bölümüne bakın. Daha detaylı bir katkı süreci planlıyorsanız, bir `CONTRIBUTING.md` dosyası oluşturmayı düşünebilirsiniz.

## 🧑‍💻 Bu Kimin İçin?

*   Bilgisayar bilimi temellerini, özellikle bağlı listeler gibi veri yapılarını öğrenen öğrenciler.
*   Bilgilerini tazelemek veya problem çözme yoluyla yeni diller/paradigmalar öğrenmek isteyen yazılım geliştiriciler.
*   Veri yapıları ve algoritmaların kilit rol oynadığı teknik mülakatlara hazırlanan herkes.
*   Rekabetçi programlama veya algoritmik zorluklarla ilgilenen meraklılar.

## 🛠️ Kullanılan Teknolojiler & Araçlar (Örnek - Bunu Özelleştirin!)

*   **Ana Dil(ler):** `Python 3.x`
*   **Test Kütüphaneleri:** `[örn: Python için pytest]` (if you use them)
*   **Development Environment:** `[örn: VS Code with Python Extension]` (optional, for context)
*   **Version Control:** Git

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page]([Link to your repository's issues page - FILL THIS IN]) of this repository.
If you'd like to contribute, please:

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

Please make sure your code adheres to any styling guidelines used in the project and include tests if applicable.

## 📜 License

Distributed under the `[Choose a License, e.g., MIT, Apache 2.0, GPLv3]` License. Create a `LICENSE.txt` or `LICENSE` file in your repository with the chosen license text. See `[e.g., LICENSE.txt]` for more information.

---
---

# Algorithms, Data Structures, and LeetCode Practice

**Türkçe açıklamalar için [buraya](#turkce-aciklamalar) tıklayınız.**

## English Explanations

### 👋 Introduction
Welcome to the "Algorithms, Data Structures, and LeetCode Practice" repository! This project is dedicated to honing problem-solving skills, understanding fundamental computer science concepts, and preparing for technical interviews. Whether you're a beginner looking to learn the basics or an experienced developer aiming to refresh your knowledge, you'll find valuable resources and examples here.

### 🎯 Purpose of This Repository
The main goals of this repository are:
*   **Learn and Understand**: To provide clear, well-commented examples of common algorithms and data structures.
*   **Practice**: To offer a collection of solved LeetCode problems, demonstrating various approaches and techniques.
*   **Prepare**: To serve as a study guide for technical interviews at tech companies.
*   **Collaborate**: To create a space where developers can share insights, solutions, and learn from each other.

### 🌟 Why Are Algorithms and Data Structures Important?
Algorithms and data structures are the building blocks of software development.
*   **Efficiency**: Understanding them helps in writing code that is efficient in terms of time and space.
*   **Problem Solving**: They provide a structured way to think about and solve complex problems.
*   **Interview Standard**: Most tech companies assess candidates on their knowledge of these topics.
*   **Foundation**: They form the foundation upon which more complex systems and applications are built.

### 📁 What's Inside?
This repository is organized to provide a comprehensive learning experience:

1.  **Data Structures**:
    *   Implementations of fundamental data structures from scratch.
    *   Each data structure comes with detailed explanations and comments.
    *   **Singly Linked List**:
        *   `Node` Class: The basic building block.
        *   `LinkedList` Class: Manages the collection of nodes.
        *   Operations:
            *   `append(value)`: Adds a new node with the given value to the end of the list.
            *   `pop()`: Removes the last node from the list and returns it.
            *   `prepend(value)`: Adds a new node with the given value to the beginning of the list.
            *   `pop_first()`: Removes the first node from the list and returns it.
            *   `get(index)`: Retrieves the node at a specific index.
            *   `set_value(index, value)`: Updates the value of the node at a specific index.
            *   `insert(index, value)`: Inserts a new node with the given value at a specific index.
            *   `remove(index)`: Removes the node at a specific index and returns it.
            *   `reverse()`: Reverses the linked list in place.
        *   Examples include:
            *   `SOLUTION-LL-Append.py`
            *   `SOLUTION-LL-Pop.py`
            *   `SOLUTION-LL-Prepend.py`
            *   `SOLUTION-LL-Pop_First.py`
            *   `SOLUTION-LL-Get.py`
            *   `SOLUTION-LL-Set.py`
            *   `SOLUTION-LL-Insert.py`
            *   `SOLUTION-LL-Remove.py`
            *   `SOLUTION-LL-Reverse.py`
            *   `EXERCISE-LL-Constructor.py` (Constructor exercise)
            *   `LL-Print_List.py` (Utility to print the list)
    *   *(Coming Soon: Doubly Linked Lists, Stacks, Queues, Trees, Graphs, Hash Tables, etc.)*

2.  **Algorithms**:
    *   Implementations of common algorithms.
    *   Categorized by type (e.g., Sorting, Searching, Graph Algorithms).
    *   *(Coming Soon: Bubble Sort, Merge Sort, Quick Sort, Binary Search, BFS, DFS, etc.)*

3.  **LeetCode Solutions**:
    *   Solutions to a variety of LeetCode problems.
    *   Each solution includes an explanation of the thought process and complexity analysis.
    *   Categorized by difficulty and topic.
    *   *(Solutions will be added progressively.)*

4.  **Big O Notation**:
    *   Practical examples illustrating different time and space complexities.
    *   Understanding Big O is crucial for analyzing algorithm efficiency.
    *   Examples include:
        *   `O(1).py`: Constant time complexity.
        *   `O(n).py`: Linear time complexity.
        *   `O(n^2).py`: Quadratic time complexity.
        *   `Drop+Const.py`: Demonstrates dropping constants in Big O.
        *   `Non+Dom.py`: Demonstrates dropping non-dominant terms.
        *   `Different+Terms.py`: Illustrates Big O with different input terms.
        *   `Cookie.py`: A fun example (`O(log n)`) - *Note: Actual implementation might vary, this is conceptual.*

### 🚀 Getting Started
1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/Algorithms_Data-Structures_and_LeetCode.git
    cd Algorithms_Data-Structures_and_LeetCode
    ```
2.  **Explore Folders**: Navigate through the `Data Structures`, `Algorithms`, and `LeetCode Solutions` directories.
3.  **Run Python Files**: The examples are primarily in Python. You can run them directly:
    ```bash
    python path/to/your/file.py
    ```
    For instance, to run the linked list append example:
    ```bash
    python "Data Structures/Linked Lists/Singly Linked List/SOLUTION-LL-Append.py"
    ```
4.  **Read Explanations**: Each file and major code block is commented to help you understand the logic.

### 🎯 Target Audience
*   Computer Science students.
*   Aspiring software engineers preparing for interviews.
*   Developers looking to strengthen their foundational knowledge.
*   Anyone interested in learning about algorithms and data structures.

### 💻 Technologies Used
*   **Python**: The primary language for implementations due to its readability and ease of use.
*   **Markdown**: For documentation and `README` files.

### 🤝 Contribution Guidelines
Contributions are welcome! If you have suggestions, find a bug, or want to add new content:
1.  **Fork the Repository**.
2.  **Create a New Branch**: `git checkout -b feature/your-feature-name` or `bugfix/your-bug-fix`.
3.  **Make Your Changes**: Ensure your code is well-commented and follows the project's style.
4.  **Test Your Changes**: Make sure your additions work and don't break existing functionality.
5.  **Commit Your Changes**: `git commit -m "Add: Brief description of your feature"` or `Fix: Brief description of your fix`.
6.  **Push to Your Branch**: `git push origin feature/your-feature-name`.
7.  **Open a Pull Request**: Provide a clear description of your changes.

### 📜 License
This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## <a name="turkce-aciklamalar"></a>🇹🇷 Türkçe Açıklamalar

### 👋 Giriş
"Algoritmalar, Veri Yapıları ve LeetCode Pratikleri" reposuna hoş geldiniz! Bu proje, problem çözme becerilerini geliştirmek, temel bilgisayar bilimi kavramlarını anlamak ve teknik mülakatlara hazırlanmak için adanmıştır. İster temelleri öğrenmek isteyen bir başlangıç seviyesinde olun, ister bilgilerinizi tazelemek isteyen deneyimli bir geliştirici olun, burada değerli kaynaklar ve örnekler bulacaksınız.

### 🎯 Bu Reponun Amacı
Bu reponun temel amaçları şunlardır:
*   **Öğrenmek ve Anlamak**: Yaygın algoritmaların ve veri yapılarının açık, iyi yorumlanmış örneklerini sunmak.
*   **Pratik Yapmak**: Çeşitli yaklaşımları ve teknikleri gösteren çözülmüş LeetCode problemlerinden oluşan bir koleksiyon sunmak.
*   **Hazırlanmak**: Teknoloji şirketlerindeki teknik mülakatlar için bir çalışma rehberi olarak hizmet etmek.
*   **İşbirliği Yapmak**: Geliştiricilerin görüşlerini, çözümlerini paylaşabileceği ve birbirlerinden öğrenebileceği bir alan yaratmak.

### 🌟 Algoritmalar ve Veri Yapıları Neden Önemlidir?
Algoritmalar ve veri yapıları, yazılım geliştirmenin temel taşlarıdır.
*   **Verimlilik**: Onları anlamak, zaman ve alan açısından verimli kod yazmaya yardımcı olur.
*   **Problem Çözme**: Karmaşık problemler hakkında düşünmek ve bunları çözmek için yapılandırılmış bir yol sunarlar.
*   **Mülakat Standardı**: Çoğu teknoloji şirketi, adayları bu konulardaki bilgilerine göre değerlendirir.
*   **Temel**: Daha karmaşık sistemlerin ve uygulamaların üzerine inşa edildiği temeli oluştururlar.

### 📁 İçinde Neler Var?
Bu repo, kapsamlı bir öğrenme deneyimi sunmak üzere düzenlenmiştir:

1.  **Veri Yapıları**:
    *   Temel veri yapılarının sıfırdan uygulamaları.
    *   Her veri yapısı, ayrıntılı açıklamalar ve yorumlarla birlikte gelir.
    *   **Tek Yönlü Bağlı Liste (Singly Linked List)**:
        *   `Node` Sınıfı: Temel yapı taşı.
        *   `LinkedList` Sınıfı: Düğüm koleksiyonunu yönetir.
        *   İşlemler:
            *   `append(value)`: Listenin sonuna verilen değere sahip yeni bir düğüm ekler.
            *   `pop()`: Listenin son düğümünü kaldırır ve döndürür.
            *   `prepend(value)`: Listenin başına verilen değere sahip yeni bir düğüm ekler.
            *   `pop_first()`: Listenin ilk düğümünü kaldırır ve döndürür.
            *   `get(index)`: Belirli bir indisteki düğümü getirir.
            *   `set_value(index, value)`: Belirli bir indisteki düğümün değerini günceller.
            *   `insert(index, value)`: Belirli bir indise verilen değere sahip yeni bir düğüm ekler.
            *   `remove(index)`: Belirli bir indisteki düğümü kaldırır ve döndürür.
            *   `reverse()`: Bağlı listeyi yerinde ters çevirir.
        *   Örnekler şunları içerir:
            *   `SOLUTION-LL-Append.py`
            *   `SOLUTION-LL-Pop.py`
            *   `SOLUTION-LL-Prepend.py`
            *   `SOLUTION-LL-Pop_First.py`
            *   `SOLUTION-LL-Get.py`
            *   `SOLUTION-LL-Set.py`
            *   `SOLUTION-LL-Insert.py`
            *   `SOLUTION-LL-Remove.py`
            *   `SOLUTION-LL-Reverse.py`
            *   `EXERCISE-LL-Constructor.py` (Yapıcı metot alıştırması)
            *   `LL-Print_List.py` (Listeyi yazdırma yardımcı programı)
    *   *(Çok Yakında: Çift Yönlü Bağlı Listeler, Yığınlar, Kuyruklar, Ağaçlar, Graflar, Karma Tablolar vb.)*

2.  **Algoritmalar**:
    *   Yaygın algoritmaların uygulamaları.
    *   Türe göre kategorize edilmiştir (örn: Sıralama, Arama, Graf Algoritmaları).
    *   *(Çok Yakında: Kabarcık Sıralaması, Birleştirme Sıralaması, Hızlı Sıralama, İkili Arama, BFS, DFS vb.)*

3.  **LeetCode Çözümleri**:
    *   Çeşitli LeetCode problemlerine çözümler.
    *   Her çözüm, düşünce sürecinin bir açıklamasını ve karmaşıklık analizini içerir.
    *   Zorluk ve konuya göre kategorize edilmiştir.
    *   *(Çözümler aşamalı olarak eklenecektir.)*

4.  **Big O Notasyonu**:
    *   Farklı zaman ve alan karmaşıklıklarını gösteren pratik örnekler.
    *   Big O'yu anlamak, algoritma verimliliğini analiz etmek için çok önemlidir.
    *   Örnekler şunları içerir:
        *   `O(1).py`: Sabit zaman karmaşıklığı.
        *   `O(n).py`: Doğrusal zaman karmaşıklığı.
        *   `O(n^2).py`: Karesel zaman karmaşıklığı.
        *   `Drop+Const.py`: Big O'da sabitlerin atılmasını gösterir.
        *   `Non+Dom.py`: Baskın olmayan terimlerin atılmasını gösterir.
        *   `Different+Terms.py`: Farklı girdi terimleriyle Big O'yu gösterir.
        *   `Cookie.py`: Eğlenceli bir örnek (`O(log n)`) - *Not: Gerçek uygulama farklılık gösterebilir, bu kavramsal bir örnektir.*

### 🚀 Başlarken
1.  **Repoyu Klonlayın**:
    ```bash
    git clone https://github.com/kullanici-adiniz/Algorithms_Data-Structures_and_LeetCode.git
    cd Algorithms_Data-Structures_and_LeetCode
    ```
2.  **Klasörleri Keşfedin**: `Veri Yapıları`, `Algoritmalar` ve `LeetCode Çözümleri` dizinlerinde gezinin.
3.  **Python Dosyalarını Çalıştırın**: Örnekler öncelikle Python dilindedir. Doğrudan çalıştırabilirsiniz:
    ```bash
    python path/to/your/file.py
    ```
    Örneğin, bağlı liste `append` örneğini çalıştırmak için:
    ```bash
    python "Data Structures/Linked Lists/Singly Linked List/SOLUTION-LL-Append.py"
    ```
4.  **Açıklamaları Okuyun**: Her dosya ve ana kod bloğu, mantığı anlamanıza yardımcı olmak için yorumlanmıştır.

### 🎯 Hedef Kitle
*   Bilgisayar Bilimi öğrencileri.
*   Mülakatlara hazırlanan yazılım mühendisi adayları.
*   Temel bilgilerini güçlendirmek isteyen geliştiriciler.
*   Algoritmalar ve veri yapıları hakkında bilgi edinmek isteyen herkes.

### 💻 Kullanılan Teknolojiler
*   **Python**: Okunabilirliği ve kullanım kolaylığı nedeniyle uygulamalar için birincil dil.
*   **Markdown**: Dokümantasyon ve `README` dosyaları için.

### 🤝 Katkıda Bulunma Yönergeleri
Katkılarınızı bekliyoruz! Önerileriniz varsa, bir hata bulursanız veya yeni içerik eklemek isterseniz:
1.  **Repoyu Forklayın (Fork the Repository)**.
2.  **Yeni Bir Dal Oluşturun (Create a New Branch)**: `git checkout -b feature/ozellik-adiniz` veya `bugfix/hata-duzeltmeniz`.
3.  **Değişikliklerinizi Yapın (Make Your Changes)**: Kodunuzun iyi yorumlandığından ve projenin stiline uyduğundan emin olun.
4.  **Değişikliklerinizi Test Edin (Test Your Changes)**: Eklemelerinizin çalıştığından ve mevcut işlevselliği bozmadığından emin olun.
5.  **Değişikliklerinizi Commit Edin (Commit Your Changes)**: `git commit -m "Ekle: Özelliğinizin kısa açıklaması"` veya `Düzelt: Düzeltmenizin kısa açıklaması`.
6.  **Dalınıza Push Edin (Push to Your Branch)**: `git push origin feature/ozellik-adiniz`.
7.  **Bir Pull Request Açın (Open a Pull Request)**: Değişikliklerinizin net bir açıklamasını yapın.

### 📜 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - ayrıntılar için `LICENSE` dosyasına bakın. 