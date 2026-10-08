const products = [
  { id: "tote", name: "Signature Tote", price: 2499, color: "#f4d7c6", description: "Perfect for work, travel, and everyday essentials.", badge: "Best seller" },
  { id: "handbag", name: "Velvet Handbag", price: 3499, color: "#d8c3ee", description: "A compact statement bag with a polished finish.", badge: "New" },
  { id: "backpack", name: "Terrain Backpack", price: 4299, color: "#bfe0d0", description: "Spacious, comfortable, and ready for every journey.", badge: "Popular" },
  { id: "laptop", name: "Metro Laptop", price: 5299, color: "#e4d0af", description: "Protective storage with a clean, professional look.", badge: "Tech" }
];

const state = {
  selectedProduct: products[0],
  color: "#f4d7c6",
  size: "Medium",
  placement: "center",
  text: "NAYARA",
  textColor: "#ffffff",
  font: "Playfair Display",
  notes: "",
  image: null,
  cart: []
};

const productGrid = document.querySelector("#productGrid");
const bagType = document.querySelector("#bagType");
const bagColor = document.querySelector("#bagColor");
const bagSize = document.querySelector("#bagSize");
const nameInput = document.querySelector("#nameInput");
const fontStyle = document.querySelector("#fontStyle");
const textColor = document.querySelector("#textColor");
const logoUpload = document.querySelector("#logoUpload");
const bagNotes = document.querySelector("#bagNotes");
const designText = document.querySelector("#designText");
const designImage = document.querySelector("#designImage");
const selectedBagName = document.querySelector("#selectedBagName");
const previewPrice = document.querySelector("#previewPrice");
const previewSize = document.querySelector("#previewSize");
const bagPreview = document.querySelector("#bagPreview");
const cartDrawer = document.querySelector("#cartDrawer");
const cartItems = document.querySelector("#cartItems");
const cartSubtotal = document.querySelector("#cartSubtotal");
const cartCount = document.querySelector(".cart-count");
const checkoutModal = document.querySelector("#checkoutModal");
const toast = document.querySelector("#toast");
const checkoutForm = document.querySelector("#checkoutForm");
const chatToggle = document.querySelector("#chatToggle");
const chatPanel = document.querySelector("#chatPanel");
const chatClose = document.querySelector("#chatClose");
const chatForm = document.querySelector("#chatForm");
const chatInput = document.querySelector("#chatInput");
const chatMessages = document.querySelector("#chatMessages");
const chatStatus = document.querySelector("#chatStatus");
const chatSend = chatForm.querySelector(".chat-send");

function formatPrice(value) {
  return new Intl.NumberFormat("en-IN", { style: "currency", currency: "INR", maximumFractionDigits: 0 }).format(value);
}

function appendMessage(content, role = "bot") {
  const wrapper = document.createElement("div");
  wrapper.className = `message ${role}`;
  const paragraph = document.createElement("p");
  paragraph.textContent = content;
  wrapper.appendChild(paragraph);
  chatMessages.appendChild(wrapper);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTyping() {
  const wrapper = document.createElement("div");
  wrapper.className = "message bot typing-message";
  wrapper.setAttribute("aria-label", "Assistant is typing");
  wrapper.innerHTML = '<span class="typing"></span><span class="typing"></span><span class="typing"></span>';
  chatMessages.appendChild(wrapper);
  chatMessages.scrollTop = chatMessages.scrollHeight;
  return wrapper;
}

function setChatStatus(message, isError = false) {
  chatStatus.textContent = message;
  chatStatus.style.color = isError ? "#d65757" : "#6a6d7a";
}

async function sendChatMessage(message) {
  const response = await fetch("http://localhost:11434/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "llama3.2:latest",
      messages: [
        {
          role: "system",
          content: "You are NAYARA's helpful bag shopping assistant. Answer in a friendly, concise style. Use bullet points or numbered lists whenever the user asks for recommendations, comparisons, steps, options, or multiple details. Keep ordinary conversations short and natural."
        },
        { role: "user", content: message }
      ],
      stream: false,
      options: { temperature: 0.7 }
    })
  });

  if (!response.ok) {
    throw new Error(`Ollama returned ${response.status}`);
  }

  const data = await response.json();
  return data.message?.content?.trim() || "Sorry, I could not generate a response.";
}

async function checkChatAvailability() {
  try {
    const response = await fetch("http://localhost:11434/api/tags");
    if (!response.ok) {
      throw new Error(`Ollama returned ${response.status}`);
    }
    const data = await response.json();
    const hasModel = data.models?.some((model) => model.name === "llama3.2:latest");
    setChatStatus(hasModel ? "Local AI ready" : "llama3.2:latest not installed");
    return hasModel;
  } catch (error) {
    setChatStatus("Local AI unavailable", true);
    return false;
  }
}

