# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'app_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('adress', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('local', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('postal', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('nif', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Client'])

        # Adding model 'Tax'
        db.create_table(u'app_tax', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Client'])),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('plate', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('plate_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'app', ['Tax'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'app_client')

        # Deleting model 'Tax'
        db.delete_table(u'app_tax')


    models = {
        u'app.client': {
            'Meta': {'object_name': 'Client'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plate': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'plate_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['app']