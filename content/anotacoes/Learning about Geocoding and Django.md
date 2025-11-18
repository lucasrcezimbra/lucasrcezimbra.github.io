---
title: Learning about Geocoding and Django
date: 2025-11-15
lastmod: 2025-11-18
---

- Spatialite 5.0.1 doesn't work with Django
  - https://groups.google.com/g/spatialite-users/c/SnNZt4AGm_o?pli=1
  - https://code.djangoproject.com/ticket/32935
  - https://forum.djangoproject.com/t/no-such-column-rowid-error-with-django-4-2-and-spatialite-5-0-1/30277
  - https://github.com/makinacorpus/django-geojson/blob/8ec70ccf966ca580621245647dd9de98bbecb80f/quicktest.py#L72
  - https://code.djangoproject.com/ticket/35387
  - https://github.com/django/django/pull/18083/

Fixes:
- update spatialite to 5.1.0
- recompile SQLite with `-DSQLITE_ALLOW_ROWID_IN_VIEW`
-
