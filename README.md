**forked from [tmountain/Super-Smack](https://github.com/tmountain/Super-Smack)**

[![Build Status](https://travis-ci.org/winebarrel/super-smack.svg?branch=master)](https://travis-ci.org/winebarrel/super-smack)

The official Super Smack project seems to be abandoned. This version
includes a few small changes to allow it to compile properly with
newer versions of g++. Specifically, it fixes compilation on CentOS 5.7.

# README for MySQL Super Smack

Super Smack is a database benchmarking tool. It currently supports
MySQL and PosgreSQL, and has some initial infrastructure for
Oracle. Refer to the INSTALL file for installation instructions. To
learn how to write your own tests, see TUTORIAL, and also study the
examples in the smack directory, and read the comments.

The CHANGES file will tell you what is new in this release.

If you are interested in adding support for Oracle, or other
databases, please go ahead and do it - I will accept the patch and
include it in the distribution. If you ever wanted your name to be in
the MySQL manual, this is your chance. To see what you need to do,
take a look at mysql-client.* and pg-client.* - you need to subclass
Client and implement all pure virtual functions.

Super Smack was hosted at MySQL AB when Sasha Pachev worked there, but
was moved to Jeremy Zawodny's MySQL site:

  http://jeremy.zawodny.com/mysql/super-smack/

and now hosted by Tony Bourke: 

  http://vegan.net/tony/supersmack/

Tony Bourke / tony@vegan.net