function renderProducts() {
  productGrid.innerHTML = products.map((product) => `
    <article class="product-card">
      <div class="product-visual" style="--bag-color:${product.color};">
        <div class="mini-bag" aria-hidden="true"></div>
      </div>
      <div class="product-copy">
        <div class="product-top">
          <h3 class="product-title">${product.name}</h3>
          <span class="product-price">${formatPrice(product.price)}</span>
        </div>
        <p>${product.description}</p>
        <button class="select-product" type="button" data-product="${product.id}">Select ${product.name}</button>
      </div>
    </article>
  `).join("");

  productGrid.querySelectorAll(".select-product").forEach((button) => {
    button.addEventListener("click", () => selectProduct(button.dataset.product));
  });
}

function renderBagTypes() {
  bagType.innerHTML = products.map((product) => `
    <div class="option">
      <input type="radio" name="bagType" id="bag-${product.id}" value="${product.id}" ${product.id === state.selectedProduct.id ? "checked" : ""}>
      <label for="bag-${product.id}">${product.name}</label>
    </div>
  `).join("");

  bagType.querySelectorAll("input").forEach((input) => {
    input.addEventListener("change", () => selectProduct(input.value));
  });
}

function selectProduct(productId) {
  const product = products.find((item) => item.id === productId);
  if (!product) return;
  state.selectedProduct = product;
  state.color = product.color;
  bagColor.value = product.color;
  selectedBagName.textContent = product.name;
  previewPrice.textContent = formatPrice(product.price);
  renderBagTypes();
  updatePreview();
}

function updatePreview() {
  bagPreview.style.setProperty("--bag-color", state.color);
  designText.textContent = state.text.trim() || "NAYARA";
  designText.style.color = state.textColor;
  designText.style.fontFamily = state.font;
  designText.style.fontStyle = state.font === "Playfair Display" || state.font === "Georgia" ? "normal" : "normal";
  designText.style.letterSpacing = state.font === "Manrope" ? "0.04em" : ".05em";
  designText.style.textTransform = state.font === "Manrope" ? "none" : "uppercase";
  designText.style.display = state.text.trim() ? "block" : "none";
  designImage.hidden = !state.image;
  if (state.image) {
    designImage.src = state.image;
    designImage.alt = "Custom design";
  }
  selectedBagName.textContent = state.selectedProduct.name;
  previewPrice.textContent = formatPrice(state.selectedProduct.price);
  previewSize.textContent = state.size;
  updatePlacement();
}

function updatePlacement() {
  const art = document.querySelector("#designArea");
  art.style.inset = state.placement === "center" ? "30% 22% 22%" : state.placement === "front" ? "26% 20% 18%" : "38% 20% 12%";
  art.style.border = state.placement === "center" ? "2px solid rgba(255,255,255,.18)" : "2px solid rgba(255,255,255,.12)";
  art.style.background = state.placement === "side" ? "rgba(255,255,255,.06)" : "transparent";
  art.style.borderRadius = state.placement === "side" ? "12px" : "18px";
}

function addToCart() {
  const item = {
    id: crypto.randomUUID(),
    name: state.selectedProduct.name,
    price: state.selectedProduct.price,
    color: state.color,
    size: state.size,
    text: state.text.trim() || "NAYARA",
    notes: state.notes.trim(),
    placement: state.placement,
    image: state.image,
    initials: (state.text.trim() || "NAYARA").slice(0, 2).toUpperCase()
  };

  state.cart.push(item);
  renderCart();
  cartDrawer.classList.add("open");
  cartDrawer.setAttribute("aria-hidden", "false");
  showToast(`${item.name} added to cart`);
}

function renderCart() {
  if (!state.cart.length) {
    cartItems.innerHTML = '<div class="empty-state"><p>Your cart is empty.</p><p>Customize a bag to get started.</p></div>';
    cartSubtotal.textContent = formatPrice(0);
    cartCount.textContent = "0";
    return;
  }

  cartItems.innerHTML = state.cart.map((item) => `
    <article class="cart-item">
      <div class="cart-bag" style="--bag-color:${item.color};" data-initials="${item.initials}"></div>
      <div>
        <h4>${item.name}</h4>
        <p>${item.text}<br>${item.size} • ${item.placement}</p>
        ${item.notes ? `<p>${item.notes}</p>` : ""}
      </div>
      <div>
        <strong>${formatPrice(item.price)}</strong>
        <button class="remove-item" data-id="${item.id}" type="button">Remove</button>
      </div>
    </article>
  `).join("");

  cartItems.querySelectorAll(".remove-item").forEach((button) => {
    button.addEventListener("click", () => removeFromCart(button.dataset.id));
  });

  const total = state.cart.reduce((sum, item) => sum + item.price, 0);
  cartSubtotal.textContent = formatPrice(total);
  cartCount.textContent = String(state.cart.length);
}

