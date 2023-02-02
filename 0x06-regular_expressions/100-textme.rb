#!/usr/bin/env ruby
text = ARGV[0]
sender = text.match(/\[from:(.*?)\]/)[1]
receiver = text.match(/\[to:(.*?)\]/)[1]
flags = text.match(/\[flags:(.*?)\]/)[1]

puts "#{sender},#{receiver},#{flags}"
