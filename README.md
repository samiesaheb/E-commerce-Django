# 💄 Sky High Cosmetics Website

A full-featured, modern cosmetics e-commerce site built with **Django**, Alpine.js, and Tailwind CSS. This platform supports private-label OEM product browsing, brand discovery, advanced services, and dynamic shopping experiences.

---

## 🚀 Features

### 🛍️ E-commerce Functionality
- **Dynamic Brands & Products**
  - Dedicated brand pages (e.g. `/brands/geometry/`)
  - Product detail pages with descriptions, prices, and images
  - Product categories: Geometry, Hair Care, Facial Care, Body & Skin Care

- **Cart System**
  - Add-to-cart functionality
  - Live cart item counter in header
  - Checkout and payment processing routes (`/checkout`, `/process-payment/`)

- **Product Search**
  - Live search bar with:
    - Real-time suggestions via API
    - Keyboard navigation (↑ ↓ Enter)
    - Bolded matching product text
    - Lazy-loaded product thumbnails

---

### 💼 Services Section
- **Services Overview Page**
  - Each service with title, short description, and link to detail page

- **Individual Service Detail Pages**
  - Extended sections:
    - ✅ Our Expertise
    - 💡 Why Choose Us
    - 🔧 How We Work
  - SEO-friendly slugs (e.g. `/services/custom-formulation/`)

---

### 👤 User Authentication
- Login, Signup, Logout using Django AllAuth
- Profile menu with auth-based display
- Authentication sidebar with smooth animations

---

### 🎨 UI/UX Enhancements
- **Responsive Header**
  - Sticky and auto-hiding on scroll
  - Centered logo, left-aligned hamburger, and right-side cart/profile

- **Animated Sidebars**
  - Left sidebar: Navigation and brand links with dropdown
  - Right sidebar: User authentication actions
  - Transitions with `x-transition` and `transform/scale/opacity`

- **Search UX**
  - Enhanced dropdown suggestion box
  - Debounced input with clean keyboard support
  - Click-outside and escape handling

---

### 🧱 Architecture & Structure
- Modular views (`core.views.services`, `products`, `auth`, `cart`)
- Templated with Tailwind CSS
- Static files managed and served properly
- URL namespaces for clean routing (e.g., `services:service_detail`)

---

## 📂 Project Structure Overview

```bash
core/
├── views/
│   ├── services.py
│   ├── products.py
│   └── auth.py
├── templates/
│   └── core/
│       ├── header.html
│       ├── services.html
│       ├── service_detail.html
│       ├── product_search_bar.html
│       └── ...
└── urls/
    ├── services.py
    └── ...
