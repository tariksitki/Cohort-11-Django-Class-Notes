
from .base import *  ## herseyi import et

## sadece dev ile ilgili olan kodlari buraya alip base.py dan siliyoruz. 
## base.py da herseyi getir buradakileri ilave et. 

THIRD_PARTY_APPS = ["debug_toolbar"]
DEBUG = config("DEBUG")
INSTALLED_APPS += THIRD_PARTY_APPS
THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]
## Önemli bu middleware en üstte olmasi lazim ona göre kod yazalim. 
# Database# https://docs.djangoproject.com/en/4.0/ref/settings/#databasesDATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3","NAME": BASE_DIR / "db.sqlite3",    }}
INTERNAL_IPS = ["127.0.0.1",]


### not: db degistirilince eski bilgiler hep gider. yeniden migrate yapilir. 

        ## Asagidaki kodu inceleyelim: 
        ### Mesajlarin nasil görünecegini belirliyoruz: 
        ## dosya kismina bakarsak;  debug.log diye bir dosya olusturur. Burada belirttigimiz formata göre kaydeder. 
        ## developer ortaminda loglari sakla diyoruz. Tüm loglari saklar ama bizim burada yazdigimiz koda göre saklar. sadece error dersek error lari kaydeder. info dersek in seviyesi ve yukarisindakiler gelir. Bu ne ise yarar. Projeyi bu dosyadan takip edebiliirz. Nerede hatalar var diye. Warning yazarsak; bu durumda browser da yaptiimiz isteklerden basarili dönmüs olanlari almaz. sadece warning ve üzerini alir. basarili olanlarda gelsin istersek info kullanmamiz gerekir. 
LOGGING = {
    "version": 1,
    # is set to True then all loggers from the default configuration will be disabled.
    "disable_existing_loggers": True,
    # Formatters describe the exact format of that text of a log record.
    "formatters": {
        "standard": {
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s"
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    # The handler is the engine that determines what happens to each message in a logger.
    # It describes a particular logging behavior, such as writing a message to the screen,
    # to a file, or to a network socket.
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",   ############## 
            "level": "INFO",  ###  ############### 
            "stream": "ext://sys.stdout",
        },
        'file': {
            'class': 'logging.FileHandler',
            "formatter": "verbose",
            'filename': './debug.log',
            'level': 'WARNING',
        },
    },
    # A logger is the entry point into the logging system.
    "loggers": {
        "django": {
            "handlers": ["console", 'file'],
            # log level describes the severity of the messages that the logger will handle.
            "level": config("DJANGO_LOG_LEVEL", "INFO"),
            'propagate': True,
            # If False, this means that log messages written to django.request
            # will not be handled by the django logger.
        },
    }, 
}


## burada yazdigimiz tempalte standart template. 

