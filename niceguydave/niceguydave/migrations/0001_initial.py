# -*- coding: utf-8 -*-
from south.v2 import DataMigration


class Migration(DataMigration):

    def forwards(self, orm):

        from django.contrib.auth.models import User

        User.objects.create_superuser(
            username="admin", email="admin@admin.com",
            password="admin")

        from django.contrib.sites.models import Site
        site = Site.objects.all()[0]
        site.domain = 'http://localhost:8000'
        site.name = 'niceguydave'
        site.save()
        #import pdb; pdb.set_trace()

    def backwards(self, orm):
        pass

    models = {}

    complete_apps = ['niceguydave']
