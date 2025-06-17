from django.shortcuts import render
from django.http import Http404

# Service data with slugs
services_data = [
    {
        "slug": "after-sales-support",
        "title": "After Sales Support",
        "description": (
            "Our relationship with clients doesn't end at production. We offer dedicated after-sales support "
            "to ensure your brand thrives in the market, helping you respond to challenges, adapt to shifting demands, "
            "and sustain long-term customer satisfaction."
        ),
    },
    {
        "slug": "regulatory-legal-services",
        "title": "Regulatory & Legal Services",
        "description": (
            "Navigating complex cosmetic regulations can be daunting. Our regulatory team ensures your products meet "
            "both local and international compliance standards—protecting your brand’s reputation and securing intellectual "
            "property from the start."
        ),
    },
    {
        "slug": "packaging-solutions",
        "title": "Packaging Solutions",
        "description": (
            "Packaging is your product’s first impression—and we make it count. Our team delivers creative, functional, "
            "and eco-conscious packaging that enhances shelf appeal, reinforces your branding, and elevates user experience."
        ),
    },
    {
        "slug": "custom-formulation",
        "title": "Custom Formulation",
        "description": (
            "Transform your product ideas into standout formulas. With a deep understanding of cosmetic science and "
            "market trends, our chemists develop custom formulations that are innovative, effective, and tailored to your "
            "target audience."
        ),
    },
    {
        "slug": "personal-care",
        "title": "Personal Care",
        "description": (
            "From daily hygiene to premium wellness products, we co-create personal care solutions that blend science, "
            "safety, and sophistication. Our OEM capabilities ensure each product reflects your brand's values and meets "
            "high consumer expectations."
        ),
    },
    {
        "slug": "baby-sensitive-skin",
        "title": "Baby & Sensitive Skin",
        "description": (
            "Delicate skin deserves uncompromising care. We specialize in gentle formulations free from harsh chemicals—"
            "crafted to meet the highest safety standards for babies and sensitive skin types."
        ),
    },
    {
        "slug": "body-care",
        "title": "Body Care",
        "description": (
            "Our body care range supports your brand in delivering nourishment, hydration, and rejuvenation. With scalable "
            "OEM production, we help you offer everything from body lotions to scrubs with exceptional quality and consistency."
        ),
    },
    {
        "slug": "hair-care",
        "title": "Hair Care",
        "description": (
            "Help your customers achieve healthier, stronger hair with our science-backed formulations. From anti-hair fall "
            "serums to moisturizing shampoos, we offer full-spectrum OEM hair care development tailored to global market needs."
        ),
    },
    {
        "slug": "skincare-solutions",
        "title": "Skincare Solutions",
        "description": (
            "Modern skincare is about results and trust. We provide advanced, dermatologist-informed solutions—from brightening "
            "creams to anti-aging serums—manufactured to exceed industry benchmarks in efficacy and safety."
        ),
    },
]

# Home services page
def services_view(request):
    return render(request, "core/services.html", {"services": services_data})


# Individual service detail page
def service_detail_view(request, slug):
    service = next((s for s in services_data if s["slug"] == slug), None)
    if not service:
        raise Http404("Service not found")
    return render(request, "core/service_detail.html", {"service": service})
