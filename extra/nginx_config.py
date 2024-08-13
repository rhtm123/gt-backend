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

    # config_file_path = "/etc/nginx/sites-available/" + project_name
    #shutil.copy(temp_file, sites_available)

    print("Config file created")

    subprocess.run(['/home/rohit/gtbackend/setup.sh', 'create', project_name])
# subprocess.run(['/path/to/your/script.sh', 'reload'])


    # Create a symbolic link to enable the Nginx configuration
    # enable_command = f"sudo ln -s {config_file_path} /etc/nginx/sites-enabled/"
    # #sites_enabled = "/etc/nginx/sites-enabled/"+project_name
    # # os.symlink(sites_available, sites_enabled)
    # run_process(f"cp /home/rohit/gtbackend/temp/{project_name} /etc/nginx/sites-available/", "/home/rohit/gtbackend/temp/outcome7.txt")
    # run_process( enable_command, "/home/rohit/gtbackend/temp/outcome5.txt")
    print("Symbolic link created")
    # subprocess.run(enable_command, shell=True, check=True)

def delete_nginx_config(project_name):
    # Remove the symbolic link to disable the Nginx configuration
    disable_command = f"rm /etc/nginx/sites-enabled/{project_name}"
    #site_enabled_file = f"/etc/nginx/sites-enabled/{project_name}"
    #os.remove(site_enabled_file)

    run_process(disable_command, "/home/rohit/gtbackend/temp/outcome3.txt")
    
    # Delete the configuration file
    config_file_path = f"/etc/nginx/sites-available/{project_name}"
    #os.remove(config_file_path)

    #temp_file = f"/home/rohit/gtbackend/temp/{project_name}"
    #os.remove(temp_file)

    run_process( f"rm {config_file_path}" ,"/home/rohit/gtbackend/temp/outcome4.txt")
    run_process( f"rm /home/rohit/gtbackend/temp/{project_name}" ,"/home/rohit/gtbackend/temp/outcome4.txt")
    print("NGINX files deleted")
    # subprocess.run(f"sudo rm {config_file_path}", shell=True, check=True)

def reload_nginx():
    # Test Nginx configuration and reload if it's valid
    # run_process("nginx -t", "/home/rohit/gtbackend/temp/outcome1.txt")
    subprocess.run(['/home/rohit/gtbackend/setup.sh', 'reload'])

    # run_process("systemctl restart nginx", "/home/rohit/gtbackend/temp/outcome2.txt")
    print("nginx reload successful")