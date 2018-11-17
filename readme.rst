=====
Quick Search
=====

Pending

Quick start
-----------

1. Add "quick_search" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'quick_search',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('quick_search/', include('quick_search.urls')),

3. Run `python manage.py migrate` to create the quick_search models.

4. GGWP