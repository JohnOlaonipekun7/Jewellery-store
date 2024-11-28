Project Features So Far
ACCOUNTS APP:
Custom user model (CustomUser) extending Django's AbstractUser.
SignUpView for user registration.
Login and logout configured:
LOGIN_REDIRECT_URL = 'shop:all_products'
LOGOUT_REDIRECT_URL = 'shop:all_products'

SHOP APP:
Models:
Category model: Represents product categories.
Product model: Represents products with fields like name, price, description, stock.
Admin Configuration:
CategoryAdmin: Displays and allows searching categories in the admin panel.
ProductAdmin: Provides editing and searching for products in the admin panel.
URLs:
Configured basic URL structure for the shop app.
Views:
ProductListView: Displays a list of all available products.
Templates:
Created shop/prod_list.html for product listings.
