=====
Setup
=====

Before jumping into features of the language, let's get ourselves setup.
Both
`Kotlin <https://try.kotlinlang.org/>`_
and
`Python <http://pythonfiddle.com>`_
have sites that let you enter and evaluate code in
a browser. For our purposes, let's compare getting a real, local setup for
each language.

The Language
============

Getting Python and Java installed are similar exercise, but with different
obstacles. For Python, while two of the major platforms ship a Python,
everybody on earth will beat you over the head if you use "the system
Python". For Java, it is not installed by default on most platforms.

Thus, both Python and Java mean an initial, joyful step into the "How do I
install it?" thicket.

This is covered in depth elsewhere, so we'll skip it. From a Pythonista's
perspective, it's pretty similar. You have to make some choices about which
Java distribution, but we have some dirty laundry here as well -- 2 vs. 3,
python.org vs. platform-y Homebrew etc. vs. Anaconda, PyPy vs. Jython vs.
weird experiment of the week.

Call this one a tie.

The IDE
=======

We're JetBrains: we're going to use the IDE as the entry point for
making a project. For both Python and Kotlin, you might make your new
project environment from the command line and then open it.

Let's use the IDE make our project, following along with the very-useful
`Getting Started with IntelliJ IDEA <https://kotlinlang.org/docs/tutorials/getting-started.html>`_
documentation.

The Project
===========

In PyCharm, you fire it up and have 3 choices: create a new project from
scratch, open a directory on disk, or get a clone from a VCS system. In the
first, you can choose from some project templates, but you then have the
important part regarding this article:

[screenshot of create new project]

In Python, we're encouraged to put each project in isolation using
*virtual environments*. Yet because it is optional, people forget to, and
create a world of hurt for themselves. Or they decide to do it, and are
confronted with choices and complexity which hurt their brain. PyCharm
helps make some of that pain go away:

[screenshot of new interpeter screen]

With two decisions -- project type and project interpreter -- you now have a
new project and environment. PyCharm made some decisions for you, the level
of magic is one degree away.

When creating a Kotlin project, you'll confront some technologies that you
are unfamiliar with. These are important decisions. Let's walk through
them.

*Go through step by step: SDK, facets, Gradle, class paths -- all from a
Python perspective*

Virtual environments and
:doc:`package management <../packages/index>`
are places where Python is behind. At the same time, the complexity is
limited. Java (and for that matter, NodeJS) have stronger stories, but you
can't take a step in without feeling pretty dumb about the huge concepts
that you don't know.

I wanted to be impartial and call this one against Python. I can't. It's a
draw.

Project Layout
==============

In Python, that's about it. You could, at this point, just make a ``.py``
file and nobody would complain. Maybe a ``.gitignore``.

You could, of course, be a grown-up and make a Python *package*. You'd then
be teleported into a world of confusion: ``setup.py`` vs.
``requirements.txt`` (vs. ``Pipfile`` vs. ``buildout.cfg``), ``MANIFEST.in``,
``setup.cfg``, do I put my sources under ``project_name`` or
``src/project_name``. But those are university politics, not state-ordered
mandates.

Talk about: src/main/kotlin/someFile.kt and whether that path matters,
vs. com.pauleveritt.projectname and how that affects choices.
