****************************
  Examples
****************************

A basic program that uses ``python-shield`` looks like this:

First, import the library and exceptions.

::

    import shieldrpc
    from shieldrpc.exceptions import InsufficientFunds

Then, we connect to the currently running ``shield`` instance of the current user on the local machine
with one call to
:func:`~shieldrpc.connect_to_local`. This returns a :class:`~shieldrpc.connection.shieldConnection` objects:

::

    conn = shieldrpc.connect_to_local()

Try to move one shield from account ``testaccount`` to account ``testaccount2`` using 
:func:`~shieldrpc.connection.shieldConnection.move`. Catch the :class:`~shieldrpc.exceptions.InsufficientFunds`
exception in the case the originating account is broke:

::  

    try: 
        conn.move("testaccount", "testaccount2", 1.0)
    except InsufficientFunds,e:
        print "Account does not have enough funds available!"


Retrieve general server information with :func:`~shieldrpc.connection.shieldConnection.getinfo` and print some statistics:

::

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
  

