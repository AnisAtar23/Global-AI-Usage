# Global AI Students - Insights Portal

A premium, responsive, multi-page Flask web application analyzing the global adoption, usage, and growth of artificial intelligence in education. This repository integrates high-level summary metrics, key research findings, and interactive Tableau Public dashboards.

---
Website- https://global-ai-usage.vercel.app/

## 🌟 Key Features

* **Multi-Page Architecture**: Transitioned from a single-page template to dedicated pages for Home, Dashboard 1, Dashboard 2, and Story.
* **Interactive Data Insights Portal**: Home page gateway featuring custom-designed card teasers with smooth hover transitions linking to sub-visualizations.
* **Top Insights Grid (Dashboard 1)**: Visualizes key high-level statistics:
  * 🌐 **85+ Countries Surveyed**
  * 📈 **67% AI Usage Growth**
  * 🎓 **Top Tool: ChatGPT**
  * 🏢 **48% Institutional Support**
* **Key Findings Grid (Dashboard 2)**: Highlights 6 main analytical outcomes:
  1. 🚺 **Gender Gap in AI Adoption**
  2. 🔬 **STEM vs. Humanities Trajectories**
  3. 💸 **Income & Access Disparity**
  4. ⚡ **AI for Productivity Gains**
  5. ⚖️ **Rising Ethical & Policy Concerns**
  6. 🔮 **Future Academic Outlook (2027)**
* **Interactive Tableau Public Embeds**: Fully integrated, responsive dashboards and narrative stories loaded from Tableau Public.
* **Robust Error Handling**: Safeguarded scripts to resolve library loading errors (such as `PureCounter` reference crashes), ensuring smooth JS execution.

---

## 🛠️ Technology Stack

* **Backend**: Python, Flask
* **Frontend**: HTML5, Vanilla CSS, JavaScript
* **UI/UX Framework**: Bootstrap 5, Bootstrap Icons
* **Animations & Sliders**: AOS (Animate on Scroll), Swiper, GLightbox
* **Data Visualization**: Tableau Public (JS Embed API v1)

---

## 📂 File Structure

```text
├── Static/
│   ├── css/
│   │   └── main.css             # Main styling
│   ├── js/
│   │   └── main.js              # Custom scripts & initializers
│   ├── vendor/                  # Assets (Bootstrap, AOS, Swiper, etc.)
│   └── img/                     # Icons, backgrounds, and design assets
├── Template/
│   ├── index.html               # Gateway portal (Home page)
│   ├── dashboard1.html          # AI Adoption Analysis (Dashboard 1)
│   ├── dashboard2.html          # Usage & Growth Dashboard (Dashboard 2)
│   └── story.html               # Global Education AI Adoption Journey (Story)
├── app.py                       # Flask routes and server entry point
├── .gitignore                   # Excludes build caches and env configs
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher installed on your system.

### Installation & Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AnisAtar23/Global-AI-Usage.git
   cd Global-AI-Usage
   ```

2. **Install Flask**:
   ```bash
   pip install Flask
   ```

3. **Start the local server**:
   ```bash
   python app.py
   ```

4. **View the website**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 📊 Tableau Dashboards Configured

* **Dashboard 1**: `GlobalAIAdoption_17830633844480/Dashboard1`
* **Dashboard 2**: `GlobalEducationAndAIadoptionJourney/Dashboard2`
* **Story**: `GlobalEducationAndAIadoptionJourney/Story1`
