# 🏎️ NEXUS-9 Quantum Hypercars: Enterprise Web Application

Welcome to the **NEXUS-9 Enterprise Hypercars** source code! This is a premium, fully-functional, futuristic 3D car dealership web application built with modern web technologies. 

It features an interactive 3D chassis inspector, a Python-powered backend, a secure admin dashboard, and a stunning cyberpunk-inspired UI.

---

## ✨ Key Features

*   **Interactive 3D Chassis Inspector:** Built with Three.js. Users can rotate (360°), zoom, and dynamically change the car's high-gloss metallic paint.
*   **Holographic HUD & Gamified UI:** Live speedometer, G-force telemetry simulation, and smooth GSAP animations.
*   **Audio Engine Simulator:** Synthetic Web Audio API generates a dynamic V12/EV engine rev sound on command.
*   **12-Car Digital Fleet:** Pre-configured catalog featuring high-resolution imagery and detailed futuristic specs.
*   **Secure Admin Command Center:** Password-protected dashboard to track live reservations, view total revenue, and search order history.
*   **Full Stack Integration:** A robust Python/FastAPI backend seamlessly connected to a modern HTML5/Vanilla JS frontend via an SQLite database.
*   **Continuous Motion Background:** A high-speed, looping 3D tunnel and starfield effect using WebGL.

---

## 🛠️ Technology Stack

*   **Frontend:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript
*   **3D Graphics & Animation:** Three.js (WebGL), GSAP (GreenSock Animation Platform)
*   **Backend API:** Python 3.x, FastAPI, Uvicorn
*   **Database:** SQLite, SQLAlchemy, Pydantic (for data validation)

---

## 🚀 Quick Start Guide

Follow these steps to get the NEXUS-9 application running on your local machine.

### Prerequisites
*   Python 3.10+ installed on your system.
*   Git (optional, but recommended).

### Installation Steps

1.  **Extract the Archive:** Unzip the downloaded `nexus9-hypercars.zip` file.
2.  **Open Terminal:** Navigate to the extracted `nexus9-hypercars/backend` directory using your terminal or command prompt.
3.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv
    ```
4.  **Activate the Virtual Environment:**
    *   **Windows:** `.venv\Scripts\activate`
    *   **macOS/Linux:** `source .venv/bin/activate`
5.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
6.  **Run the Server:**
    ```bash
    uvicorn main:app --reload
    ```

### Accessing the Application

*   **Main Website:** Open your web browser and navigate to `http://127.0.0.1:8000/`.
*   **API Documentation (Swagger UI):** To view and test the backend APIs, navigate to `http://127.0.0.1:8000/docs`.

---

## 🔒 Admin Dashboard Access

To access the "Admin Track Order" section, use the following default credentials:
*   **Username:** `manish`
*   **Password:** `manishking`

*(You can modify these credentials directly within the JavaScript logic in `frontend/index.html`).*

---

## 📝 Customization

This template is designed to be easily customizable:
*   **Modify the Car Catalog:** Edit the `CARS` list in `backend/main.py` to add your own vehicles, prices, and images.
*   **Tweak 3D Models:** The procedural 3D model generation logic is located in `frontend/index.html` within the `init3DViewer()` function.
*   **Style Adjustments:** All CSS variables (colors, fonts, glass effects) are clearly defined in the `:root` pseudo-class at the top of the CSS block in `frontend/index.html`.

---

## 📞 Support 7814398117

If you encounter any issues or have questions regarding the setup, please reach out via the platform where you purchased this template.

*Enjoy building the future of web experiences!*