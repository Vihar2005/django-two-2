from django.contrib import admin
from .models import User,Product,Wishlist,Cart,Blog
# Register your models here.
admin.site.site_header="Eiser-Shop"
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Blog)
