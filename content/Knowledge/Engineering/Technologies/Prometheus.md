---
title: Prometheus
description: Prometheus
---

![[Knowledge/Engineering/Technologies/assets/prometheus-wallpaper.png|700]]

[Prometheus](https://prometheus.io/) is an open-source real-time monitoring and alerting tool. It's a popular choice for monitoring [[Knowledge/Engineering/Technologies/Kubernetes|Kubernetes]] clusters, Linux servers, Raspberry Pis, etc. It's commonly combined with [[Knowledge/Engineering/Technologies/Grafana|Grafana]] to make a nice dashboard UI available for us to quickly understand a software system's metrics.

Popular programming languages have a Prometheus client library that lets you track and expose metrics.

## Usage
### Installing Prometheus Server
```sh
# Download a precompiled binary from https://prometheus.io/download/.
wget https://github.com/prometheus/prometheus/releases/download/v2.38.0/prometheus-2.38.0.linux-amd64.tar.gz
tar -xvf prometheus-*.tar.gz

# Run prometheus server.
# View the default dashboard at localhost:9090.
cd prometheus-*
./prometheus
```
Downloading a precompiled binary is the [recommended installation method](https://github.com/prometheus/prometheus#install). Alternatively, you could build directly from source or pull the Docker image and run the Prometheus server in a container with: `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`.

### Installing Node Exporter
A node in this context is basically just a virtual machine. The node_exporter binary is something you can run on a machine whose resources you want to monitor.
```sh
# Download a precompiled binary from https://prometheus.io/download/#node_exporter.
wget https://github.com/prometheus/node_exporter/releases/download/v1.4.0-rc.0/node_exporter-1.4.0-rc.0.linux-amd64.tar.gz  
tar -xvf node_exporter-*.tar.gz

# Run node exporter (which also runs a web server that presents some output viewable at localhost:9100).
cd node_exporter-*
./node_exporter
```

## Architecture
![[Knowledge/Engineering/Technologies/assets/prometheus-architecture.png|800]]
([official source](https://github.com/prometheus/prometheus))

In the above diagram, a machine running a [[Knowledge/Engineering/Technologies/Prometheus#Installing Prometheus Server|prometheus server]] does the following:
1. Finds the targets it's meant to pull metrics from.
2. Pulls metrics from **exporters** and possibly other prometheus servers.
3. Makes the metrics available for a client (such as Grafana) to consume via **PromQL**.
4. Pushes alerts to you based on thresholds/conditions you set, using **AlertManager**.

A **target** is a service that exposes metrics in a format Prometheus knows how to work with. A Prometheus server pulls (also called 'scrapes') data from targets. Targets you might be interested in monitoring include:
- Linux VM running in the cloud.
- Kubernetes cluster.
- Your Raspberry Pi.
- ... and so on.

An **exporter** is what lets you map metrics collected from a system into Prometheus data. It also starts a web server exposing the path `/metrics` that can be scraped.
- There are 100+ exporters ([official docs](https://prometheus.io/docs/instrumenting/exporters/)).

Prometheus uses an HTTP pull model where a Prometheus server sends an HTTP request to a dedicated endpoint exposed by target services to pull metrics from them.

Prometheus has its own custom database for storing real-time metrics.

PromQL is a language for querying metrics from the database, useful for extracting insights.

## Configuration

- Retention time — the time that metric datapoints stick around before being discarded (to save space).

## Deployment
Pull the [Prometheus Docker image](https://hub.docker.com/r/prom/prometheus) and set up the YAML config.

## AlertManager
