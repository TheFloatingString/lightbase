# Lightbase

### Running IPFS

Installing `ipfs` on Linux:

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

Web app view at `localhost:8000/view`.

