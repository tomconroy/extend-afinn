

common = File.open('common-words.txt')
output = File.open('common-words-parsed.txt', 'w')

common.lines.each do |line|
  m = /\[(.+)%/.match(line)
  puts m[1]
  output.puts m[1]
end