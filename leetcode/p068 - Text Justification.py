class Solution:
    def justify(self, line, line_width, maxWidth, left = False):
        if left or len(line) == 1:
            return ' '.join(line) + ' '*(maxWidth - line_width-len(line)+1)
        spacer_size = (maxWidth - line_width) // (len(line)-1)
        spacer_r = (maxWidth - line_width) % (len(line)-1)
        r = []
        for w in line[:-1]:
            r.extend([w, ' ' * spacer_size])
            if spacer_r > 0:
                r.append(' ')
                spacer_r -=1
        return ''.join(r+[line[-1]])
        
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        r = []
        line, line_width = [], 0

        for w in words:
            if line_width + len(w) + len(line) <= maxWidth:
                line.append(w)
                line_width += len(w)
            else:
                r.append(self.justify(line, line_width, maxWidth))
                line, line_width = [w], len(w)
                         
        r.append(self.justify(line, line_width, maxWidth, left = True))
        return r