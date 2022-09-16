---
title: Prometheus
description: Prometheus
---

![[Knowledge/Engineering/Technologies/assets/prometheus-wallpaper.png|700]]

[Prometheus](https://prometheus.io/) is an open-source real-time monitoring and alerting tool. It's a popular choice for monitoring [[Knowledge/Engineering/Technologies/Kubernetes|Kubernetes]] clusters, Linux servers, Raspberry Pis, etc. It's commonly combined with [[Knowledge/Engineering/Technologies/Grafana|Grafana]] to make a nice dashboard UI available for us to quickly understand a software system's metrics.



Popular programming languages have a Prometheus client library that lets you track and expose metrics.


## Architecture

### Exporters

A **target** is a service that exposes metrics in a format Prometheus knows how to work with. A Prometheus server pulls (also called 'scrapes') data from targets. Targets you might be interested in monitoring include:
- Linux VM running in the cloud.
- Kubernetes cluster.
- Your Raspberry Pi.
- ... and so on.

An **exporter** is what lets you map metrics collected from a system into Prometheus data. It also starts a web server exposing the path `/metrics` that can be scraped.

There are 100+ exporters ([official docs](https://prometheus.io/docs/instrumenting/exporters/)).


Prometheus uses an HTTP pull model where a Prometheus server sends an HTTP request to a dedicated endpoint exposed by target services to pull metrics from them.

Prometheus has its own custom database for storing real-time metrics.

PromQL is a language for querying metrics from the database, useful for extracting insights.

## Configuration

- Retention time — the time that metric datapoints stick around before being discarded (to save space).

## Deployment
Pull the [Prometheus Docker image](https://hub.docker.com/r/prom/prometheus) and set up the YAML config.

## AlertManager
