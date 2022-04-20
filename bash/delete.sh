#!/bin/bash

delete_between () {
    sed -i "/${2}/,/${3}/ d" $1
}