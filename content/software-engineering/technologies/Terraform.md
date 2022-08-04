---
title: Terraform
description: Terraform
---

![[software-engineering/technologies/assets/terraform.png|700]]

[Terraform](https://www.terraform.io/) is an *infrastructure as code* technology that you can use to automate your infrastructure setup. All you do is define the things you want to spin up in a `.tf` file, such as [[software-engineering/concepts/devops/Virtual Machines|VMs]], [[software-engineering/concepts/devops/Load Balancer|load balancers]], [[software-engineering/technologies/Kubernetes|K8S clusters]], a [[software-engineering/concepts/devops/VPC|VPC]], etc. using Terraform's [[software-engineering/concepts/programming/Programming Paradigm#Declarative|declarative]] language. Terraform uses your API credentials to spin up everything you declared in the `.tf` file. Terraform has a rich plugin ecosystem and it's usable on all the main [[software-engineering/concepts/cloud/Cloud Provider|cloud providers]].
