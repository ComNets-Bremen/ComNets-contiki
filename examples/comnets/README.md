ComNets apps
============

Contiki commands
----------------

- `make install <appname>.upload` Install appname on all connected nodes
- `make install <appname>.upload MOTES=/dev/ttyUSB0` Install appname at the
  node connected to /dev/ttyUSB0
- `make login` open a serial connection to the node
- ` make login MOTES=/dev/ttyUSB0` Connect to the node connected to
  /dev/ttyUSB0
- `make clean` Remove all install files
- `make install <appname>.upload TARGET=[z1|sky|...]` install app for a
  specific target device
- `make TARGET=z1 savetarget` Set default target device


sender.c and receiver.c
-----------------------

Basic example using RIME. Both apps will show their ids on startup. You have to
insert this id as the destination address on the sender side.


Burn node id
------------

You can burn the nodeid to the Z1 / telosB sensor nodes. This can be done using
the following commands:

    make clean
    make burn-nodeid.upload nodeid=<id>
    make sky-reset
    make login

This id is used for example for the RIME stack.
