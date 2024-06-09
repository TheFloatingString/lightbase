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

