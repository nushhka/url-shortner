# URL Shortener Microservice 🚀

A lightweight and efficient URL shortener microservice built using **Flask** and **SQLite**, deployed on **Alpine Linux** virtual machines.

## Features
✅ Shorten long URLs into compact, shareable links  
✅ Redirect short URLs to their original destinations  
✅ Persistent URL storage using SQLite  
✅ Lightweight and fast, ideal for microservices  

---

## Installation & Setup  

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/nushhka/url-shortner.git
cd url-shortner
```

### 2️⃣ Create & Activate a Virtual Environment
```sh
python3 -m venv myenv
source myenv/bin/activate  # For Linux/macOS
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Initialize the Database
```sh
python3 init_db.py
```

### 5️⃣ Run the Server
```sh
python3 app.py
By default, it runs on http://0.0.0.0:5000/.
```

## API Endpoints

### 🔹 Shorten a URL
- **Endpoint:** `/shorten`
- **Method:** `POST`
- **Payload (JSON):**
  ```json
  { "url": "https://example.com" }
  ```
- **Response (JSON):**
  ```json
  { "short_url": "http://<VM1-IP>/abc123" }
  ```

### 🔹 Redirect to Original URL
- **Endpoint:** `/<short_key>`
- **Method:** `GET`
- **Example:** Visiting `http://<VM1-IP>/abc123` redirects to `https://example.com`.

---

## Deployment on Alpine Linux VMs

### 🔹 On VM1 (API Service)
1. Install Python and SQLite:
   ```sh
   apk add python3 py3-pip sqlite
   ```
2. Follow the **Installation & Setup** steps above.

### 🔹 On VM2 (Reverse Proxy with Nginx)
1. Install Nginx:
   ```sh
   apk add nginx
   ```
2. Configure `nginx.conf` to route traffic to **VM1**.

