class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        result = [0 for _ in range(len(num1) + len(num2))]

        for i in range(len(num1)):
            for j in range(len(num2)):
                result[-(i+j)-1] += (ord(num1[-i-1]) - ord('0')) * \
                                    (ord(num2[-j-1]) - ord('0'))

                if result[-(i+j)-1] > 9:
                    result[-(i+j)-2] += result[-(i+j)-1] // 10
                    result[-(i+j)-1] = result[-(i+j)-1] % 10
            
        for i, e in enumerate(result):
            if e != 0: break

        return ''.join([chr(r + ord('0')) for r in result[i:]])
