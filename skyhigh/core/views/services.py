from django.shortcuts import render
from django.http import Http404

# Full service data with slugs, highlights, and steps
services_data = [
    {
        "slug": "after-sales-support",
        "title": "After Sales Support",
        "description": (
            "Launching a product is just the beginning. Sky High offers tailored after-sales services to help you troubleshoot issues, "
            "refine your offerings, and respond to market feedback. With our proactive approach, we empower your brand to thrive in a competitive environment."
        ),
        "highlights": [
            "Proactive Assistance: We work closely with you to anticipate and address potential challenges, ensuring smooth operations post-launch.",
            "Customer-Centric Approach: Our services focus on improving customer experience and satisfaction, helping you build a loyal customer base.",
        ],
        "how_we_work": [
            "Feedback Collection: Collaborate with you to gather and analyze market and customer feedback.",
            "Issue Resolution: Provide actionable solutions for any product or customer concerns.",
            "Performance Optimization: Recommend adjustments to formulations or packaging based on real-world performance and trends.",
            "Continuous Support: Stay connected to offer ongoing guidance and consultation for sustained success.",
        ],
    },
    {
        "slug": "regulatory-legal-services",
        "title": "Regulatory & Legal Services",
        "description": (
            "From product registration to trademark support, we assist our clients in every step of the process, enabling them to focus on building their brand "
            "while we handle the complexities of regulatory compliance and legal protection."
        ),
        "highlights": [
            "Expert Knowledge: Our team stays updated on the latest regulatory changes and industry standards.",
            "Streamlined Processes: We simplify complex procedures, saving you time and resources while ensuring accuracy and compliance.",
            "Comprehensive Support: From ingredient compliance to trademark registration, we provide end-to-end assistance tailored to your needs.",
            "Global Reach: Our expertise spans multiple markets, helping your brand achieve international success.",
        ],
        "how_we_work": [
            "Consultation: Understand your regulatory needs and identify the necessary approvals for your target market.",
            "Documentation & Testing: Assist with preparing and submitting required documentation and arranging testing as per regulations.",
            "Registration & Certification: Guide you through the registration process for smooth approval of your products.",
            "IP & Trademark Protection: Help you secure intellectual property rights to protect your brand and products.",
        ],
    },
    {
        "slug": "packaging-solutions",
        "title": "Packaging Solutions",
        "description": (
            "With a focus on quality and customization, we collaborate with you to develop packaging that complements your product and brand values."
        ),
        "highlights": [
            "Customization: Tailored packaging aligned with your brand’s image and product needs.",
            "Quality & Functionality: Designed to provide practicality and durability.",
            "Sustainability: Eco-friendly materials and designs available.",
            "Full-Service Support: From design to production.",
        ],
        "how_we_work": [
            "Consultation: Discuss packaging requirements and brand vision.",
            "Design & Development: Collaborate on functional and attractive packaging.",
            "Material Selection: Choose from a variety of materials and styles.",
            "Production & Delivery: Manufacture and deliver high-quality packaging.",
        ],
    },
    {
        "slug": "custom-formulation",
        "title": "Custom Formulation",
        "description": (
            "We provide end-to-end custom formulation services to create innovative, high-quality products that align with your brand identity."
        ),
        "highlights": [
            "End-to-End Solutions: From concept to delivery.",
            "Expertise & Innovation: Cutting-edge knowledge to meet market demands.",
            "Flexibility: Scalable for startups and established brands.",
            "Global Standards: Ensuring your products are market-ready.",
        ],
        "how_we_work": [
            "Consultation: Share your brand vision and product goals.",
            "Formulation Development: Tailored formulations tested for efficacy and safety.",
            "Packaging Design: Attractive, functional, and sustainable solutions.",
            "Production & Delivery: Precision manufacturing and timely delivery.",
        ],
    },
    {
        "slug": "personal-care",
        "title": "Personal Care",
        "description": (
            "We develop personal care and hygiene products that are gentle, effective, and backed by scientific advancements."
        ),
        "highlights": [
            "Tailored Solutions: Developed to match your target audience’s needs.",
            "Uncompromising Quality: Meeting stringent safety and quality standards.",
            "Innovative Formulations: Using the latest personal care science.",
            "Scalable Production: Flexible from boutique to mass production.",
        ],
        "how_we_work": [
            "Consultation: Conceptualize products aligned with your brand.",
            "Formulation & Testing: Ensure safety and effectiveness.",
            "Manufacturing & Packaging: Advanced processes and elegant packaging.",
            "Delivery: On-time and ready for your customers.",
        ],
    },
    {
        "slug": "baby-sensitive-skin",
        "title": "Baby & Sensitive Skin",
        "description": (
            "We specialize in hypoallergenic, dermatologically tested products that offer the highest safety and comfort for delicate skin."
        ),
        "highlights": [
            "Safe & Gentle: Hypoallergenic and dermatologically tested.",
            "Premium Quality: Crafted with the finest, skin-friendly ingredients.",
            "Customization: Reflect your brand’s commitment to care.",
            "Innovation: Modern solutions for sensitive skin.",
        ],
        "how_we_work": [
            "Understanding Your Needs: Aligning with your brand’s vision.",
            "Formulation & Testing: Meeting rigorous safety standards.",
            "Manufacturing & Packaging: High-quality, elegant packaging.",
            "Delivery: Timely and in perfect condition.",
        ],
    },
    {
        "slug": "body-care",
        "title": "Body Care",
        "description": (
            "We create body care products that combine comfort, confidence, and a touch of indulgence, using premium ingredients and cutting-edge formulations."
        ),
        "highlights": [
            "Customization: Unique formulations and designs.",
            "Uncompromising Quality: Meeting the highest standards.",
            "Innovation: Ahead-of-the-curve body care solutions.",
            "Flexible Manufacturing: From small to large scale.",
        ],
        "how_we_work": [
            "Concept Development: From idea to product.",
            "Formulation & Testing: Rigorous quality and safety testing.",
            "Manufacturing & Packaging: Advanced and flawless execution.",
            "Delivery: Reliable and ready to impress.",
        ],
    },
    {
        "slug": "hair-care",
        "title": "Hair Care",
        "description": (
            "We deliver hair care solutions that nourish, repair, and style with ease—suitable for all hair types and concerns."
        ),
        "highlights": [
            "Tailored Solutions: Aligned with your brand vision.",
            "Premium Quality: High-grade ingredients and standards.",
            "Cutting-Edge Innovation: Trend-aligned and effective.",
            "Scalable Production: Supporting all business sizes.",
        ],
        "how_we_work": [
            "Ideation & Consultation: Develop your tailored range.",
            "Formulation & Testing: Safety and performance ensured.",
            "Manufacturing & Packaging: Flawless results.",
            "Delivery: On-time, market-ready delivery.",
        ],
    },
    {
        "slug": "skincare-solutions",
        "title": "Skincare Solutions",
        "description": (
            "We offer dermatologist-informed skincare—from brightening creams to anti-aging serums—exceeding industry standards."
        ),
        "highlights": [
            "Customization: Tailored formulations and packaging.",
            "Quality Assurance: Compliant with global standards.",
            "Innovation: Trend-forward skincare science.",
            "Scalability: Boutique to mass-market capability.",
        ],
        "how_we_work": [
            "Concept Development: Translate ideas into products.",
            "Formulation & Testing: High-performance and safe.",
            "Production & Packaging: Flawless and efficient.",
            "Delivery: Secure, prompt delivery to market.",
        ],
    },
]

def services_view(request):
    return render(request, "core/services.html", {"services": services_data})

def service_detail_view(request, slug):
    service = next((s for s in services_data if s["slug"] == slug), None)
    if not service:
        raise Http404("Service not found")
    return render(request, "core/service_detail.html", {"service": service})
