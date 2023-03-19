#!/bin/sh

sudo ddcutil  getvcp 10 | grep -o -P '\d*,' | grep -Eo '[0-9]' | tr -d '\n'