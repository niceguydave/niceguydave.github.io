Title: Resetting a Django app managed by South
Date: 2014-10-04 10:40
Author: niceguydave
Category: Web development
Tags: django, south
Slug: resetting-a-django-app-managed-by-south

I'm currently working on a Django 1.6 project. The project is still in
the early phases of development and I have the luxury of being able to
be fairly destructive when it comes to dropping models and repopulating
data etc.

Before too long, however, I'll have to start doing some deployment for
client approval, so I already have the app I'm working on hooked up to
[South](http://south.readthedocs.org/en/latest/tutorial/part1.html) as a
way of controlling schema and data migrations. I tend not to like using
migrations too much in the early stages of development, purely because
I'm potentially still 'playing around' at this stage, rather than
committing planned changes.

Now that I'm hooked into using South, simply dropping things and
starting again is a little more involved. What this post does is explain
how I drop an app which uses South and recreate again. For this example,
I'll assume that I'm working on an app called `blog` using a postgres
database called `website_db`.

1.  First of all, I reset the migrations for the `blog` app to zero:
    `./manage.py migrate blog zero` What this does is remove any
    reference to the `blog` app from the south migration database table,
    forcing an migration to look into the files within the migrations
    folder in my `blog` app.
2.  Now I drop any database tables referred to by the blog app by piping
    the sqlclear command to the psql command:
    `./manage.py sqlclear blog | psql website_db`. This physically drops
    all database tables related to this app. *Warning: all your data
    will be lost when you do this!*
3.  The next steps is to entirely remove the migrations folder from the
    `blog` app to prepare the way for refreshing things in the next
    step: `rm -rf blog/migrations/`. We are now effectively back at a
    'blank page' with regards to this app.
4.  To hook the app back up again to South, I now convert the blog app
    to South (any changes to the schema etc. would ideally be done
    before this stage. I convert my app to South by running:
    `./manage.py convert_to_south blog`. This command builds the schema
    migration into the `blog/migrations` folder.
5.  Now I run the migration: `./manage.py migrate blog`.

Obviously, there is now no data in this app so my next step is run a
data population script. I'll outline the way I do this in a future post.

I know that nothing of what I've written above is new in any way; I
thought it would simply be useful to lay out my process in a clear way.
Hopefully it may help someone out.
