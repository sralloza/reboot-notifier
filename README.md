# Reboot notifier

Sends a message via telegram. Designed to be executed when a server is started or rebooted.

## Docker

```shell
docker buildx build -t sralloza/reboot-notifier:1.0.0 --platform=linux/arm/v7,linux/amd64 --push .
```
