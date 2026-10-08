# NAYARA — Custom Bag Store

NAYARA is a responsive mini-project website for designing and ordering customized bags. Customers can select a bag type, choose colors and sizes, add personalized text or an image, preview the design, add items to the cart, and complete an order.

## Features

- Bag catalog with multiple categories
- Color and size selection
- Personalized text, font, and color options
- Logo or image upload
- Design placement controls
- Live bag preview
- Shopping cart
- Customer checkout form
- Floating AI assistant powered by Ollama

## Local AI Setup

The chatbot connects to Ollama running locally:

```text
http://localhost:11434/api/chat
```

The configured model is:

```text
llama3.2:latest
```

If the model is not installed, run:

```powershell
ollama pull llama3.2:latest
ollama serve
```

## Run the Website

From the project folder, run:

```powershell
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

## Project Files

- `index.html` — website structure
- `styles.css` — responsive visual design
- `script.js` — product selection, cart, checkout, and chatbot behavior
- `assets/logo.svg` — NAYARA logo
- `NAYARA_Project_Documentation.md` — project overview and implementation notes
- `NAYARA_Project_Presentation.pptx` — project presentation

## Notes

- The chatbot needs Ollama running on port `11434`.
- This project uses only static HTML, CSS, and JavaScript.
- No API key is required for the local Ollama connection.