function removeFromCart(id) {
  state.cart = state.cart.filter((item) => item.id !== id);
  renderCart();
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("show");
  window.clearTimeout(showToast.timeoutId);
  showToast.timeoutId = window.setTimeout(() => toast.classList.remove("show"), 2200);
}

function openCheckout() {
  if (!state.cart.length) {
    showToast("Add a bag before checkout");
    return;
  }
  checkoutModal.classList.add("open");
  checkoutModal.setAttribute("aria-hidden", "false");
}

function closeCheckout() {
  checkoutModal.classList.remove("open");
  checkoutModal.setAttribute("aria-hidden", "true");
}

function handleCheckout(event) {
  event.preventDefault();
  const formData = new FormData(checkoutForm);
  const customer = Object.fromEntries(formData.entries());
  const total = state.cart.reduce((sum, item) => sum + item.price, 0);
  const message = `Thank you, ${customer.name}! Your NAYARA order for ${formatPrice(total)} is confirmed.`;
  showToast(message);
  state.cart = [];
  renderCart();
  checkoutForm.reset();
  closeCheckout();
}

function bindEvents() {
  bagColor.addEventListener("change", (event) => {
    state.color = event.target.value;
    updatePreview();
  });

  bagSize.addEventListener("change", (event) => {
    state.size = event.target.value;
    updatePreview();
  });

  nameInput.addEventListener("input", (event) => {
    state.text = event.target.value;
    updatePreview();
  });

  fontStyle.addEventListener("change", (event) => {
    state.font = event.target.value;
    updatePreview();
  });

  textColor.addEventListener("input", (event) => {
    state.textColor = event.target.value;
    updatePreview();
  });

  logoUpload.addEventListener("change", (event) => {
    const file = event.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (loadEvent) => {
      state.image = loadEvent.target?.result || null;
      updatePreview();
    };
    reader.readAsDataURL(file);
  });

  bagNotes.addEventListener("input", (event) => {
    state.notes = event.target.value;
  });

  document.querySelector(".add-button").addEventListener("click", addToCart);
  document.querySelector(".cart-button").addEventListener("click", () => {
    cartDrawer.classList.add("open");
    cartDrawer.setAttribute("aria-hidden", "false");
  });
  document.querySelector(".close-cart").addEventListener("click", () => {
    cartDrawer.classList.remove("open");
    cartDrawer.setAttribute("aria-hidden", "true");
  });
  document.querySelector(".checkout-button").addEventListener("click", openCheckout);
  document.querySelector(".close-modal").addEventListener("click", closeCheckout);
  document.querySelector(".modal-backdrop").addEventListener("click", closeCheckout);
  checkoutForm.addEventListener("submit", handleCheckout);

  document.querySelectorAll(".placement").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".placement").forEach((item) => item.classList.toggle("active", item === button));
      state.placement = button.dataset.placement;
      updatePreview();
    });
  });

  chatToggle.addEventListener("click", () => {
    const isOpen = chatPanel.classList.toggle("open");
    chatToggle.setAttribute("aria-expanded", String(isOpen));
    chatPanel.setAttribute("aria-hidden", String(!isOpen));
    if (isOpen) chatInput.focus();
  });

  chatClose.addEventListener("click", () => {
    chatPanel.classList.remove("open");
    chatToggle.setAttribute("aria-expanded", "false");
    chatPanel.setAttribute("aria-hidden", "true");
  });

  chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const message = chatInput.value.trim();
    if (!message) return;

    appendMessage(message, "user");
    chatInput.value = "";
    chatInput.style.height = "48px";
    chatSend.disabled = true;
    const typing = showTyping();

    try {
      const available = await checkChatAvailability();
      if (!available) {
        typing.remove();
        appendMessage("Please start the Ollama service and make sure llama3.2:latest is installed. You can run: ollama pull llama3.2:latest", "bot");
        return;
      }

      const answer = await sendChatMessage(message);
      typing.remove();
      appendMessage(answer, "bot");
    } catch (error) {
      typing.remove();
      appendMessage("I could not reach the local Ollama service. Please ensure Ollama is running on port 11434.", "bot");
      setChatStatus("Connection failed", true);
    } finally {
      chatSend.disabled = false;
      chatInput.focus();
    }
  });

  chatInput.addEventListener("input", () => {
    chatInput.style.height = "auto";
    chatInput.style.height = `${Math.min(chatInput.scrollHeight, 120)}px`;
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      cartDrawer.classList.remove("open");
      closeCheckout();
      chatPanel.classList.remove("open");
      chatToggle.setAttribute("aria-expanded", "false");
      chatPanel.setAttribute("aria-hidden", "true");
    }
  });
}

renderProducts();
renderBagTypes();
renderCart();
bindEvents();
updatePreview();
checkChatAvailability();
