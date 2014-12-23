Title: Enabling native spell checking with Django-CMS 3
Date: 2014-09-22 11:54
Author: niceguydave
Category: Web development
Tags: cms, django, django-cms
Slug: enabling-native-spell-checking-with-django-cms-3

We use Django-CMS extensively at the company I work for,
[Pancentric](http://www.pancentric.com/ "Pancentric"). I was recently
given what, at first, seemed to be a fairly simple request: ensure that
any misspelled words are highlighted within the default text editor.

I'm fairly new to [CKEditor](http://ckeditor.com/ "CKEditor") and
although I'm liking using it so far, there are a certain number of
features which make things... awkward. Spell checking is one of them.

The toolbar has a number of sensible defaults which can be seen in the
image below.  Notice that, although the last three words are misspelled,
there is no visual indication of this.

[caption id="attachment\_136" align="alignnone" width="1008"][![Default
CKEditor
layout](http://niceguydave.files.wordpress.com/2014/09/toolbar_pre_config.png)](http://niceguydave.files.wordpress.com/2014/09/toolbar_pre_config.png)
Default CKEditor layout[/caption]

You'll notice that what I *don't* have here is either a spell-check
button or the ability to see any misspelled words highlighted within the
text editor itself.

After digging around for a while, it seemed that many of the
recommendations for including a spell checker directed me to using a
licensed plugin, something which I didn't want or need; I just wanted to
enable the context menu to highlight misspelled words. Moreover, the
context menu had been hijacked too, which stopped me from right-clicking
on a word to get a context-specific menu.

In the end, after a bit of searching and finding some useful posts about
the same issue (like [this
one](http://murfitt.net/blog/getting-browser-spell-checker-work-ckeditor-drupal)
and [this
one](http://stackoverflow.com/questions/2682042/ckeditor-using-firefox-built-in-spellchecker))
I was able to hack together the following configuration. This sits
within my `settings.py` file and gives a minimal working solution which
allows misspelled words to be highlighted within the text editor and
which doesn't force me to install any additional spell checking plugins:

[code language="python"]  
CKEDITOR\_SETTINGS = {  
'disableNativeSpellChecker': False,  
'removePlugins': 'contextmenu,liststyle,tabletools',  
'toolbar\_CMS': [  
['Undo', 'Redo'],  
['cmsplugins', '-', 'PasteText',],  
['Format', 'NumberedList','BulletedList',],  
['Bold', 'Italic', 'Underline', '-', 'RemoveFormat'],  
['Source', 'ShowBlocks',]  
],  
}  
[/code]

Some notes on what I've done here:

1.  By default, [`disableNativeSpellChecker` is set to
    `True`](http://docs.ckeditor.com/#!/guide/dev_spellcheck), so I
    needed to override this behaviour.
2.  I only actually needed to remove `contextmenu` from the
    `removePlugins` attribute: `liststyle` and `tabletools` depend upon
    `contextmenu`, so they needed to come out, too.
3.  The additional `'toolbar_CMS'` config is not part of the problem
    above but illustrates how I've reduced the number of tool bar items
    to a sensible minimum in the image below

The final appearance of the editor after the changes have been made is
as below.  Notice the final three nonsense words highlighted as
misspelled (I'm using Chrome ):

[caption id="attachment\_135" align="alignnone" width="1008"][![CKEditor
toolbar after configuring native browser spell
checking](http://niceguydave.files.wordpress.com/2014/09/toolbar_post_config.png)](http://niceguydave.files.wordpress.com/2014/09/toolbar_post_config.png)
CKEditor toolbar after configuring native browser spell
checking[/caption]
