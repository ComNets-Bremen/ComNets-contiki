CONTIKI = ../..

#CFLAGS += -DPROJECT_CONF_H=\"project-conf.h\"

# Set the channel
CFLAGS += -DRF_CHANNEL=16

all: sender receiver burn-nodeid

CONTIKI_WITH_RIME = 1
include $(CONTIKI)/Makefile.include
