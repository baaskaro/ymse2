Django-google-auth2
===================

python-social-auth을 이용한 Django 로그인 연동.


Python Package
--------------
Django==1.9.7
python-social-auth==0.2.19

### Setting

    INSTALLED_APPS = [
        ...
        'app',
        'social.apps.django_app.default',
    ]
    
    AUTHENTICATION_BACKENDS = [
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    ]

    PIPELINE = [
        'social.pipeline.social_auth.social_details',
        'social.pipeline.social_auth.social_uid',
        'social.pipeline.social_auth.auth_allowed',
        'social.pipeline.social_auth.social_user',
        'social.pipeline.user.get_username',
        # 'social.pipeline.mail.mail_validation',
        'social.pipeline.social_auth.associate_by_email',
        'social.pipeline.user.create_user',
        'social.pipeline.social_auth.associate_user',
        'social.pipeline.social_auth.load_extra_data',
        'social.pipeline.user.user_details'
    ]
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
    
                    'social.apps.django_app.context_processors.backends',
                    'social.apps.django_app.context_processors.login_redirect',
                ],
            },
        },
    ]
    
    SOCIAL_AUTH_FACEBOOK_KEY = ''
    SOCIAL_AUTH_FACEBOOK_SECRET = ''
    
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
    
    SOCIAL_AUTH_TWITTER_KEY = ''
    SOCIAL_AUTH_TWITTER_SECRET = ''
    
### google_auth2/urls.py

    from django.conf.urls import url, include
    from django.contrib import admin
    
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^djloginapp/', include('app.urls')),
        url('', include('social.apps.django_app.urls', namespace='social')),
        url('', include('django.contrib.auth.urls', namespace='auth')),
    ]
    
### app/urls.py

    from django.conf.urls import url
    from . import views
    
    urlpatterns = [
        # url(r'^$', views.index, name='index'),
        url(r'^$', views.home, name='home'),
    ]


### app/views.py

    from django.http import HttpResponse
    from django.shortcuts import render, render_to_response
    
    # Create your views here.
    from django.template import RequestContext
    
    
    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
    
    
    def home(request):
        context = RequestContext(request,
                                 {'request': request,
                                  'user': request.user})
        return render_to_response('home.html',
                                  context_instance=context)


### app/templates/base.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{% block title %}Authentication Tutorial{% endblock %}</title>
    
        <!-- Bootstrap -->
        <link href="/static/css/bootstrap.min.css" rel="stylesheet">
        <link href="/static/css/bootstrap-theme.min.css" rel="stylesheet">
        <link href="/static/css/fbposter.css" rel="stylesheet">
    
        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
         <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
         <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
       <![endif]-->
    </head>
    <body>
    {% block main %}{% endblock %}
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/static/js/bootstrap.min.js"></script>
    </body>
    </html>

### app/templates/home.html

    {% extends 'base.html' %}
    
    {% block main %}
        <div>
            <h1>authentication demo</h1>
    
            <p>
            <ul>
                {% if user and not user.is_anonymous %}
                    <li>
                        <a>Hello {{ user.get_full_name|default:user.username }}!</a>
                    </li>
                    <li>
                        <a href="{% url 'auth:logout' %}?next={{ request.path }}">Logout</a>
                    </li>
                {% else %}
                    <li>
                        <a href="{% url 'social:begin' 'facebook' %}?next={{ request.path }}">Login with Facebook</a>
                    </li>
                    <li>
                        <a href="{% url 'social:begin' 'google-oauth2' %}?next={{ request.path }}">Login with Google</a>
                    </li>
                    <li>
                        <a href="{% url 'social:begin' 'twitter' %}?next={{ request.path }}">Login with Twitter</a>
                    </li>
                {% endif %}
            </ul>
            </p>
        </div>
    {% endblock %}
    
### 출처 

[Google Authentication to a Django Application] (http://artandlogic.com/2014/04/tutorial-adding-facebooktwittergoogle-authentication-to-a-django-application/)