# Django-loki
Python logging handler and formatter with grafana/loki for django

# Install Grafana

This section discusses the hardware and software requirements as well as the process of installing Grafana on different operating systems. This section has the following topics:

- [Requirements](https://grafana.com/docs/grafana/latest/installation/requirements/)

- [Install on Debian or Ubuntu](https://grafana.com/docs/grafana/latest/installation/debian/)

- [Install on RPM-based Linux (CentOS, Fedora, OpenSuse, RedHat)](https://grafana.com/docs/grafana/latest/installation/rpm/)

- [Install on macOS](https://grafana.com/docs/grafana/latest/installation/mac/)

- [Install on Windows](https://grafana.com/docs/grafana/latest/installation/windows/)

- [Run Docker image](https://grafana.com/docs/grafana/latest/installation/docker/)

- [Deploy Grafana on Kubernetes](https://grafana.com/docs/grafana/latest/installation/kubernetes/)

  ![Grafana](./images/grafana.png)

# Install Loki

## Installation methods

Instructions for different methods of installing Loki and Promtail.

- [Install using Tanka (recommended)](https://grafana.com/docs/loki/latest/installation/tanka/)

- [Install through Helm](https://grafana.com/docs/loki/latest/installation/helm/)

- [Install through Docker or Docker Compose](https://grafana.com/docs/loki/latest/installation/docker/)

- [Install and run locally](https://grafana.com/docs/loki/latest/installation/local/)

- [Install from source](https://grafana.com/docs/loki/latest/installation/install-from-source/)

  ![django-log](./images/django-log.png)

# Installation

Using pip:

```shell
pip install django-loki
```

# Django-loki Usage

`LokiHttpHandler` is a custom logging handler which sends Loki-messages using `http` or `https`.

Modify your `settings.py` to integrate `django-loki` with Django's logging:

```python
LOGGING = {
    ...
    'formatters': {
        'loki': {
            'class': 'django_loki.LokiFormatter',  # required
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] [%(funcName)s] %(message)s',  # optional, default is logging.BASIC_FORMAT
            'datefmt': '%Y-%m-%d %H:%M:%S',  # optional, default is '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'loki': {
            'level': 'DEBUG',  # required
            'class': 'django_loki.LokiHttpHandler',  # required
            'host': '192.168.57.242',  # required, your grafana/Loki server host, e.g:192.168.57.242
            'formatter': 'loki',  # required, loki formatter,
            'port': 3100,  # optional, your grafana/Loki server port, default is 3100
            'timeout': 0.5,  # optional, request Loki-server by http or https time out, default is 0.5
            'protocol': 'http',  # optional, Loki-server protocol, default is http
            'source': 'Loki',  # optional, label name for Loki, default is Loki
            'src_host': 'localhost',  # optional, label name for Loki, default is Loki
            'tz': 'UTC',  # optional, timezone for formatting timestamp, default is UTC, e.g:Asia/Shanghai
        },
    },
    'loggers': {
        'django': {
            'handlers': ['loki'],
            'level': 'INFO',
            'propagate': False,
        }
    },
    ...
}
```

