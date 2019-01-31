class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_dic = {
            0: "Zero",
            1: "One", 2: "Two", 3: "Three",
            4: "Four", 5: "Five", 6: "Six",
            7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion",
        }

        res = []
        for d in (1000000000, 1000000, 1000, 100):
            if num >= d:
                prefix, num = divmod(num, d)
                res.append(self.numberToWords(prefix))
                res.append(num_dic[d])
        if 9 < num < 20:
            res.append(num_dic[num])
        else:
            if num > 19:
                res.append(num_dic[num - num % 10])
            num %= 10
            if not res and not num or num:
                res.append(num_dic[num])

        return(' '.join(res))
