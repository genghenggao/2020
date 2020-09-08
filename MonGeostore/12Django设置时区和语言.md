### 设置时区和语言

- Django默认使用美国时间和英语，在项目的settings文件中，如下所示

```
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

- 我们把它改为`亚洲/上海`时间和中文

```
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
```



