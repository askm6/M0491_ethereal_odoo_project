FROM odoo:17

COPY ./config /etc/odoo
COPY ./custom_addons /mnt/extra-addons

RUN mkdir -p /mnt/extra-addons

CMD ["sh", "-c", "exec odoo --db_host=$HOST --db_port=$PORT_DB --db_user=$USER_DB --db_password=$PASSWORD_DB --db_sslmode=require --addons-path=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons --http-port=$PORT"]