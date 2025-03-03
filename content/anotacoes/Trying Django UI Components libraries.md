---
title: Trying Django UI Components libraries
date: 2025-02-28
lastmod: 2025-03-03
---

Options: https://toolbox.cezimbra.me/lists/django-web-components/

| Project              | First release | Component definition                  | Component usage                                      | Scoped CSS       | Scoped JS        |
| -------------------- | ------------- | ------------------------------------- | ---------------------------------------------------- | ---------------- | ---------------- |
| django-bird          | 2024-09-25    | HTML template in `templates/bird/`    | Django template tag for now, HTML tag in the roadmap | Roadmap          | Roadmap          |
| django-cotton        | 2024-06-08    | HTML template in `templates/cotton/`  | HTML tag `<c-my-component />`                        | ❌               | ❌               |
| dj-angles            | 2024-10-26    | HTML template used as `{% include %}` | HTML tag `<dj-my-component />`                       | Using Shadow DOM | Using Shadow DOM |
| django-viewcomponent | 2024-03-12    | Python class + HTML template          | Custom Django template tag `{% component ... %}`     | ❌               | ❌               |


## django-template-partials
- https://github.com/carltongibson/django-template-partials

## django-components
- https://github.com/django-components/django-components


## Archived/unmaintained projects
- [django-sockpuppet](https://github.com/jonathan-s/django-sockpuppet) last
  commit was in 2021.
- [reactor](https://github.com/edelvalle/reactor) last commit was in 2023 and
  it was a Phoenix LiveView like lib.
- [slippers](https://github.com/mixxorz/slippers) last commit was in 2023.
- [django-web-components](https://github.com/xzya/django-web-components) last
  commit was in Feb 2024; requires to define a Python class for each component,
  which looks annoying:
    ```python
    from django_web_components import component

    @component.register("card")
    class Card(component.Component):
        template_name = "components/card.html"
    ```


## Honorable mentions
- [django-unicorn](https://github.com/adamghill/django-unicorn) is a reactive
  component framework. It's way bigger than only UI components.
- [django-htmx-components](https://github.com/iwanalabs/django-htmx-components)
  is a collection of components for Django and HTMX meant to be copy-pasted
  into your project.
