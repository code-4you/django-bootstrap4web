=====
Bootstrap4web
=====

Bootstrap4web is a simple Django app that configure a perfect single page
web in bootstrap 4. It's only a single. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "bootstrap4web" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bootstrap4web',
    ]

2. Include the bootstrap4web URLconf in your project urls.py like this::

    path('bootstrap/', include('bootstrap4web.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
