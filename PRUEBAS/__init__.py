import logging as log

# Los distintos tipos de controles de error que veremos en este módulo son:
# Trace  (van dejando de menos a más traza)
# Debug
# Info
# Warning
# Error
# Critical

log.basicConfig(level=log.DEBUG)

log.trace("Esto es un error TRACE de prueba")
log.debug("Esto es un error DEBUG de prueba")
log.info("Esto es un error INFO de prueba")
log.warning("Esto es un error WARNING de prueba")
log.error("Esto es un error ERROR de prueba")
log.critical("Esto es un error CRITICAL de prueba")