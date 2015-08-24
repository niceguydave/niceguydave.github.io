Title: Django - unexpected behaviour when deleting optional fields
Date: 2015-08-24 11:30
Author: niceguydave
Category: Web development
Tags: django
Slug: unexpected-behaviour-deleting-optional-fields

I've just come out of a situation where data has been deleted from a site
I'm responsible for - I wasn't expecting this to happen when writing the 
schema so I thought it worthwhile adding here in the event that it helps
anyone else who may be in the same situation

The scenario was adding an optional field to to a Django (
FilerImageField [http://django-filer.readthedocs.org/en/latest/usage.html#filerfilefield-and-filerimagefield]).

A simplification of my model is as follows:

[code language="python"]  
from filer.fields.image import FilerImageField
...

class Foo(models.Model):  
    name = models.CharField(max_length=100)      
    image = FilerImageField(null=True, blank=True,
                            help_text='Image should be at least 200 x 100px.')

[/code]

My initial thoughts on this were, "it's an optional field so it shouldn't 
matter whether the `image` instance referred to is deleted from the library.
 
It does.

When deleting anything, the default behaviour of any foreign keys 
['emulates the behavior of the SQL constraint ON DELETE 
CASCADE'](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey.on_delete), 
which is to say, even though an `image` exists in an instance of `Foo`, 
and is optional, the fact that it has a foreign key relationship to the
`FilerImageField` instance means that the `Foo` instance will, be default,
 be deleted.

To resolve this issue, in my case, I changed the `on_delete` attribute for my
`image` field to set the value of `image` to be
[`NULL` (https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.SET_NULL)] 
in the event that the connected `FilerFieldImage` field were deleted.

The code therefore was rewritten to look as follows:

[code language="python"]  
from filer.fields.image import FilerImageField
...

class Foo(models.Model):  
    name = models.CharField(max_length=100)      
    image = FilerImageField(null=True, blank=True,
                            help_text='Image should be at least 200 x 100px.',
                            on_delete=models.SET_NULL)

[/code]
