FROM ubuntu:16.04

MAINTAINER komad

ENV REFRESHED_AT 2016-03-05

ENV DEBIAN_FRONTEND noninteractive

ENV AFL_INSTALL http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz
ENV LIBJPEG_TURBO_INSTALL https://github.com/ImageMagick/ImageMagick.git

# Update and install minimal.
#
# afl:
#   build-essential, wget
#
# lidjpeg-turbo:
#   autoconf, automake, build-essential, libtool, nasm,
#   subversion, wget

RUN \
    apt-get update \
        --quiet \
    && apt-get install \
        --yes \
        --no-install-recommends \
        --no-install-suggests \
    autoconf \
    automake \
    gcc \
    libtool \
    make \
    nasm \
    wget \
    git\
    ca-certificates \

# Clean up packages.
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Get ready to build.
WORKDIR /tmp

# Get and build AFL.
RUN \
    wget \
    $AFL_INSTALL \
        --no-verbose \
    && mkdir afl-src \
    && tar -xzf afl-latest.tgz \
        -C \
        afl-src \
        --strip-components=1 \
    && cd afl-src \
    && sed -i 's/^\/\/ #define USE_64BIT/#define USE_64BIT/gI' config.h \
    && make \
    && make install \
    && rm -rf \
        /tmp/afl-latest.tgz \
        /tmp/afl-src


        

RUN \
    git clone https://github.com/ImageMagick/ImageMagick.git \
    && cd ImageMagick \
    && CC=/usr/local/bin/afl-gcc ./configure \
    && make \
    && make install \

VOLUME ["/data"]

WORKDIR /data

CMD ["bash"]
