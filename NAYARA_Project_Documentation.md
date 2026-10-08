# NAYARA Project Documentation

## 1. Project Overview

NAYARA is a college mini-project website for selling and customizing bags. The website allows customers to browse bag types, personalize them, preview the result, and place an order.

## 2. Objectives

- Provide an attractive, responsive online shopping experience.
- Let customers select a bag type, color, and size.
- Allow custom text, fonts, colors, and image uploads.
- Show a live preview before adding an item to the cart.
- Support cart management and order details.
- Add an AI assistant powered by a local Ollama model.

## 3. Technologies Used

- HTML5
- CSS3
- JavaScript
- Ollama API
- Python HTTP server for local preview

## 4. Project Structure

```text
NAYARA/
├── index.html
├── styles.css
├── script.js
├── README.md
├── NAYARA_Project_Documentation.md
├── NAYARA_Project_Presentation.pptx
└── assets/
    └── logo.svg
```

## 5. Features

### Storefront

The homepage contains a hero section, product collection, customization area, customer benefits, and footer-style brand section.

### Customization

Customers can choose:

- Bag type
- Color
- Size
- Name or text
- Font style
- Text color
- Logo or image
- Design placement
- Additional notes

### Live Preview

The customization panel updates the bag preview in real time as users change the options.

### Cart and Checkout

Users can add customized items to a cart, remove them, view the subtotal, and enter their customer details in the checkout form.

### NAYARA AI Assistant

The chatbot uses the Ollama API endpoint:

```text
http://localhost:11434/api/chat
```

The configured model is:

```text
llama3.2:latest
```

The assistant delivers concise answers in bullet or numbered points when users request recommendations, steps, comparisons, or multiple details.

## 6. Local Setup

1. Install and start Ollama.
2. Pull the required model:

```powershell
ollama pull llama3.2:latest
```

3. Start Ollama:

```powershell
ollama serve
```

4. Start the website:

```powershell
python -m http.server 8000
```

5. Open:

```text
http://localhost:8000/
```

## 7. Important Requirements

- Keep Ollama running while using the chatbot.
- Do not expose the local Ollama endpoint to the public internet.
- The local model must be installed before sending chatbot requests.
- The browser must allow local HTTP requests to `localhost:11434`.

## 8. Future Improvements

- Add product images and detailed product pages.
- Connect the checkout form to a real database and payment gateway.
- Add user accounts and saved designs.
- Add multilingual chatbot support.
- Add image generation and product recommendation features.
- Add order history and admin management.
