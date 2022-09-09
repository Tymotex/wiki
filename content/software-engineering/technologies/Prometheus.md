---
title: Prometheus
description: Prometheus
---

![[software-engineering/technologies/assets/prometheus-wallpaper.png|700]]

[Prometheus](https://prometheus.io/) is an open-source real-time monitoring and alerting tool. It's commonly combined with Grafana to make a nice dashboard UI available for us to quickly understand a software system's metrics.





It's a popular choice for monitoring [[software-engineering/technologies/Kubernetes|Kubernetes]] clusters, Linux servers, 

Prometheus pulls data from services

Use cases:
- Traffic.
- Errors.
- Checking SLAs are met.


Popular programming languages have a Prometheus client library that lets you track and expose metrics.


## Architecture

Prometheus has its own custom database for storing real-time metrics.

PromQL is a language for querying metrics from the database, useful for extracting insights.

## Deployment
Pull the [Prometheus Docker image](https://hub.docker.com/r/prom/prometheus) and set up the YAML config.
