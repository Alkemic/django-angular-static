# Django Angular Static
AngularJS (1.2, 1.3, 1.4) static files collection for Django

## Installation

To install this package, juz run:
```bash
$ pip install git+https://github.com/Alkemic/django-angular-static.git
```
After that, add `'angular',` to yours `INSTALLED_APPS` in `settings.py`, after the `'django.contrib.staticfiles',` app, just like this:
```python
INSTALLED_APPS = (
    # ...

    'django.contrib.staticfiles',
    'angular',

    # ...
)
```

And collect static files

```bash
$ ./manage.py collectstatic
```

**Don't forget** to [proper setup](https://docs.djangoproject.com/en/dev/howto/static-files/) your static app!

## Usage
Within your template file ``load staticfiles`` templatetags and using `static` tempalte tag make full path to file.
```html
{% load staticfiles %}
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="{% static "angular/1.4/angular.js" %}"></script>
    <script src="{% static "angular/1.4/angular-sanitize.js" %}"></script>
</head>
<body>
</body>
</html>
```

## TODO
* Scrip for automated checking and adding new versions of AngularJS
