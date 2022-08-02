#!/bin/bash

set -o errexit

SCRIPTDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

docker build -t 69323/cart --build-arg service_version=v1 "${SCRIPTDIR}"
