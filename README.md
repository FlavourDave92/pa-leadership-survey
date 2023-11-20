# pa-leadership-survey (mit Verena)

## nginx config
Note: no self-signed certs on aws possible (certbot) --> only use http and no https. If certs possible, insert them (crt or pem file possible) in the config.

- Add file in `/etc/nginx/sites-enabled`
- Remove the `default` file in the folder


```
map $http_upgrade $connection_upgrade {
    default   upgrade;
    ''        close;
}

server {
    listen 80;
    server_name _;
#     return 301 https://$server_name$request_uri;
# }

# server {
#     listen 443 ssl;
#     server_name _;

#     ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
#     ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Port $server_port;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header        Connection $connection_upgrade;
        proxy_set_header        X-Real-IP $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Host $server_name;
    }
}
```

## example call
http://localhost:8000/link/to/experiment/?participant_label=ProlificKey123


## Todos


## Configurations


## experimental flow
1. introduction

