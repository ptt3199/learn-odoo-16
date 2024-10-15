# learn-odoo-16
Run the app:
```bash
./odoo-bin --addons-path=./addons,./custom -c ./odoo.conf
```
Add params to update the database:
```bash
./odoo-bin --addons-path=./addons,./custom -c ./odoo.conf -d odoo -u om_hospital
```

User: admin/admin

1. Install extension: Odoo IDE for enabling type hinting
2. odoo.conf:
```
[options]
addons_path = /home/ptt/odoo/odoo/addons,/home/ptt/odoo/odoo/custom
admin_passwd = 1
db_host = localhost
db_password = 1
db_port = 15432
db_user = odoo
http_port = 8069
dbfilter = ^odoo$
```