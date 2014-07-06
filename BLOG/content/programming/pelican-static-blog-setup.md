Title: How to set up a Pelican static blog site
Date: 2014-06-21 20:21
Tags: python

Pelican is an open source project that converts static text files into an html site.


**`sudo pip install pelican Markdown `**
> - installing both the pelican and the Markdown packages
> - optionally use virtualenv venv; source venv/bin/activate

**`pelican-quickstart`**

    :::text
    Welcome to pelican-quickstart v3.3.0.
    This script will help you create a new Pelican-based website.
    Please answer the following questions so this script can generate the files needed by Pelican.

    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? johnpfeiffer.bitbucket.org
    > Who will be the author of this web site? john pfeiffer
    > What will be the default language of this web site? [en]
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
    > What is your URL prefix? (see above example; no trailing slash) https://johnpfeiffer.bitbucket.org
    > Do you want to enable article pagination? (Y/n)
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
    > Do you want to upload your website using FTP? (y/N)
    > Do you want to upload your website using SSH? (y/N)
    > Do you want to upload your website using Dropbox? (y/N)
    > Do you want to upload your website using S3? (y/N)
    > Do you want to upload your website using Rackspace Cloud Files? (y/N)
    Done. Your new project is available at /home/ubuntu/BLOG

- - - 

`tree`

    :::text
    .
    ├── content
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── output
    ├── pelicanconf.py
    └── publishconf.py
    
    2 directories, 5 files

- - -

`mkdir -p content/images`

`mkdir -p content/pages`

`vi content/hello_world.md`

    :::text
    Title: My first blog post
    Date: 2014-06-21 20:20
    Tags: python
    Slug: my-first-blog-post
    Author: John Pfeiffer
    Summary: Short version for index and feeds

    This is the content of my first blog post.

- - - 

`make devserver`
> ...Starting up Pelican and pelican.server...

`./develop_server.sh stop`
>  stop the dev server (required if reloading the .conf file)

**This only works with the basic first setup, after that it is better to manually use multiple screens:**

`make clean`

`make regenerate`
> auto detects any content changes and reloads itself

`cd output; python -m SimpleHTTPServer`
> Serving HTTP on 0.0.0.0 port 8000 ... (Control + C to quit)

**http://localhost:8000**

- - -

```vi pelicanconf.py```

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- #
    from __future__ import unicode_literals

    AUTHOR = u'john pfeiffer'
    SITENAME = u'johnpfeiffer'
    SITEURL = ''

    # Feed generation is usually not desired when developing
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None

    # Blogroll
    LINKS =  (('CV', 'https://www.linkedin.com/in/foupfeiffer'),
        ('source code', 'https://bitbucket.org/johnpfeiffer'))

    # DEFAULT_PAGINATION = 10

    # Uncomment following line if you want document-relative URLs when developing
    #RELATIVE_URLS = True

    STATIC_PATHS = ['images'] 

- - -

### Importing from drupal (work in progress) ###

    :::bash
    sudo apt-get install pandoc
    sudo pip install feedparser
    pelican-import -h
    pelican-import --feed http://blog.example.com/rss.xml -o output/ -m markdown

NEED TO HACK DRUPAL DO TO MORE THAN 10 STORES IN THE RSS FEED

- - -

https://github.com/getpelican/pelican-themes
git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes
http://pelican.readthedocs.org/en/latest/pelican-themes.html
sudo pelican-themes --install ~/pelican-themes/foundation-default-colours
  Installing themes...
  Copying `/home/ubuntu/pelican-themes/foundation-default-colours' to `/usr/local/lib/python2.7/dist-packages/pelican/themes/foundation-default-colours' ...
pelican-themes --list

vi pelicanconf.py
THEME = "/home/ubuntu/pelican-themes/foundation-default-colours"


Tweaking default syntax highlighting: http://pygments.org/docs/lexers/
