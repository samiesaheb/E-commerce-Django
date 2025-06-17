import os
from decimal import Decimal

import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skyhigh.settings")
django.setup()

from core.models import Brand, Product

products_by_brand = {
    "geometry": [
        {
            "name": "Geometry Facial Foam",
            "slug": "geometry-whitening-facial-foam",
            "description": "A gentle, pH-balanced cleansing foam that purifies and refreshes skin without stripping moisture. Ideal for daily use to remove impurities and leave skin feeling soft and supple.",
            "price": Decimal("120.00"),
        },
        {
            "name": "Geometry Hair Serum",
            "slug": "geometry-extra-hair-serum",
            "description": "A lightweight hair serum formulated with argan oil and keratin to add shine, reduce frizz, and protect against heat damage. Promotes healthy-looking, silky smooth hair.",
            "price": Decimal("149.99"),
        },
        {
            "name": "Geometry Sunscreen SPF 50",
            "slug": "geometry-sunscreen-facial-cream",
            "description": "Broad-spectrum SPF 50 sunscreen offering superior protection against UVA/UVB rays. Non-greasy, fast-absorbing formula suitable for all skin types, leaving no white cast.",
            "price": Decimal("99.99"),
        },
    ],
    "facial-care": [
        {
            "name": "ACNI-DS PLUS Face Wash",
            "slug": "acni-ds-plus-face-wash",
            "description": "Gentle cleanser with Glycolic and Salicylic Acid, exfoliates oily and acne-prone skin for clearer, younger-looking skin.",
        },
        {
            "name": "Facy Clean Face Wash",
            "slug": "facy-clean-face-wash",
            "description": "Vitamin C-enriched cleanser for lasting oil control, skin brightening, acne reduction, and pH balance.",
        },
        {
            "name": "GLOFIX Whitening Face Wash",
            "slug": "glofix-whitening-face-wash",
            "description": "Purifying cleanser that removes dull surface cells, reduces blemishes, and promotes brighter, even-toned skin.",
        },
        {
            "name": "TIMELESS Whitening Face Wash",
            "slug": "timeless-whitening-face-wash",
            "description": "Deeply cleansing and exfoliating face wash that brightens skin, reduces breakouts, and enhances skin clarity and texture.",
        },
        {
            "name": "Globac Face Wash",
            "slug": "globac-face-wash",
            "description": "Daily cleanser with Salicylic Acid and Nicotinamide that purifies skin, removes dullness, and enhances brightness.",
        },
        {
            "name": "Facyglow Plus Face Wash",
            "slug": "facyglow-plus-face-wash",
            "description": "Face wash for oily and acne-prone skin, deeply cleansing impurities, brightening skin tone, and restoring moisture.",
        },
        {
            "name": "Acne Cleaner Cleansing Gel",
            "slug": "acne-cleaner-cleansing-gel",
            "description": "Removes excess oil, impurities, and acne-causing bacteria, leaving skin soft, moisturized, and visibly clear.",
        },
        {
            "name": "NI-ACNE Liquid Cleanser",
            "slug": "ni-acne-liquid-cleanser",
            "description": "Refreshing cleansing water for oily, acne-prone skin. Removes makeup, excess oil, and reduces irritation.",
        },
        {
            "name": "FACY GLOW Cream",
            "slug": "facy-glow-cream",
            "description": "Whitening cream that reduces dark spots, fine lines, and hyperpigmentation. Provides lasting hydration and UV protection.",
        },
        {
            "name": "D Silk Whitening Cream",
            "slug": "d-silk-whitening-cream",
            "description": "Nourishing cream that reduces fine lines and wrinkles while hydrating and smoothing skin tone for face and neck.",
        },
        {
            "name": "ZEFLAX Anti Melasma Cream",
            "slug": "zeflax-anti-melasma-cream",
            "description": "Melasma treatment cream that reduces freckles and dark spots, moisturizes, and promotes radiant, even-toned skin.",
        },
        {
            "name": "I TOX Whitening Cream",
            "slug": "i-tox-whitening-cream",
            "description": "Intensive whitening cream that hydrates deeply, reduces sun-induced hyperpigmentation, and smoothens skin tone.",
        },
        {
            "name": "Alovete Plus Moisturizing Cream",
            "slug": "alovete-plus-moisturizing-cream",
            "description": "Deeply moisturizing cream for dry, sensitive skin. Restores lipid barrier and soothes irritation.",
        },
        {
            "name": "ARBUTIN-DS Serum",
            "slug": "arbutin-ds-serum",
            "description": "Anti-melasma serum with Alpha Arbutin, Vitamin C, and Kojic Acid. Reduces freckles and enhances radiance.",
        },
        {
            "name": "Facy Acney Gel",
            "slug": "facy-acney-gel",
            "description": "Fast-acting acne treatment gel. Reduces redness, inflammation, and breakouts with targeted application.",
        },
    ],
    "body-and-skin-care": [
        {
            "name": "D White Whitening Soap",
            "slug": "d-white-whitening-soap",
            "description": "Soap enriched with Glutathione, Kojic Acid, and Vitamin C for cleansing and whitening the skin.",
        },
        {
            "name": "DANGLOW Bar",
            "slug": "danglow-bar",
            "description": "Anti-fungal soap with Ketoconazole & ZPTO that combats fungal infections and protects skin.",
        },
        {
            "name": "KCN-BAR",
            "slug": "kcn-bar",
            "description": "Ketoconazole & ZPTO soap that provides effective protection against fungal conditions.",
        },
        {
            "name": "Ketofast Bar",
            "slug": "ketofast-bar",
            "description": "Therapeutic soap bar that prevents dandruff and fungal infections while gently cleansing.",
        },
        {
            "name": "PERTHIN Bar",
            "slug": "perthin-bar",
            "description": "Soap with Permethrin & Aloe Vera for daily moisturizing, protection, and skin care.",
        },
        {
            "name": "SCALICE Bar",
            "slug": "scalice-bar",
            "description": "Permethrin & Aloe Vera soap that soothes and hydrates sensitive skin.",
        },
        {
            "name": "Perzil Plus Bar",
            "slug": "perzil-plus-bar",
            "description": "Daily use soap that gently cleanses and moisturizes with Aloe Vera & Permethrin.",
        },
        {
            "name": "FAST PRO Bar",
            "slug": "fast-pro-bar",
            "description": "Mild soap for sensitive skin, enriched with Permethrin & Aloe Vera for daily care.",
        },
        {
            "name": "PERTHIN Lotion",
            "slug": "perthin-lotion",
            "description": "Rich lotion with Permethrin & Cetrimide that moisturizes deeply and firms the skin.",
        },
        {
            "name": "Neonate D Baby Soap",
            "slug": "neonate-d-baby-soap",
            "description": "Gentle soap for baby skin that cleanses, hydrates, and protects against irritation.",
        },
        {
            "name": "V-BEST Intimate Hygiene Wash",
            "slug": "v-best-intimate-hygiene-wash",
            "description": "Hygiene wash with lactic acid and tea tree oil to maintain pH and provide daily comfort.",
        },
    ],
    "hair-care": [
        {
            "name": "DANGLOW Shampoo",
            "slug": "danglow-shampoo",
            "description": "Strengthening & Protective Shampoo that fortifies and shields hair against chemical and heat damage, leaving it strong, shiny, and smooth.",
        },
        {
            "name": "CLEAN UP DS Shampoo",
            "slug": "clean-up-ds-shampoo",
            "description": "Anti-dandruff shampoo designed to repair dull and brittle hair, revive split ends, protect against heat and chemical damage, and restore shine and vitality.",
        },
        {
            "name": "MYCO HAIR Long Hair & Anti-Hair Loss Serum",
            "slug": "myco-hair-long-hair-anti-hair-loss-serum",
            "description": "Powerful serum enriched with Essential Amino Acids, Organic Argan Oil, Pro-Vitamin B5, and botanical extracts.",
        },
    ],
}

# Create products
for brand_slug, products in products_by_brand.items():
    try:
        brand = Brand.objects.get(slug=brand_slug)
        for product in products:
            try:
                obj, created = Product.objects.update_or_create(
                    brand=brand,
                    slug=product["slug"],
                    defaults={
                        "name": product["name"],
                        "description": product["description"],
                        "price": product.get("price", Decimal("0.00")),
                    },
                )
                status = "🆕 Created" if created else "✅ Exists"
                print(f"{status}: {obj.name}")
            except Exception as e:
                print(f"❌ Failed to create product '{product['name']}': {e}")
        print(f"✅ Finished seeding {len(products)} products for brand: {brand_slug}")
    except Brand.DoesNotExist:
        print(f"⚠️ Brand with slug '{brand_slug}' not found. Skipping...")
