class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = sorted({i for i in time[:2] + time[3:]})
        idxs = [digits.index(time[i]) for i in (0,1,3,4)]
        
        print(digits, idxs, time, idxs[3], len(time)-1)
        if idxs[3] < len(digits) - 1: 
            return time[:4] + digits[idxs[3] + 1]
        elif idxs[2] < len(digits) - 1 and int(digits[idxs[2] + 1]) < 6:
            return time[:3] + digits[idxs[2] + 1] + digits[0]
        elif idxs[1] < len(digits) - 1 and \
        (int(time[0]) < 2 or int(time[0]) == 2 and int(digits[idxs[1] + 1]) < 4):
            return time[0] + digits[idxs[1] + 1] + ":" + digits[0] * 2
        elif idxs[0] < len(digits) - 1 and int(digits[idxs[0] + 1]) < 3:
            return digits[idxs[0] + 1] + digits[0] + ":" + digits[0] * 2
        else:
            return digits[0] * 2 + ":" + digits[0] * 2

    def nextClosestTime(self, time):
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = sorted({i for i in time[:2] + time[3:]})
        idxs = [digits.index(time[i]) for i in (0,1,3,4)]
        
        print(digits, idxs, time, idxs[3], len(time)-1)
        if idxs[3] < len(digits) - 1: 
            return time[:4] + digits[idxs[3] + 1]
        elif idxs[2] < len(digits) - 1 and int(digits[idxs[2] + 1]) < 6:
            return time[:3] + digits[idxs[2] + 1] + digits[0]
        elif idxs[1] < len(digits) - 1 and \
        (int(time[0]) < 2 or int(time[0]) == 2 and int(digits[idxs[1] + 1]) < 4):
            return time[0] + digits[idxs[1] + 1] + ":" + digits[0] * 2
        elif idxs[0] < len(digits) - 1 and int(digits[idxs[0] + 1]) < 3:
            return digits[idxs[0] + 1] + digits[0] + ":" + digits[0] * 2
        else:
            return digits[0] * 2 + ":" + digits[0] * 2
        
    def nextClosestTime(self, time):
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
            print(h1,h2,m1,m2)
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapsed = (cur - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed
        return "{:02d}:{:02d}".format(*divmod(ans, 60))

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(":")
        # Generate all possible 2 digit values
        # There are at most 16 sorted values here
        nums = sorted(set(hour + minute))
        two_digit_values = [a+b for a in nums for b in nums]
        print(nums, two_digit_values)
        # Check if the next valid minute is within the hour
        i = two_digit_values.index(minute)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "60":
            return hour + ":" + two_digit_values[i+1]

        # Check if the next valid hour is within the day
        i = two_digit_values.index(hour)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "24":
            return two_digit_values[i+1] + ":" + two_digit_values[0]
        
        return two_digit_values[0] + ":" + two_digit_values[0]    
