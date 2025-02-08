from chatbot.models import Supplier, Product

# Creating Suppliers
apple = Supplier.objects.create(
    name="Apple Inc.",
    contact_info="1 Infinite Loop, Cupertino, CA 95014, USA | support@apple.com",
    product_categories_offered="Smartphones, Laptops, Tablets, Wearables"
)

samsung = Supplier.objects.create(
    name="Samsung Electronics",
    contact_info="Samsung Town, Seoul, South Korea | support@samsung.com",
    product_categories_offered="Smartphones, TVs, Home Appliances, Wearables"
)

xiaomi = Supplier.objects.create(
    name="Xiaomi Corporation",
    contact_info="Beijing, China | support@xiaomi.com",
    product_categories_offered="Smartphones, IoT Devices, Smart Home Gadgets"
)

oneplus = Supplier.objects.create(
    name="OnePlus Technology",
    contact_info="Shenzhen, China | support@oneplus.com",
    product_categories_offered="Smartphones, Accessories"
)

google = Supplier.objects.create(
    name="Google LLC",
    contact_info="1600 Amphitheatre Parkway, Mountain View, CA 94043, USA | support@google.com",
    product_categories_offered="Smartphones, Laptops, Software"
)

huawei = Supplier.objects.create(
    name="Huawei Technologies",
    contact_info="Shenzhen, China | support@huawei.com",
    product_categories_offered="Smartphones, Networking Equipment"
)

# Creating Products

# Apple Products
Product.objects.create(
    name="iPhone 14 Pro",
    brand="Apple",
    price=999.99,
    category="Smartphone",
    description="Latest iPhone featuring the advanced A16 Bionic chip and an innovative camera system.",
    supplier=apple
)
Product.objects.create(
    name="iPhone 14",
    brand="Apple",
    price=799.99,
    category="Smartphone",
    description="Standard model offering robust performance with modern features.",
    supplier=apple
)
Product.objects.create(
    name="MacBook Pro 14-inch",
    brand="Apple",
    price=1999.99,
    category="Laptop",
    description="Powerful laptop equipped with the M1 Pro chip for professional-grade performance.",
    supplier=apple
)
Product.objects.create(
    name="iPad Pro",
    brand="Apple",
    price=1099.99,
    category="Tablet",
    description="High-end tablet featuring a ProMotion display and the powerful M1 chip.",
    supplier=apple
)
Product.objects.create(
    name="Apple Watch Series 8",
    brand="Apple",
    price=399.99,
    category="Wearable",
    description="Advanced smartwatch with comprehensive health tracking and a vibrant display.",
    supplier=apple
)

# Samsung Products
Product.objects.create(
    name="Galaxy S23 Ultra",
    brand="Samsung",
    price=1199.99,
    category="Smartphone",
    description="Flagship smartphone featuring a 200MP camera system and S Pen support.",
    supplier=samsung
)
Product.objects.create(
    name="Galaxy S23",
    brand="Samsung",
    price=899.99,
    category="Smartphone",
    description="High-performance smartphone with an immersive display and advanced features.",
    supplier=samsung
)
Product.objects.create(
    name="Galaxy Note 20",
    brand="Samsung",
    price=999.99,
    category="Smartphone",
    description="Productivity-focused smartphone with an integrated S Pen for creativity and work.",
    supplier=samsung
)
Product.objects.create(
    name="Galaxy Tab S8",
    brand="Samsung",
    price=649.99,
    category="Tablet",
    description="Versatile tablet designed for both entertainment and productivity.",
    supplier=samsung
)
Product.objects.create(
    name="Samsung Galaxy Watch 5",
    brand="Samsung",
    price=279.99,
    category="Wearable",
    description="Smartwatch with advanced health monitoring and seamless integration with Samsung devices.",
    supplier=samsung
)

# Xiaomi Products
Product.objects.create(
    name="Redmi Note 11",
    brand="Xiaomi",
    price=199.99,
    category="Smartphone",
    description="Affordable smartphone offering solid performance and long-lasting battery life.",
    supplier=xiaomi
)
Product.objects.create(
    name="Redmi Note 10",
    brand="Xiaomi",
    price=179.99,
    category="Smartphone",
    description="Popular budget-friendly smartphone with reliable features and sleek design.",
    supplier=xiaomi
)
Product.objects.create(
    name="Xiaomi Mi 11",
    brand="Xiaomi",
    price=699.99,
    category="Smartphone",
    description="Premium smartphone with cutting-edge technology and a stunning display.",
    supplier=xiaomi
)
Product.objects.create(
    name="Xiaomi Mi Band 6",
    brand="Xiaomi",
    price=49.99,
    category="Wearable",
    description="Affordable fitness tracker with a vibrant AMOLED display and comprehensive health tracking.",
    supplier=xiaomi
)

# OnePlus Products
Product.objects.create(
    name="OnePlus 10 Pro",
    brand="OnePlus",
    price=899.99,
    category="Smartphone",
    description="High-performance smartphone with ultra-fast charging and a fluid display.",
    supplier=oneplus
)
Product.objects.create(
    name="OnePlus Nord 2",
    brand="OnePlus",
    price=399.99,
    category="Smartphone",
    description="Mid-range smartphone balancing performance and affordability with a sleek design.",
    supplier=oneplus
)

# Google Products
Product.objects.create(
    name="Pixel 7 Pro",
    brand="Google",
    price=899.99,
    category="Smartphone",
    description="Google's flagship device with advanced AI photography and Tensor chip.",
    supplier=google
)
Product.objects.create(
    name="Pixel 7",
    brand="Google",
    price=599.99,
    category="Smartphone",
    description="Streamlined smartphone offering a pure Android experience and excellent camera performance.",
    supplier=google
)

# Huawei Products
Product.objects.create(
    name="Huawei P50 Pro",
    brand="Huawei",
    price=799.99,
    category="Smartphone",
    description="Innovative smartphone featuring top-tier photography capabilities and a sleek design.",
    supplier=huawei
)
Product.objects.create(
    name="Huawei Mate 40 Pro",
    brand="Huawei",
    price=1099.99,
    category="Smartphone",
    description="Flagship smartphone with powerful performance and cutting-edge technology.",
    supplier=huawei
)
