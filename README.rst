collective.jazzport
===================

**collective.jazzport** is a yet another Zip export plugin for Plone.

It's a minimal export, supporting only those content types that get downloaded
as files by default.

It differs from the other zip exports in that it's implemented as a ZPublisher
stream iterator, which means that it releases Zope worker thread as soon as
possible and downloads all the zipped files separately through their public
URLs. (Note: this approach could be problematic HAProxy configured to allow
only fixed number of requests, but works great with Varnish' health check
approach.)

After activation, **collective.jazzport** displays **Download Zip** document
action, whenever its permission **collective.jazzport: Download Zip** is
available for the current user. By default, the permission is not given
to anyone, not even the Manager role.
