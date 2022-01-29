from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import AccountCreationForm, AccountChangeForm
from .models import Account


class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    list_display = [
        "email",
        "is_staff",
        "uuid",
    ]
    ordering = ("email",)
    readonly_fields = ["uuid"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
    )
    search_fields = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(Account, AccountAdmin)
