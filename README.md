# Lightbase

![img](https://raw.githubusercontent.com/TheFloatingString/lightbase/main/static/img/Lightbase%20Cover.png)

Lightbase is an abstract, low-cost database library built on peer-to-peer networks. To simplify operations with databases, Lightbase is built to be:

+ **Affordable**: as low-cost as possible leveraging peer-to-peer databases.
+ **Frictionless**: fast and easy for developers to use. Built on REST API (minimal dependencies required) and HTTP-inspired calls.
+ **Unique**: unique items that can be accessed across different databases.

Lightbase is currently built on [IPFS](https://ipfs.tech).

Feel free to create an issue for feature requests.

### Running IPFS

Installing `ipfs` on Linux for [terminal](https://docs.ipfs.tech/install/command-line/):

```bash
wget https://dist.ipfs.tech/kubo/v0.28.0/kubo_v0.28.0_linux-amd64.tar.gz
tar -xvzf kubo_v0.28.0_linux-amd64.tar.gz
cd kubo
sudo bash install.sh
```

In this project's root folder:

```bash
ipfs init
ipfs daemon
```

### Running the Backend

```bash
cd backend
pip install -r requirements.txt
fastapi dev main.py
```

Read:

```bash
curl -XGET localhost:8000/read/<ipfs_hash>
```

Write:

```bash
curl -XPOST localhost:8000/create -H "Content-Type: application/json" -d "{\"data\":\"<Attachment string>\"}"
```

Web app view at [localhost:8000/view](localhost:8000/view).

