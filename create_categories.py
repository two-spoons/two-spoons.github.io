#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('/home/two_spoons/Documents/twospoonsanewhope')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_site.settings')
django.setup()

from blog.models import Category

# Create the three categories
categories = [
    {'name': 'Writing', 'slug': 'writing', 'description': 'Articles about creative writing, storytelling, and literature.'},
    {'name': 'Casting', 'slug': 'casting', 'description': 'Posts about casting, auditions, and performance.'},
    {'name': 'Coding', 'slug': 'coding', 'description': 'Technical articles about programming and software development.'},
]

for cat_data in categories:
    category, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults={
            'name': cat_data['name'],
            'description': cat_data['description']
        }
    )
    if created:
        print(f"Created category: {category.name}")
    else:
        print(f"Category already exists: {category.name}")

print("All categories created successfully!")