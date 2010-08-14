YABT - Yet Another Bug Tracker
==============================
Because the world needs more bug trackers–really.

.. Caution::
    This project is in a state of flux.  Feel free to use it, and please
    contribute your thoughts, but be warned that every can, and probably will
    break quite regularly until it reaches 1.0.

.. WARNING::
    This README is the expected state of this project.  Until this warning is
    removed, what is described here and what is actually in the repository **do
    not** match.

YABT (pronounced yeah-bit) provides a plain text issue tracker that is meant to
be stored along side your project's source code inside its repository.  Tickets
are tracked in the ``.yabt/tickets/`` directory along the same lines as
`Jekyll`_.  In other words::

    ---
    ID: <some unique ID>
    Creator: Travis Swicegood <travis@domain51.com>
    CreatedOn: 2010-04-26 12:11:41
    Subject: Sample ticket in YABT
    ---
    There's some great content in here.

The idea is simple.  Files inside the YABT directory are scanned for `YAML
Front Matter`_.  When found, they're scanned and added to the list of tickets.
YAML Front Matter is denoted by two ``---`` lines, one on the first line of the
file, and another at the end of the headers.

The body can be whatever you want it to be.  It's plain text in its simplest
form, just like an email.  You could use MIME style separators to include
multiple versions, you could store the body as YAML, JSON, XML, or any other
number of things you want.  That's the reason for it being free-form, you get
to choose your own style.


YAML Front Matter
-----------------
You can include whatever you like within the YAML front matter.  It serves as a
header for the ticket and includes the meta data about it.  There are two cases
where values are reserved:


ID
  This should be unique.  By default, it is a `SHA-1`_ hash of the
  ``CreatedOn``, ``Creator``, and ``Subject`` fields.

YABT-*
  Any field that begins with ``YABT-`` is considered reserved.



.. _Jekyll: http://github.com/mojombo/jekyll
.. _YAML Front Matter: http://wiki.github.com/mojombo/jekyll/yaml-front-matter
.. _SHA-1: http://en.wikipedia.org/wiki/SHA-1
