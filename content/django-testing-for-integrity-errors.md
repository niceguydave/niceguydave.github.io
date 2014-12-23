Title: Django - testing model methods
Date: 2014-04-25 09:10
Author: niceguydave
Category: Web development
Tags: django, testing
Slug: django-testing-for-integrity-errors

I recently stumbled upon a "gotcha" which may help someone else testing
Django model methods.

An overview: I recently found myself in a situation where I needed to
ensure that the `slug` field on a model was unique.

A simplification of the model is as follows:

[code language="python"]  
from django.db import models

class Foo(models.Model):  
name = models.CharField(max\_length=100)  
slug = models.SlugField(unique=True)  
[/code]

In terms of how to test this change to the model, my initial thoughts
were that things should be fairly simple: create an object with a
specific `slug` and then create another object with the same `slug`,
expecting an `IntegrityError` to be raised. As such, my approach was to
write the following:

[code language="python"]  
from django.db import IntegrityError  
from django.test import TestCase  
from .models import Foo

class FooModelTest(TestCase):

def test\_unique\_slug(self):  
&quot;&quot;&quot;A slug should be unique.  
&quot;&quot;&quot;  
f1 = Foo(name=&quot;Foo1&quot;, slug=&quot;foo1&quot;)  
f1.save()  
f2 = Foo(name=&quot;Foo2&quot;, slug=&quot;foo1&quot;)  
self.assertRaises(IntegrityError, f2.save())  
[/code]

However, rather than checking that the `IntegrityError` was being raised
was being raised, the `IntegrityError` was called before the test could
run.

What had happened was that, rather than passing the `save` method itself
to `self.assertRaises` I was calling `save()` directly: an
`IntegrityError` was being raised before the test had even been run,
rather than having the test itself check the `save` method in the
assertion.

To fix this, I removed the parentheses from `f2.save()` i.e.

[code language="python"]  
...  
self.assertRaises(IntegrityError, f2.save)  
[/code]

then everything works exactly as expected.
