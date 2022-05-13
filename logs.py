#!/usr/bin/env python3

import os
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# BOILERPLATE
# TODO: user função
# TODO user lib (loguru)
# nossa instancia
log = logging.Logger(__name__, log_level)
# level
ch = logging.StreamHandler() # Console Handler
ch.setLevel(logging.DEBUG)
# formatacao
fmt = logging.Formatter(
    "%(asctime)s %(name)s $(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

"""
# logging # root logger // logging levels
log.debug("[DEBUG] Mensagem pro dev, qa, sysadmin")
log.info("[INFO] Mensagem geral para usuario")
log.warning("[WARNING] Aviso que nao causa erro")
log.error("[ERROR] Erro que afeta uma unica execucao")
log.critical("[CRITICAL] Erro geral ex: banco de dados inalcancavel")
"""

try:
    1/0
except ZeroDivisionError as e:
    log.error("[Err] Deu erro %s", str(e))
    # stdout
    # stderr
