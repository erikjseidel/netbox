
Fork of the Netbox Community project [1] for the SaltStack SoT integration PoC

Based on 3.5 with select incremental changes pulled in from 3.5.1 and 3.5.2.

## The primary customizations

(1) A Virtual Link model - similar to Wireless Link - to map connections between Virtual Interfaces

(2) The addition of several Virtual Interface types

(3) Allow virtual interface types to be parents of other interfaces

(4) Additional Graphql Mixin to allow easier querying of L2VPN relations from interface endpoints

## Getting Started

This project can be used with the Netbox Docker project [2] to create a container with the customized Netbox version.

Follow the instruction there [2] with the following slight modifications:

(1) Make sure your docker-compose.yaml file is modified to use the locally built docker image rather than pulling from the official Netbox repo, e.g. change the relevant line:
```
...
    image: netboxcommunity/netbox:latest
...
```
(2) You can then build the new containers using the following command:

```
SRC_ORG=erikjseidel SRC_REPO=netbox ./build.sh master
```
Once the containers are up it can be used normally per instructions found in the Netbox Docker project.

[1] https://github.com/netbox-community/netbox

[2] https://github.com/netbox-community/netbox-docker 
