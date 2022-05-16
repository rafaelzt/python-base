#!/usr/bin/env python3

import os
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "INFO").upper()

# BOILERPLATE
# TODO: user função
# TODO user lib (loguru)
# nossa instancia
log = logging.Logger(__name__, log_level)
# level
# ch = logging.StreamHandler() # Console/Terminal/stderr Handler
# ch.setLevel(logging.DEBUG)
fh = handlers.RotatingFileHandler("meulog.log", 
                                  maxBytes=300,   # 10**6 -> 1M
                                  backupCount=10 
                                  )
fh.setLevel(logging.DEBUG)

# formatacao
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)

# destino
# log.addHandler(ch)
log.addHandler(fh)

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
