# 🧠 EDW-2: Honeywell EDW Reasoning Assistant (Alpha)

This is the **alpha version** of the **Honeywell Enterprise Data Warehouse (EDW) Reasoning Assistant**, powered by the **Groq LLM API**.  
It enables natural-language reasoning over structured evidence and generates concise analytical summaries.

---

## 🚀 Features
- Integrates with **Groq Llama 3.3 70B Versatile** model  
- Works directly in **Google Colab** — no local setup required  
- Designed for **root-cause analysis** and **evidence synthesis**  
- Uses **FastAPI** for modular API endpoints  
- Compatible with **Ngrok** for secure local tunneling  
- Supports **Streamlit** for simple UI visualization  

---

## ⚙️ Requirements

| Dependency | Version / Notes |
|-------------|-----------------|
| **Python** | 3.12.5 |
| **FastAPI** | Web framework for serving the API |
| **Uvicorn** | ASGI server for FastAPI |
| **Pydantic** | Data validation and serialization |
| **Pandas** | Data manipulation |
| **Requests** | For HTTP requests |
| **Groq** | Access to Groq LLM API |
| **Streamlit** | For interactive UI |
| **Ngrok** | For public URL tunneling |
| **Groq API Key** | Required for LLM access |

---

## 🧩 Installation & Setup

1. **Run in Google Colab**

   Simply open this project in **Google Colab** and execute the setup cells below:

   ```bash
   !pip install fastapi uvicorn pydantic pandas requests groq streamlit pyngrok
