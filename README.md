# Dynamic Forward Proxy #

## Summary ##
This repo is an example of a dynamic forward proxy with NGINX. When running, it will use part of the URL to direct you to the server you want. This sort of approach helps for 2 main reasons:

1. In NGINX, when using a hardcoded *proxy_pass*, the host must be alive or NGINX will also fail, leaving all the other services without a proxy.
2. If you add and remove services, you can have them behind the same NGINX server without having to change the config or restart the proxy.

In my repo you will find the following services:

- A math service (takes a number as 'n' then performs a simple operation)
- A string service (takes a string 'string' then performs a simple string operation)
- NGINX

## Running the example ##

Prerequisites:

- Docker

To run this example, execute the following command

```sh
docker-compose up --build
```

When it is up and running you will be able to get to the services via the following **http://localhost:8080/services/{service}/{function}** where service is the docker service of the API (i.e. math) and the function is the API route (i.e. double). Using these parameters the URL would look like this

> [http://localhost:8080/services/math/double?n=5](http://localhost:8080/services/math/double?n=5_)

To stop the services running you are able to run the following command:

```sh
docker-compose down --remove-orphans
```