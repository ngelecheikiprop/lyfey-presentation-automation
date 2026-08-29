# vJunos GNS3 Access Setup

## 1. Create TAP interface on Linux

```bash
sudo ip tuntap add dev tap0 mode tap user $USER
sudo ip addr add 10.100.100.1/24 dev tap0
sudo ip link set tap0 up
```

Check:

```bash
ip addr show tap0
```

## 2. Connect GNS3

In GNS3:

```text
Cloud tap0  --->  vJunos ge-0/0/0
```

Use the correct vJunos adapter for `ge-0/0/0`.

## 3. Configure vJunos interface

```text
configure

set interfaces ge-0/0/0 unit 0 family inet address 10.100.100.2/24
```

## 4. Configure user and SSH

```text
set system root-authentication plain-text-password

set system login user lab class super-user
set system login user lab authentication plain-text-password

set system services ssh
```

## 5. Configure NETCONF

```text
set system services netconf ssh
```

NETCONF uses port:

```text
830
```

## 6. Configure REST API

```text
set system services rest http port 3000
set system services rest enable-explorer
```

Commit:

```text
commit
```

## 7. Check configuration

```text
show configuration system services
show interfaces terse ge-0/0/0
```

The interface should show:

```text
ge-0/0/0    up    up
```

## 8. Test from Linux

Ping:

```bash
ping 192.168.100.2
```

SSH:

```bash
ssh lab@192.168.100.2
```

Test NETCONF:

```bash
nc -zv 192.168.100.2 830
```

## 9. Open REST API Explorer

Open in a browser:

```text
http://192.168.100.2:3000
```

Example RPC:

```text
http://192.168.100.2:3000/rpc/get-interface-information
```

## After restarting Linux

Bring `tap0` back up and restore the IP:

```bash
sudo ip link set tap0 up
sudo ip addr add 192.168.100.1/24 dev tap0
```
