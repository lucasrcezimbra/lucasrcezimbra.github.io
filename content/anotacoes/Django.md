---
title: "Django"
date: 2024-04-16
lastmod: 2025-07-17
---

- [Snippet - Django password hashers time comparison](https://gist.github.com/lucasrcezimbra/69286c9f1cbdb355e242990d2bc85e02)
- [OWASP - Django Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html)
- [Ninja](https://github.com/vitalik/django-ninja)
	- Fields selections [Issue](https://github.com/vitalik/django-ninja/issues/333)
- [Scaffold](https://github.com/Abdenasser/dr_scaffold)
- Avoid overwriting Model.delete. For example, overwriting to ensure soft
  delete (idea from
  [django-tenant-users](https://github.com/Corvia/django-tenant-users/blob/933c87dbad920d2c75666429ef37a552b15e9ac6/tenant_users/tenants/models.py#L404C1-L411C1)):
	```python
	def delete(self, *args, hard=False, **kwargs):
		if not hard:
			raise DeleteError("Use Model.soft_delete()")
		super().delete(*args, **kwargs)ht
	```
- `django.core.exceptions.ImproperlyConfigured: Cannot import '<app>'. Check that '<project>.<app>.apps.<App>Config.name' is correct.` #troubleshooting
	- Rename `<App>Config.name` from `<app>` to `<project>.<app>`
- [How to Switch to a Custom Django User Model Mid-Project](https://www.caktusgroup.com/blog/2019/04/26/how-switch-custom-django-user-model-mid-project/)
  and [Document how to migrate from a built-in User model to a custom User model](https://code.djangoproject.com/ticket/25313#comment:24)
- [`ForeignKey.on_delete`](https://docs.djangoproject.com/en/5.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)
  is enforced by the ORM not by the database. There is a
  [ticket](https://code.djangoproject.com/ticket/21961) since 2014 to support
  database-level cascading. Related PR:
  [Refs #21961 : Added support for database-level cascading options](https://github.com/django/django/pull/16851)


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


## Template
### Adding a char when the for loop has next element
```
{% for x in tool.lists.all %}
    {{ x }}{% if not forloop.last %},{% endif %}
{% endfor %}
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


### TestCase vs TransactionTestCase
#### TestCase
- is faster than TransactionTestCase
- doesn't commit the changes
- runs each test inside a transaction to provide isolation
- wraps the tests within two nested `atomic()`: 1. whole class; 2. each test.
- doesn't truncate tables after a test. Instead, it encloses the test code in
  a database transaction that is rolled back at the end of the test

References:
[Writing and running tests | Django documentation](https://docs.djangoproject.com/en/5.1/topics/testing/overview/#module-django.test),
[TestCase | Django documentation](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#testcase),
[TestCase | django/django/test/testcases.py](https://github.com/django/django/blob/a060a22ee2dde7aa29a5a29120087c4864887325/django/test/testcases.py#L1362),
[pytest.mark.django_db | pytest-django/pytest_django/fixtures.py](https://github.com/pytest-dev/pytest-django/blob/263ca6d5affdb2af0693042e75a9af81b4497dac/pytest_django/fixtures.py#L173-L214)

#### TransactionTestCase
- resets the database after the test runs by truncating all tables
- may call commit and rollback

References:
[TransactionTestCase | Django documentation](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#django.test.TransactionTestCase),
[TransactionTestCase | django/django/test/testcases.py](https://github.com/django/django/blob/a060a22ee2dde7aa29a5a29120087c4864887325/django/test/testcases.py#L1090),
[pytest.mark.django_db | pytest-django/pytest_django/fixtures.py](https://github.com/pytest-dev/pytest-django/blob/263ca6d5affdb2af0693042e75a9af81b4497dac/pytest_django/fixtures.py#L173-L214)



## `virtual_only` fields
- Advantages: 1. Improved performance; 2. Consistent interface; 3.
  Compatibility with Django’s ORM; 4. Integration with serialization.
- from https://henriquebastos.net/how-chatgpt-quickly-helped-me-understand-djangos-source-code



## Toolbox
Moved to My Toolbox:
- [Django - Admin](https://toolbox.cezimbra.me/lists/django-admin/)
- [Django - Auth](https://toolbox.cezimbra.me/lists/django-auth/)
- [Django - GraphQL](https://toolbox.cezimbra.me/lists/django-graphql/)
- [Django - Healthcheck](https://toolbox.cezimbra.me/lists/django-healthcheck/)
- [Django - Servers](https://toolbox.cezimbra.me/lists/django-servers/)
- [Django - Saving Trees](https://toolbox.cezimbra.me/lists/django-saving-trees/)


### Multi-tenancy
- django-tenants - [GitHub](https://github.com/django-tenants/django-tenants/)
    * separation: multi-schema
    * identifier: subdomain and path-based
	* Examples of projects using it:
      [bakeup](https://github.com/bruecksen/bakeup),
      [Zango](https://github.com/Healthlane-Technologies/Zango),
      [authentik](https://github.com/goauthentik/authentik/),
      [koku](https://github.com/project-koku/koku)
	* django-tenant-users - [GitHub](https://github.com/Corvia/django-tenant-users)
		* Examples: [RPGnotes](https://github.com/Findus23/RPGnotes)
- [django-multitenant](https://github.com/citusdata/django-multitenant)
    * separation: row-based
    * identifier: out of scope
    * depends on PostgreSQL + Citus
