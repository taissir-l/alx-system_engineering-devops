#!/usr/bin/env ruby
# regular expression that is matches a string that starts with h  and
# ends with n, it can have any single character in between
puts ARGV[0].scan(/h.n/).join
