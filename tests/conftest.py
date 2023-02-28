import pytest
import os
from selenium import webdriver

browsers = {
    "firefox": webdriver.Firefox,
    #'PhantomJS': webdriver.PhantomJS,
    #'chrome': webdriver.Chrome,
}

browser_options = {"firefox": webdriver.FirefoxOptions()}

browser_options["firefox"].add_argument("--headless")


@pytest.fixture(scope="session", params=browsers.keys())
def driver(request):
    b = browsers[request.param](options=browser_options[request.param])

    request.addfinalizer(lambda *args: b.quit())

    return b


def pytest_configure():
    import django
    from django.conf import settings

    settings.configure(
        DEBUG=False,
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={
            "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
        },
        SITE_ID=1,
        SECRET_KEY="not very secret in tests",
        USE_I18N=True,
        USE_L10N=True,
        STATIC_URL="/static/",
        ROOT_URLCONF="tests.urls",
        TEMPLATE_LOADERS=(
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ),
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.template.context_processors.tz",
                        "django.contrib.messages.context_processors.messages",
                    ],
                },
            },
        ],
        MIDDLEWARE=(
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ),
        INSTALLED_APPS=(
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.sites",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "admin_async_upload",
            "tests",
        ),
        PASSWORD_HASHERS=("django.contrib.auth.hashers.MD5PasswordHasher",),
        MEDIA_ROOT=os.path.join(os.path.dirname(__file__), "media"),
    )
    try:
        import django

        django.setup()
    except AttributeError:
        pass
