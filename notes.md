add the optimization of not using max on whole dictionary
using key= dictionary.get for problem 424. 
instead keep track of the number of times we've seen the
most frequently seen character so far. When we add a character, check 
is the count for seeing this character greater than our tracked number of the 
most frequently seen character so far? if so, we update it. This way we 
aren't using max over the entire dictionary, and instead are just comparing 
2 values.