Students system (AWS-ready)

This setup runs three containers: Postgres, Backend (FastAPI), and Frontend (Nginx + static).
Frontend proxies /api to the backend, so you only need to open port 80 on the EC2 instance.

How to run locally with Docker Compose (for dev):
  docker compose up --build

How to deploy on an AWS EC2 instance:
  1. Create an EC2 (Amazon Linux 2) and open Security Group ports: 22 (SSH) and 80 (HTTP).
  2. Convert your .pem to .ppk with PuTTYgen if on Windows.
  3. Connect via PuTTY as ec2-user@<EC2_IP> using the .ppk key.
  4. Install Docker and Docker Compose on the instance (commands below).
  5. Upload project folder to /home/ec2-user (with WinSCP or git clone).
  6. In the project folder run: docker compose up --build -d
  7. Open in browser: http://<EC2_IP> (the frontend on port 80).

Install Docker & Docker Compose (Amazon Linux 2):
  sudo yum update -y
  sudo amazon-linux-extras install docker -y
  sudo service docker start
  sudo usermod -a -G docker ec2-user
  # log out and back in so group change applies
  # Install docker-compose (standalone binary)
  sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  # now you can use: docker-compose or docker compose

Notes:
 - In this configuration Postgres is NOT exposed to the public internet (no host port mapping).
 - Frontend proxies "/api" to the backend, so all API calls are same-origin and no CORS headaches.
 - Data persists using docker volume 'postgres_data'.
