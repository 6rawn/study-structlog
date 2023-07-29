import structlog


structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        # structlog.stdlib.add_log_level,
        # structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        # structlog.processors.StackInfoRenderer(),
        # structlog.processors.format_exc_info,
        # structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer(),
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger(__name__)

logger.info("User logged in", user_id="1234", ip="192.168.2.1")
