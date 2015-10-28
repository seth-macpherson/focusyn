# focusyn

__focusyn__ is an easy-to-use command line program that blocks websites known to distract us from our work, which is forked from [leftnode/get-crap-done](https://github.com/leftnode/get-shit-done).

### 2. Using Git:

Clone the Git repository:

    $ git clone git://github.com/soimort/focusyn.git
    $ [sudo] python setup.py install

## Usage

### 1. Configuration

`distractions` is a no-brainer plain text file contains a load of distractions that may distract you from work, line by line.

    twitter.com
    plus.google.com
    reddit.com

On *nix systems, put your `distractions` into:

    /etc/distractions

Or: (recommended!)

    ~/.config/distractions

On Windows, put it into your user directory:

    .config/distractions

### 2. To focus

Execute it as root because it modifies your hosts file and restarts your network daemon.

    $ sudo focus work

### 3. To no longer focus

    $ sudo focus play

## Additional Tips

You can, of course, use `focus` with your `crontab`, to control your work time and play time during the day. Whatever, I should say self-control is always the best.



## Acknowledgement

Thanks to Vic Cherubini, the original author of __focus__.
