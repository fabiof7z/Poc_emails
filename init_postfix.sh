#!/bin/bash

# Defina o nível de compatibilidade do Postfix
postconf compatibility_level=3.6

# Inicie o serviço Postfix em primeiro plano
postfix start-fg
