---
title: "Django"
date: 2024-04-16
lastmod: 2024-10-11
---

- [Snippet - Django password hashers time comparison](https://gist.github.com/lucasrcezimbra/69286c9f1cbdb355e242990d2bc85e02)
- [OWASP - Django Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html)
- [Ninja](https://github.com/vitalik/django-ninja)
	- Fields selections [Issue](https://github.com/vitalik/django-ninja/issues/333)
- [Scaffold](https://github.com/Abdenasser/dr_scaffold)
- Avoid overwriting Model.delete. For example, overwriting to ensure soft delete (idea from [django-tenant-users](https://github.com/Corvia/django-tenant-users/blob/933c87dbad920d2c75666429ef37a552b15e9ac6/tenant_users/tenants/models.py#L404C1-L411C1)):
	```python
	def delete(self, *args, hard=False, **kwargs):
		if not hard:
			raise DeleteError("Use Model.soft_delete()")
		super().delete(*args, **kwargs)ht
	```
- `django.core.exceptions.ImproperlyConfigured: Cannot import '<app>'. Check that '<project>.<app>.apps.<App>Config.name' is correct.` #troubleshooting
	- Rename `<App>Config.name` from `<app>` to `<project>.<app>`
- [How to Switch to a Custom Django User Model Mid-Project](https://www.caktusgroup.com/blog/2019/04/26/how-switch-custom-django-user-model-mid-project/) and [Document how to migrate from a built-in User model to a custom User model](https://code.djangoproject.com/ticket/25313#comment:24)

## Natural Key example
```diff
+class MyModelManager(models.Manager):
+    def get_by_natural_key(self, field1, field2):
+        return self.get(field1=field1, field2=field2)
+
+
 class MyModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     field1 = models.CharField(max_length=254)
     field2 = models.CharField(max_length=254)
+
+    objects = MyModelManager()
+
+    def natural_key(self):
+        return (self.field1, self.field2)
```

## Testing
### Unmanaged models
- [Source](https://stackoverflow.com/a/72593718)

```python
# conftest.py
def pytest_sessionstart():
    from django.apps import apps

    unmanaged_models = [m for m in apps.get_models() if not m._meta.managed]

    for m in unmanaged_models:
        m._meta.managed = True

# pyproject.toml
[tool.pytest.ini_options]
addopts = "--no-migrations"
```

### Defining a conftest shared between all apps
The `conftest.py` must be in the same directory of `manage.py`.


## `virtual_only` fields
- Advantages: 1. Improved performance; 2. Consistent interface; 3. Compatibility with Django’s ORM; 4. Integration with serialization.
- from https://henriquebastos.net/how-chatgpt-quickly-helped-me-understand-djangos-source-code


## Multi-tenancy
- django-tenants - [GitHub](https://github.com/django-tenants/django-tenants/)
	- Examples of projects using it: [bakeup](https://github.com/bruecksen/bakeup), [Zango](https://github.com/Healthlane-Technologies/Zango), [authentik](https://github.com/goauthentik/authentik/), [koku](https://github.com/project-koku/koku)
	- django-tenant-users - [GitHub]
		- Examples: [RPGnotes](https://github.com/Findus23/RPGnotes)

## Toolbox
### Admin
Moved to My Toolbox - [Django - Admin](https://toolbox.cezimbra.me/lists/django-admin/)

### Auth
Moved to My Toolbox - [Django - Auth](https://toolbox.cezimbra.me/lists/django-auth/)

### GraphQL Server
Moved to My Toolbox - [Django - GraphQL](https://toolbox.cezimbra.me/lists/django-graphql/)

### Health Check
Moved to My Toolbox - [Django - Healthcheck](https://toolbox.cezimbra.me/lists/django-healthcheck/)

### Servers
Moved to My Toolbox - [Django - Servers](https://toolbox.cezimbra.me/lists/django-servers/)

### Tree structures
Moved to My Toolbox - [Django - Saving Trees](http://localhost:8000/lists/django-saving-trees/)
