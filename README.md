# schema.gsd.id

schema.gsd.id is generated from https://github.com/cloudsecurityalliance/schema.gsd.id via CloudFlare pages and the make)index.py script that genewrates all the index.html files.

## File names and layout

For humans we have the files with the version number embedded, e.g.: gsd.id/osv-gsd/schema-osv-gsd-1.0.1.json

For computers we have the files in directories with the version number, e.g.: gsd.id/osv-gsd/1.0.1/schema.json

The latest version of the schema is in the root directory and called schema.json, e.g.: gsd.id/osv-gsd/schema.json

The file $id for versioned copies of the file will point at the machine readable URL (e.g.: gsd.id/osv-gsd/1.0.1/schema.json), humans can easily use that and manually look at things to
discover what else there is, this also preserves the version that was used.

The file $id for the "CURRENT" version will point at itself (e.g.: gsd.id/osv-gsd/schema.json), the expectation is if you're using CURRENT, you stay CURRENT.
