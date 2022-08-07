---
title: NGINX
description: NGINX
---

![[software-engineering/technologies/assets/nginx-wallpaper.png|800]]

NGINX is a production-grade web server that sits between the external web and your backend infrastructure. It can be configured to be a [[software-engineering/concepts/architecture/Load Balancer|load balancer]], [[software-engineering/concepts/architecture/Reverse Proxy|reverse proxy]], HTTP cache, and more.

> This page assumes that NGINX is installed on a Linux machine.

## Directives
Nginx configuration files contain a custom language consisting of *directives*. See the [list of all directives](https://nginx.org/en/docs/dirindex.html). Directives can reference *variables*. See the [list of all variables](https://nginx.org/en/docs/varindex.html).

- `/etc/nginx/nginx.conf`

### LetsEncrypt Sysadmin
Renew SSL certificates:
```bash
sudo certbot --nginx -d example.com -d www.example.com
```
