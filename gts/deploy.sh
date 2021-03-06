#!/usr/bin/env bash
# vim: et ts=4 sw=4 ai


CODEDIR=/data/www/gts
STATICDIR=/var/gtsforum.xyz/static

rm -r "$CODEDIR" 

mkdir -pv "$CODEDIR"

cp -rvf gts/ "$CODEDIR"
cp -rvf diskusia/ "$CODEDIR"
find "$CODEDIR" -name '*.pyc' -exec rm -v {} \;
find "$CODEDIR" -name '*~' -exec rm -v {} \;
chown -Rv www-data:www-data "$CODEDIR"
chmod -v -R u=rX,g=,o= "$CODEDIR"
find  "$CODEDIR" -type d -exec chmod -v u+w {} \;

mkdir -pv "$STATICDIR"
rm -r "$STATICDIR"
mkdir -pv "$STATICDIR"
DJANGO_SETTINGS_MODULE=gts.settings_deploy ./manage.py collectstatic --no-input
