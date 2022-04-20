from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio


# HOME

admin.site.register(Home)

# ABOUT
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

# SKILLS
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]


    # PORTFOLIO
    admin.site.register(Portfolio)