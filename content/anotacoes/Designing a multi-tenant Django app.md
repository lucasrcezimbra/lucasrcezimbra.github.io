---
title: Designing a multi-tenant Django app
date: 2024-11-07
lastmod: 2024-11-12
---

## Setting and getting the tenant
### Thread-Local
[Thread-Local](https://docs.python.org/3/library/threading.html#thread-local-data)
using [asgiref](https://github.com/django/asgiref/) that is a drop-in replacement for
`threading.local` with support to threads and asyncio.

```python
from asgiref.local import Local

local = Local()


def set_tenant(id):
    local.id = id


def get_tenant():
    return getattr(local, "id", None)
```

- Pros
    * Globally available
- Cons



## Marking models as tenant-aware
### Inheritance
[django-multitenant](https://github.com/citusdata/django-multitenant) approach.

```python
# models.py
class TenantModel(models.Model):
    objects = TenantManager()

    class Meta:
        abstract = True


class MyModel(TenantModel):
    pass
```

- Pros
    * more flexibility
- Cons
    * doesn't work well for third party apps
    * the flaws of inheritance


### Settings by apps
[django-tenants](https://github.com/django-tenants/django-tenants/) approach:
https://django-tenants.readthedocs.io/en/latest/install.html#configure-tenant-and-shared-applications

```python
# settings.py
SHARED_APPS = (
    ...
)

TENANT_APPS = (
    # tenant-specific apps
    ...
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]
```

- Pros
    * work for third party apps
- Cons
    * less flexibility


### Settings by models (idea)
Inspired by [Settings by apps]({{< ref "Django#settings-by-apps" >}}).
```python
# settings.py
TENANT_MODELS = (
    'core.MyModel',
    ...
)
```


### Decorator (idea)
Inspired by [attrs](https://github.com/python-attrs/attrs).
```python
@tenant_aware
class MyModel(models.Model):
    objects = models.Manager()
```

- Pros
    * more flexibility
    * no inheritance
- Cons
    * doesn't work well for third party apps



## Applying the tenant
### Manager setting tenant in all queries
Example:
```python
# middleware.py
class TenantMiddleware:
    ...
    def __call__(self, request):
        set_tenant(extract_tenant(request))
        response = self.get_response(request)
        return response


# models.py
class TenantManager(models.Manager):
    def get_queryset(self):
        assert_tenant()
        return super().get_queryset().filter(tenant_id=get_tenant()})


class TenantModel(models.Model):
    objects = TenantManager()
    unsafe_objects = models.Manager()
```

- Pros
    * No need to set the tenant ID in each query.
- Cons
    * Admin doesn't work because it will use `objects` without setting the tenant.
    * Tests will need more setup.


### Manager setting tenant when available
```python
# middleware.py
class TenantMiddleware:
    ...
    def __call__(self, request):
        set_tenant(extract_tenant(request))
        response = self.get_response(request)
        return response


# models.py
class TenantManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()

        if tenant := get_tenant():
            assert_tenant()
            qs = qs.filter(tenant_id=tenant)

        return qs


class TenantModel(models.Model):
    objects = TenantManager()
```

- Pros
    * Works with Django Admin
    * Tests better with tests
- Cons
    * Less secure because some bug could let the query without the tenant.


###


## References
- [Python docs - Thread-Local](https://docs.python.org/3/library/threading.html#thread-local-data)
- [asgiref](https://github.com/django/asgiref/)
- [django-tenants](https://github.com/django-tenants/django-tenants/)
- [django_tenants docs - Configure Tenant and Shared Applications](https://django-tenants.readthedocs.io/en/latest/install.html#configure-tenant-and-shared-applications)
- [attrs](https://github.com/python-attrs/attrs)
- [Why I use attrs instead of pydantic](https://threeofwands.com/why-i-use-attrs-instead-of-pydantic)
- [django-multitenant](https://github.com/citusdata/django-multitenant)
