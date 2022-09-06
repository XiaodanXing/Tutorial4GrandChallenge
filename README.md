# Tutorial4GrandChallenge
A tutorial of docker submission for grandchallenge.org.

## Required packages
Docker, evalutils

```
evalutils init algorithm myproject
```
To copy the model weights, in the Dockerfile, 
1. change " FROM python:3.9-slim" to " FROM pytorch/pytorch"
2. copy the pth file into the docker filefolder, and in the Dockerfile, add
 ```
 COPY --chown=algorithm:algorithm best.pth /opt/algorithm/
 ```

