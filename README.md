from pathlib import Path

# Define the README content
readme_content = """# 💄 Sky High Cosmetics Website

A full-featured, modern cosmetics e-commerce site built with Django, Alpine.js, and Tailwind CSS. This platform supports private-label OEM product browsing, brand discovery, advanced services, and dynamic shopping experiences.

---

## 🚀 Features

### 🛍️ E-commerce Functionality

#### Dynamic Brands & Products
- Dedicated brand pages (e.g. `/brands/geometry/`)
- Product detail pages with descriptions, prices, and images
- Product categories: Geometry, Hair Care, Facial Care, Body & Skin Care
- Session-based cart data rendering in all templates via global context processor

#### Cart System
- Add-to-cart functionality
- Live cart item counter in header
- Cart dropdown with dynamic item display: name, quantity, price, and image
- Cart total dynamically shown in header dropdown
- Checkout and payment processing routes (`/checkout`, `/process-payment/`)

#### Product Search
- Live search bar with:
  - Real-time suggestions via `/products/api/search-suggestions/`
  - Keyboard navigation (↑ ↓ Enter)
  - Bolded matching text only in suggestions
  - Lazy-loaded product thumbnails

---

### 💼 Services Section

#### Services Overview Page
- Each service with title, short description, and link to detail page

#### Individual Service Detail Pages
- Extended sections:
  - ✅ Our Expertise  
  - 💡 Why Choose Us  
  - 🔧 How We Work  
- SEO-friendly slugs (e.g. `/services/custom-formulation/`)

---

### 👤 User Authentication

- Login, Signup, Logout using Django AllAuth
- Authentication sidebar with smooth transition animations
- Profile dropdown in header, revealed on hover
- Password reset and change flows with 6 styled templates

---

### 🎨 UI/UX Enhancements

#### Responsive Header
- Sticky and auto-hiding on scroll
- Centered logo, left-aligned hamburger, and right-side cart/profile icons

#### Animated Sidebars
- Left sidebar: Navigation and brand links with dropdown
- Right sidebar: User authentication actions
- Toggle animations with Alpine.js transitions
- Close button aligns with hamburger icon for clean UX

#### Cart UX
- Hoverable cart dropdown
- Live preview of items in cart including name, quantity, image, and total
- Fully responsive for desktop and mobile views

#### Search UX
- Enhanced dropdown suggestion box
- Debounced input with clean keyboard support
- Click-outside and escape key handling

---

### 🧱 Architecture & Structure

- Modular views (`core.views.services`, `products`, `auth`, `cart`)
- Clean URL namespaces (e.g., `services:service_detail`)
- Templated with Tailwind CSS
- Static/media file management
- Alpine.js used for interactivity
- Custom context processors for cart and search integration
"""

# Save the content to a Markdown file
output_path = Path("/mnt/data/Sky_High_Cosmetics_README.md")
output_path.write_text(readme_content)

output_path.name
