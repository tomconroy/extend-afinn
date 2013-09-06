require 'set'

common_words = File.open('common-words-parsed.txt')
adjectives = File.open('adjectives-parsed.txt')
common_adjectives = File.open('common-adjectives-parsed.txt', 'w')

common_words_array = []
adjectives_array = []

adjectives.each_line do |adj|
  adjectives_array.push adj.strip
end
common_words.each_line do |word|
  common_words_array.push word.strip
end


common_adjectives_set = adjectives_array.to_set & common_words_array.to_set


common_adjectives_set.each do |word|
  common_adjectives.puts word
end