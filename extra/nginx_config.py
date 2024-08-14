import json
from asgiref.sync import async_to_sync
import subprocess
from django.core.management import call_command


import socket
import sys
import shutil
import os
import time


def run_process(cmd, filename):
    with open(filename, "w") as output:
        print("command- ", cmd, "filename - ", filename)
        password = "gtserver123"
        subprocess.run(f'echo {password} | sudo -S {cmd}', shell=True, stdout=output, stderr=output)

  
def create_nginx_config(subdomain, project_name):
    # Create an Nginx configuration file for the container
    nginx_config = f"""
server {{
    listen 80;
    server_name {subdomain} ;

    location = /favicon.ico {{ access_log off; log_not_found off; }}
    location /static/ {{
        root /home/rohit/gtbackend;
    }}

    location / {{
        include proxy_params;
        proxy_pass http://unix:/home/rohit/gtbackend/gtbackend.sock;
    }}

    error_page 500 502 503 504 /50x.html;
        location = /50x.html {{
            root /usr/share/nginx/html;
        }}
}}
    """
    # Write the configuration to a file
    temp_file = f"/home/rohit/gtbackend/temp/{project_name}"
    with open(temp_file, "w") as config_file:
        config_file.write(nginx_config)

    print("Config file created")

    subprocess.run(['/home/rohit/gtbackend/setup.sh', 'create', project_name])

    print("Symbolic link created")

def delete_nginx_config(project_name):
    print("NGINX files deleted started", project_name)

    subprocess.run(['/home/rohit/gtbackend/setup.sh', 'delete', project_name])

    print("NGINX files deleted")
    # subprocess.run(f"sudo rm {config_file_path}", shell=True, check=True)

def reload_nginx():
    # Test Nginx configuration and reload if it's valid
    subprocess.run(['/home/rohit/gtbackend/setup.sh', 'reload'])

    # run_process("systemctl restart nginx", "/home/rohit/gtbackend/temp/outcome2.txt")
    print("nginx reload successful")