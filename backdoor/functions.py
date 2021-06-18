# This file is for functions that will alter certain behaviors for your system

from django.utils.crypto import get_random_string

def get_random_slug(obj):
    # This is to get a random and unique slug for a posts
    if not obj.slug: # if no slug present
        obj.slug = get_random_string(16)
        is_not_unique = True

        while is_not_unique:
            is_not_unique = False

            obj_with_slug = type(obj).objects.filter(slug=obj.slug)
            if len(obj_with_slug) > 0:
                is_not_unique = True # slug not unique

            bad_words = ['fuck', 'shit']
            if obj.slug in bad_words:
                is_not_unique = True # no bad words

            if is_not_unique:
                obj.slug = get_random_string(16) # continue looking