# Modelio CI

## Test
To run test, you also need to mount the modelio project and the test scripts to the container.

As example, let's assume we have a directory `/docker/modelio` on host, which contains a project folder called `EmergencyExitRos` as well as a test script `launchGeneration.py`. In this case, you can run your container like this:

```bash
docker run --name modelio -v /docker/modelio:/modelio modelio_image
```

Then the Dockerfile command (CMD) would create a virtual display with Xvfb and then generate files according to the project setting
