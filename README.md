# simple-Python-HTTP-server-sample
### Requirements  
Python libraries: (pip installation)  
```
flask
gunicorn
gevent
```  
Install from source code: (manual compilation)
```
Nginx
```  
System environment:
```
macOS Monterey v12.1
Python 3.8.12 (Clang 10.0.0)
```
### After Installation
* Replace the default Nginx configuration file `/usr/local/nginx/conf/nginx.conf` with the one in folder
* Modify hosts file `/private/etc/hosts`, add line that maps the server name ("myworld.com") to localhost (or your address in the network)
### Notes
Gunicorn does not work on Windows systems properly (many missing modules)!