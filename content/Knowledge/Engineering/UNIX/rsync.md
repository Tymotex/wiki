---
title: rsync
---

`rsync` is basically like `cp`, but it can seamlessly copy files/directories between local and remote machines. It's called `rsync` because it can keep filesystems in a remote machine in sync with the local one.

Here's the basic usage. Just like `cp`, the source comes before the destination:
```sh
rsync -avz /foo/bar username@address
```
