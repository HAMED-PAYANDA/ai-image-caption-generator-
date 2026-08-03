# 🖼️ Give Meaningful Names to Your Photos with Image Captioning AI

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers-yellow.svg)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.2.1-red.svg)
![IBM](https://img.shields.io/badge/IBM-CognitiveClass.ai-052FAD.svg)

## 📌 Overview
Images are rich with untapped visual information, but search engines and data systems cannot inherently "see" them. This project leverages state-of-the-art **Generative AI** and **Vision-Language Pre-training** to automatically translate visual data into machine-readable and human-readable text descriptions. 

Developed as part of the **IBM AI Developer Series**, this tool replaces generic filenames (like `image09321.jpeg`) with meaningful captions, streamlining data organization, boosting accessibility, and enhancing visual content searchability.

---

## 🏢 Real-World Business Application: News & Media
In a fast-paced news agency, publishing hundreds of articles daily requires handling thousands of images. Manually writing descriptive captions for every image is tedious and slows down publication. 

This AI tool expedites the pipeline by automatically generating suggested captions for bulk images, serving two critical purposes:
1. ♿ **Enhanced Accessibility:** Captions are integrated as alternative text (alt text). Visually impaired users utilizing screen readers can fully understand the visual context, adhering to inclusive design principles.
2. 🔍 **Improved SEO:** Search engines like Google rely on alt text for indexing. Properly captioned images with relevant keywords drastically improve the article's search engine ranking and drive organic traffic.

---

## 🚀 Key Features

* **Interactive Web Application:** A user-friendly GUI built with **Gradio** that allows users to upload images and receive instant AI-generated captions.
* **Automated Web Scraper:** Uses **BeautifulSoup** to parse HTML content from any given webpage URL, extracts all valid image tags (`<img>`), downloads the images synchronously, and generates bulk captions.
* **Batch Processing:** Processes multiple local images in a directory using Python's `glob` module.
* **Scalable AI:** Built on the `Salesforce/blip-image-captioning-base` model with the flexibility to upgrade to heavier, more powerful models like **BLIP-2** for local execution.

---

## 🛠️ Architecture & Tech Stack

* **Language:** Python
* **Vision-Language Model:** Hugging Face `Transformers` (`AutoProcessor`, `BlipForConditionalGeneration`)
* **Web Scraping:** `BeautifulSoup4`, `requests`
* **User Interface:** `Gradio`
* **Data Processing:** `Pillow` (PIL), `NumPy`, `PyTorch` (`torch`)

---

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| `image_captioning_app.py` | The main **Gradio** web application for interactive image captioning. |
| `automate_url_captioner.py` | Web scraping script that parses a URL, downloads images, and outputs captions to a text file. |
| `image_cap.py` | Core backend script for processing individual local image files. |
| `captions.txt` | The automated output file storing generated image URLs and their respective descriptions. |
| `requirements.txt` | Dependency file listing exact library versions. |

---

## 💻 Installation & Setup

**1. Clone the Repository:**
```bash
git clone [https://github.com/HAMED-PAYANDA/ai-image-caption-generator-.git](https://github.com/HAMED-PAYANDA/ai-image-caption-generator-.git)
cd ai-image-caption-generator-

2. Create a Virtual Environment:
python3 -m venv my_env
source my_env/bin/activate  # On Windows: my_env\Scripts\activate

3. Install Dependencies:
pip install -r requirements.txt
