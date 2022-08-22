'''
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
'''

'''
The hard part here is how decoder knows how to distinguish words. 
There might not only be chars in the input, so we cannot simply put a # in front of each word when encode
If we figure out what to do in encoder, it will be easy in decoder
'''

'''
思路：
encoder: for each word, add length of the word and a # in front of it
decoder: loop through the input string, for str[i], it should be the length, so we let j = i, add 1 to j till hit #
         length = str[i:j] -> it might be more than one digit
         first word would be str[j+1:j+length+1]
         update i = j+length+1
'''

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        results = ""
        for s in strs:
            results=results+str(len(s))+"#"+s
        return results
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j+1+length
        return res
        
        
# Time complexity : O(n)
