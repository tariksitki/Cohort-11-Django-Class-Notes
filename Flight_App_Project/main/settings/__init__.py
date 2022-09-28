
from .base import *

env_name = config("ENV_NAME")
if env_name == "dev":
    from .dev import *
elif env_name == "prod":
    from .prod import *


### bu dosya ilk calistiginda calisacak dosya. Bu nedenle burada hangisini yüklersek o calisir tüm projede. 

## Önemli: pgadminde  sql de olusturdugumuz database ismini SQL_DATABASE kismina yaziyoruz. .env dosyasinda.
## create database dedigimizde yazdigimiz ismi buraya yaziyoruz. 
## sifre kismina da db de kullandigimiz sifreyi yaziyoruz. 

