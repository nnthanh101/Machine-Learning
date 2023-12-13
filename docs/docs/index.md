# Data-Science documentation!

## Description

🛠 Production-grade project structure for successful data-science or machine-learning projects 🚀

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://analytics101/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://analytics101/data/` to `data/`.


