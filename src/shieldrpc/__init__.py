# Copyright (c) 2010 Witchspace <witchspace81@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
shield-python - Easy-to-use shield API client
"""


def connect_to_local(filename=None):
    """
    Connect to default shield instance owned by this user, on this machine.

    Returns a :class:`~shieldrpc.connection.shieldConnection` object.

    Arguments:

        - `filename`: Path to a configuration file in a non-standard location (optional)
    """
    from shieldrpc.connection import shieldConnection
    from shieldrpc.config import read_default_config

    cfg = read_default_config(filename)
    if cfg is None:
        cfg = {}
    port = int(cfg.get('rpcport', '120103' if cfg.get('testnet') else '20103'))
    rpcuser = cfg.get('rpcuser', '')
    rpcpassword = cfg.get('rpcpassword', '')

    return shieldConnection(rpcuser, rpcpassword, 'localhost', port)


def connect_to_remote(user, password, host='localhost', port=20103,
                      use_https=False):
    """
    Connect to remote or alternative local shield client instance.

    Returns a :class:`~shieldrpc.connection.shieldConnection` object.
    """
    from shieldrpc.connection import shieldConnection

    return shieldConnection(user, password, host, port, use_https)
