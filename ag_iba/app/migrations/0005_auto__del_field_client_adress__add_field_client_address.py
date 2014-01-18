# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Client.adress'
        db.delete_column(u'app_client', 'adress')

        # Adding field 'Client.address'
        db.add_column(u'app_client', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=160),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Client.adress'
        db.add_column(u'app_client', 'adress',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=160),
                      keep_default=False)

        # Deleting field 'Client.address'
        db.delete_column(u'app_client', 'address')


    models = {
        u'app.client': {
            'Meta': {'object_name': 'Client'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'from_home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'nif': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'postal': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'app.tax': {
            'Meta': {'object_name': 'Tax'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Client']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 18, 0, 0)'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plate': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'plate_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['app']