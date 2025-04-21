# 💌 AI-Powered Gmail Draft Generator with Gemini ✨  
> Auto-write emails like a pro — Powered by Google Gemini + Gmail API  

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)  
[![Google Gemini](https://img.shields.io/badge/AI-Gemini-brightgreen)](https://ai.google.dev/)  
[![Gmail API](https://img.shields.io/badge/API-Gmail-red)](https://developers.google.com/gmail/api)  


---

## 🚀 What This Does

This magical Python script helps you:

✅ Auto-generate professional emails using Google Gemini  
✅ Save those emails directly as **drafts** in your Gmail  
✅ Review & send the email from terminal  
✅ Impress people (without actually writing much) 😎

---

## 🧠 How It Works

1. You enter a recipient email + a topic  
2. Gemini generates a *subject line* and *body*  
3. You preview and choose to save/send the email  
4. Gmail API saves it as a draft or sends it on command  

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/himanshupardhi14/AI-Powered-Gmail-Draft-Generator-with-Gemini-
cd AI-Powered-Gmail-Draft-Generator-with-Gemini-
```
### 2. Add Secrets
Create a .env file and paste your Gemini API key:
GEMINI_API_KEY=your-gemini-api-key

### ▶️ Run It!
```bash
python main.py
```
## 🧬 Example Output
```bash
Enter recipient email: ceo@company.com
Enter the topic: Quarterly Performance Update

Generated Email Preview:
Subject: Q1 Performance Overview & Insights
Body:
Hi there,
I hope this email finds you well. Here's a brief overview...

```
You'll then be asked:
✅ "Send this email now?"
or
💾 "Save as draft?"
## 📁 Project Structure
```bash
📦 AI-Powered-Gmail-Draft-Generator-with-Gemini-
├── main.py             # Main script
├── .env                # Stores GEMINI_API_KEY
├── credentials.json    # Gmail OAuth2 credentials
├── token.pickle        # Stores session token (auto-generated)
├── requirements.txt    # Dependencies

```
## 📜 Requirements
```bash
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
google-generativeai
python-dotenv
```
## 🙏 Big Thanks & Credits

💡 **Powered by awesome tech:**

- 🔮 [**Google Gemini API**](https://ai.google.dev)  
  For generating professional and contextual email content using cutting-edge generative AI.

- 📬 [**Gmail API Docs**](https://developers.google.com/gmail/api)  
  For providing the tools to create, save, and send emails directly from Python.

Made possible with the magic of AI ✨ and open web APIs ❤️


